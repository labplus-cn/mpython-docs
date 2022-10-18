.. currentmodule:: machine
.. _machine.Timer:

Class Timer -- Hardware Control Timer
======================================

Timer for hardware processing cycle and event time. Timers are probably the most flexible and heterogeneous hardware types in MCUs and SoCs, and vary greatly from one model to another. 
MicroPython's Timer class defines a baseline operation that performs callbacks within a given time period (or executes a callback after a delay), and allows a specific board to define more non-standard behaviors (so it cannot be ported to other boards). 

Reference for the timer callback :ref:`important constraints <machine_callbacks>`.

.. note::

    Memory cannot be allocated in the IRQ handler (interrupt), so exceptions raised in the handler will not provide much information.
    To understand how to resolve this limitation:func:`micropython.alloc_emergency_exception_buf` .

Construct object
------------

.. class:: Timer(id, ...)

Construct a new timer object with the given ID.

    - ``id`` - Any positive integer



Method
-------

.. method:: Timer.init(\*, mode=Timer.PERIODIC, period=-1, callback=None)


    - ``mode`` - Timer mode, can be one of the following:

        - ``Timer.ONE_SHOT`` - The timer runs once until the time limit of the configured channel expires. 
        - ``Timer.PERIODIC`` - The timer runs regularly at the channel's configured frequency。
    - ``period`` -  The period of the timer execution (in ms), executed once every period ms. Period range： 0 < period <= 3435973836
    - ``callback`` -  Timer callback function


Initialize timer, example::

    tim.init(period=100)                         # periodic with 100ms period
    tim.init(mode=Timer.ONE_SHOT, period=1000)   # one shot firing after 1000ms


.. method:: Timer.value()

Obtain and return the current count value of the timer.  

::

    value = tim.value()
    print(value)

.. method:: Timer.deinit()


Cancel the initialization of the timer. Stop the timer and disable timer peripherals. 


Constant
---------

.. data:: Timer.ONE_SHOT
.. data:: Timer.PERIODIC


.. literalinclude:: /../../examples/timer/timer_led_blink.py
    :caption: Timer control LED blink
    :linenos:
