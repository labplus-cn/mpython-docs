.. _isr_rules:

Write interrupt handler
==========================

On the appropriate hardware, MicroPython provides the ability to write interrupt handlers in Python. Interrupt handler-also known as interrupt service routine (ISR), defined as a callback function.
These functions are all executed in response to events such as timer triggers or voltage changes on pins. These events may occur at any point in the execution of the program code.
This has a major impact, some of which are specific to the MicroPython language. Others are applicable to all systems that can respond to real-time events. This document covers language-related issues, 
And a brief introduction to real-time programming.

Some vague language such as "slow" and "as fast as possible" are used in the introduction, which is not unintentional because the speed depends on the application. 
The acceptable duration of ISR depends on several factors：The speed of interruption, the nature of the main program and the existence of other concurrent events.

Tips and recommended practice
------------------------------

Below is a deatil summary, and the main recommendations for the interrupt handler code。

* Try to keep the code short and simple。
* Avoid memory allocation: no additional lists or dictionaries inserted, no floating-point numbers。
* In the case where the ISR returns multiple bytes, use the pre-allocated ``bytearray`` . If multiple integers are shared between the ISR and the main program, use an array（ ``array.array`` ）.
* In the case of sharing data between the main program and the ISR, consider disabling interrupts before accessing the data in the main program and re-enabling it immediately afterwards (see Critical Sections)。
* Allocate emergency exception buffer (see below).


MicroPython issues
------------------

Emergency exception buffer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If an error occurs in the ISR, MicroPython cannot generate an error report unless a special buffer is created for it. If any program that uses interrupts contains the following code, debugging will be simplified.


.. code:: python

    import micropython
    micropython.alloc_emergency_exception_buf(100)

Simplify
~~~~~~~~~

For various reasons, it is important to keep the ISR code as short as possible. It should be after the incident；Do this：Deferrable operations should be delegated to the main program loop.
Typically, an ISR will handle the hardware device that caused the interrupt and prepare for the next interrupt. The ISR will communicate with the main loop, update the shared data to indicate that the interruption has occurred, and return. ISR should return control to the main loop as soon as possible. 
This is not a typical MicroPython problem, as detailed below（ :ref:`below <ISR>`）。

Communication between ISR and main program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usually, the ISR needs to communicate with the main program. The simplest communication method is through one or more shared data objects, declared as global or through a type of sharing (see below).
However, this method has many limitations and hazards, which will be described in detail below. Integers,  ``bytes`` and ``bytearray`` objects and arrays (from the array module, which can store multiple data types) are usually used for this purpose.

Object methods are used as callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MicroPython supports this powerful technology that enables ISR to share instance variables with the underlying code. It also enables classes that implement device drivers to support multiple device instances. The following example is to make the two LEDs flash at different rates.

.. code:: python

    import pyb, micropython
    micropython.alloc_emergency_exception_buf(100)
    class Foo(object):
        def __init__(self, timer, led):
            self.led = led
            timer.callback(self.cb)
        def cb(self, tim):
            self.led.toggle()

    red = Foo(pyb.Timer(4, freq=1), pyb.LED(1))
    greeen = Foo(pyb.Timer(2, freq=0.8), pyb.LED(2))

In this example, the ``red``  instance associates timer 4 with LED 1：When the timer 4 interrupt occurs, call ``red.cb()`` to change the state of LED 1.
The operation of the  ``green`` instance is similar：The interruption of timer 2 triggers the execution of ``green.cb()`` and switches LED 2. The use of example methods has two major benefits. 
First, a single class allows code to be shared among multiple hardware instances. Second, as the binding method, the first parameter of the callback function is ``self`` . 
This allows the callback to access instance data, and save state between successive callbacks. For example, if the above class puts the variable ``self.count``in the constructor.
Set to 0, ``cb()`` will increment the counter.  ``red`` 和 ``green`` instances will keep an independent count of the number of times each LED has changed state.

Create Python objects
~~~~~~~~~~~~~~~~~~~~~~~~~~

ISR cannot create instance of Python object. This is because MicroPython needs to allocate memory for objects from the storage of free memory blocks called heaps.
This is not allowed in the interrupt handler, because heap allocation is not reentrant. In other words, when the main program is performing allocation，
Interruptions may occur-to maintain the integrity of the heap, the interpreter does not allow memory allocation in ISR code.

One of its effects is that ISR cannot use floating point arithmetic；This is because floating point numbers are Python objects. Similarly, ISR cannot append items to the list.
In actual operation, it is difficult to determine exactly which code structure will try to perform memory allocation and raise an error message：Another reason to make ISR code as short as possible.

One way to avoid such problems is for ISR to use pre-allocated buffers. For example, a class constructor creates an instance of ``bytearray`` and a boolean flag.
The ISR method allocates data to a location in the buffer and sets a flag. When instantiating objects, memory allocation is implemented in the main program code, not in the ISR.

