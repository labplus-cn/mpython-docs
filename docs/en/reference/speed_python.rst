.. _speed_python:
Maximize MicroPython speed
============================

.. contents::

This tutorial introduces ways to improve MicroPython code. Optimization and other languages are introduced in other chapters (ie modules written in C and MicroPython inline assembly).

The development of high-performance code includes the following two stages, which we will introduce successively.

* Speed design
* Code and troubleshooting

Optimization steps:

* Identify the slowest section of code
* Improve the efficiency of Python code
* Use local code launcher
* Use Viper Code Launcher
* Use hardware-specific optimizations

Speed design
-------------------

Performance issues should be considered from the beginning. This involves parts of the code that are critical to performance, and special attention should be paid to the design of the code. 
The optimization process starts with checking the code: if the design has no errors from the beginning, then optimization is very easy, in fact, there may be no need for optimization.

Algorithm
~~~~~~~~~~

The most important part of designing a performance program is to ensure that the best algorithm is used. This should be an issue in the textbook instead of appearing in the MicroPython guide.
But sometimes considerable performance gains can be achieved by using algorithms of known efficiency.

RAM allocation
~~~~~~~~~~~~~~

To design efficient MicroPython code, it is necessary to understand how the interpreter allocates RAM. When an object is created or the size of the object grows (for example, an item is appended to the list), 
RAM is allocated from the block named heap. This process takes a long time and sometimes triggers the garbage collection process, which will take a few milliseconds.

Therefore, if the object is allowed to be created only once and its size cannot be increased, the performance of the function or method is improved. This means that the object persists during its use：
Usually the object is instantiated in the class constructor and used in various methods。

For more details, please see the following :ref:`Controlling garbage collection <controlling_gc>` below.

Buffer zone
~~~~~~~

The above example is a common situation where a buffer is required, such as a buffer used to communicate with a device. A typical drive will create a buffer in the constructor, 
And used in its I/O method, which will be called repeatedly.

MicroPython libraries usually provide support for pre-allocated buffers. For example, objects that support streaming interfaces (such as files or UART) are provided as
Read data to allocate a new buffer `read()` method, and read data into an existing buffer `readinto()` method. 

Floating point
~~~~~~~~~~~~~~

Some MicroPython ports allocate floating point numbers on the heap. Other ports may lack dedicated floating-point coprocessors, and perform arithmetic operations on them in "software" at a slower speed than on integers.
When performance matters, use integer arithmetic；In cases where performance is irrelevant, restrict floating-point numbers to the part of the code. For example, capture ADC readings as integer values into an array,
Then convert it to floating point number for signal processing.

Array
~~~~~~

Consider using various types of arrays instead of lists. The `array` module supports different item types, 8-bit items are supported by the built-in `bytes` and `bytearray` classes.
These data structures store items in consecutive memory locations. To avoid allocating memory in the critical section code, the memory should be pre-allocated and passed as a parameter or restricted object.

When passing an object fragment such as a `bytearray` instance, Python creates a copy, which involves size allocation proportional to the fragment size.
This can be mitigated using the `memoryview` object.  `memoryview` itself is allocated on the heap, but it is a small and fixed size object.

.. code:: python

    ba = bytearray(10000)  # big array
    func(ba[30:2000])      # a copy is passed, ~2K new allocation 传递一个副本，~2K新分配
    mv = memoryview(ba)    # small object is allocated 分配小对象
    func(mv[30:2000])      # a pointer to memory is passed 传递指向内存的指针

`memoryview` can only be applied to objects that support the buffer protocol-this includes arrays but not lists. Tip: The memoryview object is useful，
It retains the original buffer object. Therefore, memoryview is not a panacea. For example, in the above example, if you use 10K buffer to complete, 
Only 30 of them: 2000 bytes, so it is better to make a fragment, not use 10K buffer (garbage collection is ready), instead of doing a long memory view，
And keep a 10K blocked GC.

Nevertheless, `memoryview` is essential for advanced pre-allocated buffer management. The above `readinto()` method puts the data at the beginning of the buffer, 
And fill the entire buffer.  What should you do if you need to put the data into an existing buffer? Just create a memory view in the required part of the buffer,
And pass it to `readinto()` 。

Identify the slowest section of code
---------------------------------------

