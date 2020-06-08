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

When memory allocation is required, MicroPython will try to find blocks of appropriate size on the heap. The search may fail, usually because the heap is full of objects that the code no longer refers to.
If a failure occurs, garbage collection will reclaim the memory occupied by the redundant objects, and then try to allocate again. This process may take several milliseconds.

Periodically issuing ``gc.collect()`` may be helpful for prevention. Firstly, it will be faster to recycle before recycle is needed, if recycle frequently, it takes about 1 millisecond. 
Secondly, you can determine the use point of this time in the code, rather than a long delay at a random point may be in the speed critical section.
May be in the speed critical area. Severe fragmentation can cause irreparable allocation failures.

Local password transmitter
-----------------------

This causes the MicroPython compiler to send local CPU opcodes instead of bytecodes. It covers most features of MicroPython，
So most functions do not need to be adapted (see below). It is called through a function decorator:

.. code:: python

    @micropython.native
    def foo(self, arg):
        buf = self.linebuf # Cached object
        # code

At present, local code transmitters still have some limitations。

* No context manager support（ ``with`` statement）.
* No generator support. 
* If ``raise`` is used, a parameter must be applied，

The cost of improved performance (about twice the bytecode) is an increase in the size of the compiled code。

Viper Code transmitter
----------------------

The optimization discussed above contains standard-compliant Python code. Viper code transmitter is not fully compatible. For high performance, it supports special Viper local data types.
Integer processing is not compatible because it uses machine words: the algorithm on 32-bit hardware is the execution module 2**32. 

Similar to the local transmitter, Viper generates machine instructions, but has been further optimized to greatly improve performance, especially in integer algorithms and bit operations. It used a decorator call:

.. code:: python

    @micropython.viper
    def foo(self, arg: int) -> int:
        # code

As mentioned above, it is beneficial to use the Python hint type to assist the Viper optimizer. The type hint provides information about the data type and return value of the parameter；
These are the standard Python language features formally defined here `PEP0484 <https://www.python.org/dev/peps/pep-0484/>`_.
Viper supports its own type group named ``int`` 、 ``uint`` （unsigned integer）、 ``ptr`` 、 ``ptr8`` 、 ``ptr16`` and ``ptr32`` . The ``ptrX`` type is described below.
The current type is only used for one purpose：Type hints as function return values. If the function returns ``0xffffffff`` , Python interprets the result as 2**32 -1 instead of -1.

In addition to the restrictions imposed by the local transmitter, the following restrictions also apply:

* Function may have up to 4 parameters. 
* Disallow default parameter values.
* Floating point numbers may be used but not optimized.

Viper provides pointer types to assist the optimizer. These include

* ``ptr`` Pointer to object.
* ``ptr8`` Pointer to a byte.
* ``ptr16`` Pointer to a 16-bit halfword.
* ``ptr32`` Pointer to a 32-bit machine word.

Python programmers may not be familiar with the concept of pointers. It is similar to the Python `memoryview` object, it can directly access the data stored in memory. 
Use subscript symbols to access items, but clips are not supported：Pointer can only return a single item. Its purpose is to provide fast random access to data stored in continuous storage locations--
For example, data stored in objects that support the buffer protocol, and memory-mapped peripheral registers in the microcontroller. It should be noted that using pointer programming is dangerous：
Boundary checking will not be performed, and the compiler will not prevent buffer overrun errors.

Typical usage is to cache variables:

.. code:: python

    @micropython.viper
    def foo(self, arg: int) -> int:
        buf = ptr8(self.linebuf) # self.linebuf is a bytearray or bytes object
        for x in range(20, 30):
            bar = buf[x] # Access a data item through the pointer
            # code omitted 

In this example, the compiler "know" that ``buf`` is the address of the byte group；It can send code to quickly calculate the address of ``buf[x]`` at runtime.
When using conversion to convert an object to the Viper native type, it should be executed at function startup, not in a critical timing loop, because the conversion operation may take several microseconds. The conversion requirements are as follows:

* The current conversion operator are: ``int``, ``bool``, ``uint``, ``ptr``, ``ptr8``, ``ptr16`` and ``ptr32``.
* Conversion result to local Viper variable.
* Converted parameters can be Python objects or local Viper variables.
* If the parameter is a local Viper variable, it is converted to a no-operation that only changes the type（example: from  ``uint`` to ``ptr8`` ）, so you can use this pointer to store/load.
* If the parameter is a Python object and it is converted to ``int`` or ``uint`` , the Python object must be of integer type and return the value of the integer object.
* Boolean conversion parameters must be of integer type (boolean or integer)；When used as a return type, the Viper function will return True or False objects.
* If the parameter is a Python object, it is converted to  ``ptr``、 ``ptr``、 ``ptr16`` or ``ptr32`` , then the Python object must have a buffer protocol for reading and writing.
 (In this case, return a pointer to the beginning of the buffer) or an integer type (in this case, return the value of the integer object).

The following example illustrates the use of  ``ptr16`` conversion to switch pin X1 ``n`` times:

.. code:: python

    BIT0 = const(1)
    @micropython.viper
    def toggle_n(n: int):
        odr = ptr16(stm.GPIOA + stm.GPIO_ODR)
        for _ in range(n):
            odr[0] ^= BIT0

For detailed technical descriptions of these three code senders, please refer to Kickstarter `Note 1 <https://www.kickstarter.com/projects/214379695/micro-python-python-for-microcontrollers/posts/664832>`_
and `Note 2 <https://www.kickstarter.com/projects/214379695/micro-python-python-for-microcontrollers/posts/665145>`_

Direct hardware access
---------------------------

.. note::

    This section gives a code example of Pyboard.  However, the techniques described here may also be applicable to other MicroPython ports.

This belongs to the more advanced programming category and involves some knowledge of the target MCU. Consider the example of switching output pins on Pyboard. The standard method is to write

.. code:: python

    mypin.value(mypin.value() ^ 1) # mypin was instantiated as an output pin

This involves the expenses of calling the `value()` method of the `Pin` instance twice. Perform read/write operations on the relevant bits of the chip's GPIO port output data register (odr), 
This expenses can be eliminated. To achieve this, the ``stm`` module provides a set of constants that provide relevant register addresses. Quick switching of pin ``P4`` （CPU pin ``A14`` ）
(Corresponding to green LED) can be executed as follows:

.. code:: python

    import machine
    import stm

    BIT14 = const(1 << 14)
    machine.mem16[stm.GPIOA + stm.GPIO_ODR] ^= BIT14