MicroPython library I/O methods usually provide the option of using pre-allocated buffers. Example, ``pyb.i2c.recv()`` can accept a variable buffer as its first parameter: this makes it usable in ISR.

The method of creating an object without using classes or global variables is as follows:

.. code:: python

    def set_volume(t, buf=bytearray(3)):
        buf[0] = 0xa5
        buf[1] = t >> 4
        buf[2] = 0x5a
        return buf

When the function is first loaded, the compiler instantiates the default  ``buf`` parameter (usually when the module in which it is located is imported).

Use Python objects
~~~~~~~~~~~~~~~~~~~~~

Due to the way Python objects operate, there are further restrictions on objects. When executing the ``import`` statement, Pyton code is compiled into byte code.
When running the code, the interpreter reads each byte of code and executes it as a set of machine code instructions. Given that interruptions can occur at any moment between machine code instructions, 
the original line of Python code may only be partially executed, Similar to a group, list or library modified in the main loop may lack internal consistency when an interrupt occurs.

Typical results are as follows. In rare cases, the ISR will run at the exact time when the object part is updated. When ISR tries to read the object, it will cause a crash.
Because such problems occur only in very few and random situations, it is difficult to diagnose. There are many ways to avoid this problem, please see
:ref:`Critical Sections <Critical>` below.

It is important to understand the composition of changes to objects. Problems with changes to built-in types such as dictionaries. Changing the contents of an array or byte array is relatively easy.
This is because bytes or words are written as a single machine code that can be interrupted：According to real-time programming, writing is atomic. User-defined objects may instantiate integers, arrays, or byte arrays,
Both the main loop and ISR can modify their contents.

MicroPython supports integers of arbitrary precision. Values between 2**30 -1 and -2**30 will be stored in a single machine word. Larger values are stored as Python objects.
Therefore, the modification of long integers is not considered atomic. Using long integers in ISR is not safe, because when the value of the variable changes, you may try to allocate memory.

Overcome floating point restrictions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generally, it is best to avoid floating point numbers in ISR：Hardware usually processes integers in the main loop and converts to floating point. However, there are some DSP algorithms that require floating point numbers.
On platforms with hardware floating-point numbers (such as Pyboard), the inline ARM Thumb assembler can be used to avoid this limitation. This is because the processor stores floating point values in machine words；
This is because the processor stores floating point values in machine words。

Exception
----------

If an abnormality occurs in the ISR, the abnormality will not propagate to the main loop. Unless the exception is handled by the ISR code, the interrupt will be disabled.

General questions
--------------

This is a short introduction to real-time programming. Beginners to take note：Design errors in real-time programming can lead to faults that are extremely difficult to diagnose. This is because they may rarely occur and the time interval of their occurrence is completely random.
It is important to ensure that the original design is accurate and predict the problem before it occurs. Both the interrupt handler and the main program need to consider the following issues during design.

.. _ISR:

Interrupt handler design
~~~~~~~~~~~~~~~~~~~~~~~~

As mentioned above, the design of ISRs should be as simple as possible, they should return within a short, predictable period of time. This is very important, when the ISR is running, the main loop is not running：The main loop will inevitably pause at random places in the code.
Such pauses can lead to faults that are more difficult to diagnose, especially when the duration of the pause is long or variable. To understand the running time of ISR, a basic understanding of interrupt priority is required.

Interrupts are organized through a priority scheme. The ISR code itself may be interrupted by a higher priority interrupt. If two interrupts share data (see Critical Sections below), it will have a certain impact.
If such an interrupt occurs, insert a delay in the ISR code. If a lower priority interrupt occurs while the ISR is running, the lower priority interrupt will be invalid. Another problem with slow ISR is：The second occurrence of the same type of interrupt in execution.
The second interrupt will be processed after the first interrupt is terminated. However, if the rate of subsequent interruptions still exceeds the value that the ISR can accommodate, the results will not be optimistic.

Therefore, the loop structure should be avoided or minimized. I/O should be avoided for devices other than interrupt devices：Such as disk access,  ``print`` statement and UART access are relatively low, and their durations vary.
Another problem here is that file system functions are not reentrant：You may encounter many problems when using file system I/O in the ISR or main program. It is important that the ISR should not wait for events. If you ensure that the code returns within the expected time，
If switching pins or LEDs, I/O is acceptable. It may be necessary to access the interrupt device via I2C or SPI, but the time spent on these accesses should be calculated and its impact on the application should be evaluated.

Usually need to share data between ISR and main loop. Can be shared by whole sentence variables or class or instance variables. Variables are usually integer or boolean types, integer or byte arrays (a pre-allocated integer array is faster than list access).
When ISR modifies multiple values, it is necessary to consider the case where the main program accesses some values (but not all values) and an interruption occurs. This leads to inconsistencies.