This process is also called profiling, which is described in the textbook, and this process is supported by different software tools (for standard Python).
For smaller embedded applications that may run on the MicroPython platform, the slowest function or method is usually passed correctly
Use the time series ``ticks``  function recorded in  `utime` to build. Code execution time can be calculated in milliseconds, microseconds and CPU cycle.

The following code can make any function or method time by adding ``@timed_function`` decorator:

.. code:: python

    def timed_function(f, *args, **kwargs):
        myname = str(f).split(' ')[1]
        def new_func(*args, **kwargs):
            t = utime.ticks_us()
            result = f(*args, **kwargs)
            delta = utime.ticks_diff(utime.ticks_us(), t)
            print('Function {} Time = {:6.3f}ms'.format(myname, delta/1000))
            return result
        return new_func

MicroPython code improvements
-----------------------------

const() declaration
~~~~~~~~~~~~~~~~~~~~~~~

MicroPython provides a ``const()`` statement. The operation mode is similar to ``#define`` in C language, because when the code is compiled into bytecode, 
The compiler will replace numeric values with identifiers. This can avoid looking up the dictionary at runtime. The parameter of ``const()`` can be any value that can be calculated as an integer at compile time,
Such as  ``0x100`` or ``1 << 8`` 。

.. _Caching:

Cache object reference
~~~~~~~~~~~~~~~~~~~~~~~~~~

In the case where a function or method repeatedly accesses an object, performance can be improved by caching the object in a local variable:

.. code:: python

    class foo(object):
        def __init__(self):
            ba = bytearray(100)
        def bar(self, obj_display):
            ba_ref = self.ba
            fb = obj_display.framebuffer
            # iterative code using these two objects 

This avoids repeated searches for ``self.ba`` and ``obj_display.framebuffer`` in the method  ``bar()`` .

.. _controlling_gc:

Control garbage collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

当需要内存分配时，MicroPython会尝试在堆上寻找适当大小的块。寻找可能会失败，通常是因为堆中堆满了代码不再引用的对象。
若发生故障，垃圾回收将回收冗余对象所占用的内存，然后再次尝试分配。此过程可能需要数毫秒。

周期性地发布 ``gc.collect()`` 可能对预防有帮助。首先，在真正需要回收之前进行回收速度会更快，
若经常回收，则耗时约1毫秒。其次，您可在代码中确定此时间的使用点，而非在随机点上发生较长的延迟，
可能在速度临界区。最后，经常进行回收可减少堆中的碎片化。严重的碎片化会导致无法修复的分配故障。

本地密码发射器
-----------------------

这使得MicroPython编译器发送本地CPU操作码，而非字节码。它涵盖了MicroPython的大部分功能，
所以大部分功能无需适应（见下文）。它是通过一个函数装饰器调用的:

.. code:: python

    @micropython.native
    def foo(self, arg):
        buf = self.linebuf # Cached object 缓存对象
        # code

目前本地代码发送器仍然存在一些局限性。

* 不支持上下文管理器（ ``with`` 语句）。
* 不支持生成器。
* 若使用 ``raise`` ，则必须应用一个参数。

性能提高的代价（约为字节码的两倍）是编译代码大小的增加。

Viper代码发送器
----------------------

上面讨论的优化包含符合标准的Python代码。 Viper代码发射器并不完全兼容。为实现高性能，它支持特殊的Viper本地数据类型。
整数处理并不兼容，因其使用机器字：32位硬件上的算法是执行模块2**32。

与本地发送器相似，Viper生成机器指令，但进行了进一步优化，大大提高了性能，尤其是在整数算法和位操作方面。其使用装饰器调用:

.. code:: python

    @micropython.viper
    def foo(self, arg: int) -> int:
        # code

如上所述，使用Python提示类型来辅助Viper优化器大有益处。类型提示提供参数的数据类型和返回值的信息；
这些是在此正式定义的标准Python语言特性 `PEP0484 <https://www.python.org/dev/peps/pep-0484/>`_.
Viper支持名为 ``int`` 、 ``uint`` （无符号整数）、 ``ptr`` 、 ``ptr8`` 、 ``ptr16`` 和 ``ptr32`` 的其自身的类型组。 ``ptrX``类型在下面进行介绍。
目前类型仅作一种用途：作为函数返回值的类型提示。若函数返回 ``0xffffffff`` ，Python将结果解释为2**32 -1而非-1。

