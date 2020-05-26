.. currentmodule:: machine
.. _machine.Pin:

.. module:: Pin

Class Pin -- control I/O pins
=============================

Pin objects are used to control I / O pins (also known as GPIO-general purpose input / output). Pin objects are usually associated with physical pins that can drive the output voltage and read the input voltage.
The pin class has a method to set the pin mode (IN, OUT, etc.) and a method to obtain and set the digital logic level. For analog control of pins, please refer to :class:`ADC` class.

Construct a pin object by using an identifier that explicitly specifies a certain I/O pin. The allowed identifier form and the physical pin to which the identifier is mapped are port-specific。
The possibility of the identifier is an integer, a string or a tuple with port and pin number.

Example::

    from machine import Pin

    # create an output pin on pin #32
    p0 = Pin(32, Pin.OUT)

    # set the value low then high
    p0.value(0)
    p0.value(1)

    # create an input pin on pin #33, with a pull up resistor
    p2 = Pin(33, Pin.IN, Pin.PULL_UP)


    # configure an irq callback
    p2.irq(trigger=Pin.IRQ_FALLING, handler=lambda t:print("IRQ"))

Build Object
------------

.. class:: Pin(id, mode=1, pull=1, value, drive, alt)

  Access the pin peripheral (GPIO pin)  ``id`` associated with the given. If other parameters are given in the build object, they are used to initialize the pins.
  Any settings not specified will maintain their previous state.

.. Attention:: The mPython control board provides its own pin mapping, mapping pins to GPIO of ESP32.For example, the P0 pin of the control board corresponds to the IO33 of ESP32, then you can use  ``Pin.P0`` to replace ``33`` .

Parameter:

  - ``id`` is mandatory and can be any object. Possible value types include：int (Internal pin identifier), str（Pin name）and tuple（[port，pin] match）. If you use mPython, you can use Pin.P(0~20), for example (Pin.P0)P0  pin provides mapping as GPIO.

  - ``mode`` specifies the pin mode, which can be one of the following：

    - ``Pin.IN`` - Pin is configured as input. If it is regarded as an output, the pin is in a high-impedance state.

    - ``Pin.OUT`` - Pin is configured as (normal) output.

    - ``Pin.OPEN_DRAIN`` - Pin is configured as an open-drain output. The open-drain output works in the following way：If the output value is set to 0, the pin is active low; if the output value is 1, the pin is high impedance. Not all ports implement this mode, or some ports may only be implemented on certain pins.

    - ``Pin.ALT_OPEN_DRAIN`` - Pin configuration as open drain。

  ``pull`` specifies whether a (weak) pull resistor is connected to the pin, which can be one of the following：

    - ``None`` - No pull-up or pull-down resistors
    - ``Pin.PULL_UP`` - Pull-up resistor enabled
    - ``Pin.PULL_DOWN`` - Pull-down resistor enabled

  - ``value`` is only valid for ``Pin.OUT`` and ``Pin.OPEN_DRAIN`` modes, and specifies the initial output pin value, otherwise the state of the pin peripherals remains unchanged.


Method
-------

.. method:: Pin.init(mode=1, pull=1, value, drive, alt)

   Reinitialize the pin with the given parameters. Only set the specified parameters. The rest of the pin peripheral state will remain unchanged.
   For detailed information about the parameters, see the build object documentation.

   Return ``None``.