Consider the following design. The ISR stores the input data to the byte object, and adds the number of received bytes to the integer of the total number of bytes to be processed. The main program reads the number of bytes, processes the bytes, and clears the number of bytes ready.
After the main program reads the number of bytes and an interrupt occurs, this process begins to run. ISR puts the added data into the buffer and updates the received number, but the main program has read the number, so it processes the original received data.
New bytes waiting to be received are lost.

There are many ways to avoid this problem, the simplest is to use a ring buffer. If a structure with inherent thread safety cannot be used, other methods will be introduced below.

Reentrancy
~~~~~~~~~~

If a function or method is shared between the main program and one or more ISRs or between different ISRs, it may cause a potential problem. The function itself may be interrupted, another instance of the function runs.
If this problem occurs, the function must be designed to be reentrant. How to implement this design is an advanced task beyond the scope of this article.

.. _Critical:

Critical area
~~~~~~~~~~~~~~~~~

An example of a critical section of code is accessing multiple variables, which are affected by ISR. If the interruption occurs between accesses to a single variable, its value will be inconsistent.
This is an example of a problem called "race condition"：ISR and main program loop compete to modify variables. To avoid inconsistencies, a method must be adopted to ensure that the ISR does not modify the value during the critical period.
One way to achieve this is to issue  ``pyb.disable_irq()`` before the start of the critical section, and ``pyb.enable_irq()`` at the end of it. An example of this method:

.. code:: python

    import pyb, micropython, array
    micropython.alloc_emergency_exception_buf(100)

    class BoundsException(Exception):
        pass

    ARRAYSIZE = const(20)
    index = 0
    data = array.array('i', 0 for x in range(ARRAYSIZE))

    def callback1(t):
        global data, index
        for x in range(5):
            data[index] = pyb.rng() # simulate input 
            index += 1
            if index >= ARRAYSIZE:
                raise BoundsException('Array bounds exceeded')

    tim4 = pyb.Timer(4, freq=100, callback=callback1)

    for loop in range(1000):
        if index > 0:
            irq_state = pyb.disable_irq() # Start of critical section 
            for x in range(index):
                print(data[x])
            index = 0
            pyb.enable_irq(irq_state) # End of critical section 
            print('loop {}'.format(loop))
        pyb.delay(1)

    tim4.callback(None)

The critical section can contain a line of code and a variable. Consider the following code fragment.

.. code:: python

    count = 0
    def cb(): # An interrupt callback 
        count +=1
    def main():
        # Code to set up the interrupt callback omitted 
        while True:
            count += 1

This example illustrates the potential cause of the failure. The ``count += 1``  line in the main loop carries a specific race condition problem called "read-modify-write" . This is a typical cause of failures in real-time systems.
In the main loop, read the value of  ``t.counter`` , increase it by 1, and write it back. In a few cases, the interrupt occurs after reading and before writing. Interrupt the change ``t.counter`` , but its change is overwritten by the main loop when the ISR returns.
In real-time systems, this may cause very few, unpredictable failures.

As mentioned above, if you modify an instance of the Python built-in type in the main code or access the instance in the ISR, you should pay more attention. The code that executes the change should be considered a critical section to ensure that the instance of the ISR runtime is in a valid state.。

If data sets are shared between different ISRs, special attention should be paid. The problem here is that when the lower priority interrupt partially updates the shared data, the higher priority interrupt may occur at this time.
Handling this situation is an advanced task that is beyond the scope of this article, but the following mutex objects are sometimes available.

Disabling interrupts in the critical interval is the most common and simplest method, but it disables all interrupts, even interrupts that do not cause problems. Usually we don’t want to disable interrupts for a long time.
In the case of a timer interruption, it introduces variability to the moment the callback occurs. When the device is interrupted, it may cause the device to be serviced too late, may lose data or cause the device hardware to exceed the limit error.
Like ISR, the duration of the critical section in the main code should be short and predictable.

One way to deal with the critical section (to completely reduce the time to disable interrupts) is to use an object called "mutexes" (named after the concept of mutual exclusion). Lock the mutex before the main program runs the critical section, 
and unlock at the end. ISR tests if the mutex is locked. If locked, it avoids the critical section and returns. The problem with this design is how to define the behavior that the ISR should do when access to critical variables is denied.
此处提供互斥体的简单示例：
`here <https://github.com/peterhinch/micropython-samples.git>`_。注意：互斥体代码禁用了中断，但其禁用仅限于8个机器指令期间。
The advantage of this method is that it hardly affects other interrupts.

Interrupt and REPL
~~~~~~~~~~~~~~~~~~~~~~~

Interrupt handlers (such as timer-related interrupt handlers) can continue to run after the program ends. This may produce unexpected results, in which case you may expect that the object that triggered the callback is out of scope.
Example in Pyboard

.. code:: python

    def bar():
        foo = pyb.Timer(2, freq=4, callback=lambda t: print('.', end=''))

    bar()

This code will continue to run unless the timer is explicitly disabled or use ``ctrl D`` to reset the board.