除了本地发送器施加的限制之外，以下限制也适用:

* 函数可能有多达4个参数。
* 不许可默认参数值。
* 浮点数可能被使用但未优化。

Viper提供指针类型以协助优化器。这些包括

* ``ptr`` 指向对象的指针。
* ``ptr8`` 指向一个字节的指针。
* ``ptr16`` 指向一个16位半字的指针。
* ``ptr32`` 指向一个32位机器字的指针。

Python程序员可能不熟悉指针的概念。 它与Python `memoryview` 对象有相似之处，它可以直接访问存储在内存中的数据。
使用下标符号访问项目，但不支持片段：指针只能返回单个项目。其目的是提供快速随机访问存储在连续存储位置的数据--
例如存储在支持缓冲协议的对象中的数据，以及微控制器中存储器映射的外设寄存器。应该指出的是，使用指针编程很危险：
边界检查不会执行，编译器不会阻止缓冲区的超限错误。

典型的用法是缓存变量:

.. code:: python

    @micropython.viper
    def foo(self, arg: int) -> int:
        buf = ptr8(self.linebuf) # self.linebuf is a bytearray or bytes object 是一个字节数组或一个字节对象
        for x in range(20, 30):
            bar = buf[x] # Access a data item through the pointer 通过指针访问数据项目
            # code omitted 省略的代码

在此示例中，编译器"知道" ``buf`` 为字节组的地址；其可发送代码，以在运行时快速计算 ``buf[x]`` 的地址。
在使用转换将对象转换为Viper本机类型时，应在函数启动时执行，而不是在关键计时回路中执行，因为转换操作可能需要数微秒。转换要求如下:

* 转换操作符当前为: ``int``, ``bool``, ``uint``, ``ptr``, ``ptr8``, ``ptr16`` 和 ``ptr32``.
* 转换结果为本地Viper变量。
* 转换的参数可为Python对象或本地Viper变量。
* 若参数为本地Viper变量，则转换为仅改变类型（例如：从 ``uint`` 到 ``ptr8`` ）的空操作，所以您可使用此指针来储存/加载。
* 若参数为Python对象，且转换为 ``int`` 或 ``uint`` ，则Python对象须为整数类型，且返回该整数对象的值。
* 布尔转换的参数须为整数类型（布尔值或整数）；当用作返回类型时，Viper函数将返回True或False对象。
* 若参数为Python对象，转换为 ``ptr``、 ``ptr``、 ``ptr16`` 或 ``ptr32``，则Python对象须具有读写功能的缓冲区协议
 （在此情况下，返回指向缓冲区开始的指针）或为整数类型（在此情况下，返回整数对象的值）。

以下示例说明了使用 ``ptr16`` 转换来切换引脚X1 ``n`` 次:

.. code:: python

    BIT0 = const(1)
    @micropython.viper
    def toggle_n(n: int):
        odr = ptr16(stm.GPIOA + stm.GPIO_ODR)
        for _ in range(n):
            odr[0] ^= BIT0

这三个代码发送器的详细技术说明，请参见Kickstarter的 `Note 1 <https://www.kickstarter.com/projects/214379695/micro-python-python-for-microcontrollers/posts/664832>`_
和 `Note 2 <https://www.kickstarter.com/projects/214379695/micro-python-python-for-microcontrollers/posts/665145>`_

直接访问硬件
---------------------------

.. note::

    本节给出了Pyboard的代码示例。 不过，此处介绍的技术也可能适用于其他MicroPython端口。

这属于更高级的编程范畴，涉及目标MCU的一些知识。考虑切换Pyboard上的输出引脚的例子。标准方法是写入

.. code:: python

    mypin.value(mypin.value() ^ 1) # mypin was instantiated as an output pin实例化为输出引脚

这涉及两次调用 `Pin` 实例的 `value()` 方法的开销。通过对芯片的GPIO端口输出数据寄存器（odr）的相关位执行读/写操作，
可消除此开销。为实现这一点， ``stm`` 模块提供了一组提供相关寄存器地址的常量。引脚 ``P4`` （CPU引脚 ``A14`` ）的快速切换
（对应绿色LED）可按如下方式执行:

.. code:: python

    import machine
    import stm

    BIT14 = const(1 << 14)
    machine.mem16[stm.GPIOA + stm.GPIO_ODR] ^= BIT14