.. method:: Pin.value([x])

  This method allows setting and getting the value of the pin, depending on whether ``x`` provides the parameter.

  If this parameter is omitted, the method obtains the digital logic level of the pin and returns 0 or 1 corresponding to the low voltage signal and the high voltage signal, respectively.
  The behavior of this method depends on the mode of the pin：

    - ``Pin.IN`` -  This method returns the actual input value currently present on the pin.
    - ``Pin.OUT`` - This method returns the actual input value currently present on the pin.
    - ``Pin.OPEN_DRAIN`` - If the pin is in state “0”, the behavior and return value of the method are undefined. Otherwise, if the pin is in state “1”, the method returns the actual input value currently present on the pin.

   
  If parameters are provided, this method sets the digital logic level of the pin. Parameter x can be any value converted to Boolean.
  If converted to True, set the pin to state “1”, otherwise set it to “0” state. The behavior of this method depends on the mode of the pin：



    - ``Pin.IN`` - This value is stored in the output buffer of the pin. The state of the pin will not change, it is still in a high impedance state. Once changed to ``Pin.OUT`` or ``Pin.OPEN_DRAIN`` mode, the stored value will be activated on the pin.
    - ``Pin.OUT`` -  The output buffer is immediately set to the given value.
    - ``Pin.OPEN_DRAIN`` - If the value is “0”,the pin is set to a low voltage state. Otherwise, the pin is set to high impedance.

  When setting the value returned by this method ``None``.

.. method:: Pin.__call__([x])

  Pin object is callable. The call method provides a (quick) shortcut to set and get the value of the pin. It is equivalent to Pin.value([x]). For details, see :meth:`Pin.value` 。

.. method:: Pin.on()

   Set the pin to high level

.. method:: Pin.off()

 Set the pin to low level

.. _Pin.irq:

.. method:: Pin.irq(handler=None, trigger=(Pin.IRQ_FALLING | Pin.IRQ_RISING), wake=None)

  Configure the interrupt handler to be called when the trigger source of the pin is active. If the pin mode is ``Pin.IN``, then the trigger source is the external value on the pin.
  If the pin mode is ``Pin.OUT``,  then the trigger source is the output buffer of the pin.
  Otherwise, if the pin mode is  ``Pin.OPEN_DRAIN``, then the trigger source is the output buffer of state '0' and the external pin value of state '1'.

  Parameter:

    - ``handler``  is an optional function that is called when the interrupt is triggered.

    - ``trigger`` configure events that can trigger an interrupt. Possible values are：

      - ``Pin.IRQ_FALLING`` falling interruption
      - ``Pin.IRQ_RISING`` rising interruption
      - ``Pin.IRQ_LOW_LEVEL`` low level interruption
      - ``Pin.IRQ_HIGH_LEVEL`` high level interruption
      - ``Pin.WAKE_HIGH`` Used for wake-up function, high level trigger
      - ``Pin.WAKE_LOW`` Used for wake-up function, low level trigger

      These values can be used to perform ``OR``  operations together to trigger multiple events.

    - ``wake`` select this interrupt to wake up the power mode of the system. It can be ``machine.IDLE`` ，``machine.SLEEP`` or ``machine.DEEPSLEEP`` . These values can also be “or” calculated together to cause pins to break in multiple power consumption modes.

  This method returns a callback object.  

Constant
---------
The board's own pin mapping maps of the mPython Board pins to the GPIO of ESP32
mPython 

.. data:: Pin.P0
          Pin.P1
          Pin.P2
          Pin.P3
          Pin.P4
          Pin.P5
          Pin.P6
          Pin.P7
          Pin.P8
          Pin.P9
          Pin.P10
          Pin.P11
          Pin.P13
          Pin.P14
          Pin.P15
          Pin.P16
          Pin.P19
          Pin.P20
          Pin.P23
          Pin.P24
          Pin.P25
          Pin.P26
          Pin.P27
          Pin.P28


The following constants are used to configure pin objects.

.. data:: Pin.IN
          Pin.OUT
          Pin.OPEN_DRAIN

  Select pin mode.

.. data:: Pin.PULL_UP
          Pin.PULL_DOWN
          Pin.PULL_HOLD

   Select whether there is a pull-up / pull-down resistor. Use  `None` value.

.. data:: Pin.IRQ_FALLING
          Pin.IRQ_RISING
          Pin.IRQ_LOW_LEVEL
          Pin.IRQ_HIGH_LEVEL

  Select IRQ trigger type.
