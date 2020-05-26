Key Button
====

There are two push buttons A and B on the upper edge of the control panel. Low level when the button is pressed, otherwise high level. 


The process of pressing the keys on the control panel A and B is as follows. When pressed, the level changes from high to low, and the moment when the high level (1) changes to the low level (0) is called the falling edge. When the button is released, the level changes from low to high, and the moment when the low level (0) changes to the high level (1) is called the rising edge.
We can get the current key state by getting the level change.

.. image:: /../images/tutorials/falling.png
    :align: center

----------------------------------------------

Obtain the key status
++++++++++

.. literalinclude:: /../../examples/button/button_ctl_led.py
    :caption: Example - Press A key to turn on the light, press B key to turn off the light.
    :linenos:

First, import the mpython module::

  from mpython import *

Pressed Button A and Button B::

  button_a.value() == 0      #Pressed button A
  button_b.value() == 0      #Pressed button B

.. Note::

  `` button_a`` is the object name of button A, and the object name of button B is `` button_b``, which is a derived class of `` machine.Pin`` and inherits the method of Pin, so you can use the `` value`` function to read the reference Pin value, return `` 1 '' for high level signal, return `` 0 '' for low level signal, so value == 1 when the button is not pressed, value == 0 when pressed. ``button_a`` is the object name of button A, and the object name of button B is ``button_b`` , which is a derived class of  ``machine.Pin`` and inherits the method of Pin, so you can use the  ``value`` function to read the reference Pin value, return ``1``  for high level signal, return ``0`` for low level signal, so value==1，when the button is not pressed, value==0 when pressed.


Key interrupt
++++++++

.. admonition:: What is an interrupt？

    In the process of running the program, the system has a situation that must be dealt with by the CPU immediately. At this time, the CPU temporarily suspends the execution of the program and turns to deal with this new situation.
    When there is a need, the CPU must suspend the current thing, handle other things, and then go back to execute the suspended thing after processing. 


.. literalinclude:: /../../examples/button/button_irq_ctl_led.py
    :caption: Example - Press button A to turn on the onboard lights and buzzer, press button B to turn off the onboard lights and buzzer.
    
    :linenos:
   
.. Note:: By default, the above program does not execute any instructions when the program is empty, etc. When the a and b keys are interrupted, the corresponding function is called back.


``button_a.irq(trigger=Pin.IRQ_FALLING, handler=ledon)`` It is the function corresponding to the interrupt handler called. `trigger` configuration can trigger interrupt events, possible values are：`Pin.IRQ_FALLING` Falling edge interrupt；`Pin.IRQ_RISING` Rising edge interrupt；`Pin.IRQ_LOW_LEVEL` low level interrupt；`Pin.IRQ_HIGH_LEVEL` high level interrupt. `handler`  is an optional function that is called when an interrupt is triggered and returns a callback object.
For detail, refers to :ref:`button_[a,b].irq<button.irq>`。

.. Attention:: When defining an interrupt handler function, the function must contain any  **ONE** parameter, otherwise it cannot be used. The parameters in theledon()、ledoff() functions are ``_`` .


