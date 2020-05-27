.. currentmodule:: machine
.. _machine.PWM:

Class PWM -- Pulse width modulation
=============================

Pulse Width Modulation (PWM) is a technique for obtaining analog results digitally.


Create object
------------

.. class:: PWM(pin, freq, duty)

Create a PWM object associated with a set pin. So you can write the analog value on that pin.

 - ``pin`` pins that support PWM  ``GPIO0``、``GPIO2``、``GPIO4``、``GPIO5``、``GPIO10``、``GPIO12~19``、``GPIO21``、``GPIO22``、``GPIO23``、``GPIO25~27``. see more `ESP32引脚功能表. <../../../_images/pinout_wroom_pinout.png>`_ 
 - ``freq`` frequency, 0 < freq <= 78125 Hz
 - ``duty``  duty ratio, 0 ≤ duty ≤ 0x03FF (Decimal：0 ≤ duty ≤ 1023)

.. Important:: PWM can be enabled on all output pins. But it has limitations：All must be the same frequency and only have 8 channels.

Example::

  from machine import PWM, Pin

  pwm = PWM (Pin(2), freq=1000,  duty=1023)    # create an PWM object


Method
------------

.. method:: PWM.init(freq, duty)

Initialize PWM，freq、duty as described above.    


Example::

 pwm.init(1000, 500)


.. method:: PWM.freq([freq_val])

When there are no parameters, the function obtains and returns the PWM frequency. When setting parameters, the function is used to set the PWM frequency, no return value.

 - ``freq_val`` PWM frequency, 0 < freq ≤ 0x0001312D（Decimal：0 < freq ≤ 78125 Hz）

Example::

 print(pwm.freq())
 print(pwm.freq(2000)

.. method:: PWM.duty([duty_val])

Without parameters, the function obtains and returns the PWM duty cycle. When there are parameters, the function is used to set the PWM duty cycle.

- ``duty_val`` duty ratio, 0 ≤ duty ≤ 0x03FF（Decimal：0 ≤ duty_val ≤ 1023）

Example::

 >>> print(pwm.duty())
 50
 >>> print(pwm.duty(500))
 None


.. method:: PWM.deinit( )

Turn off PWM. After using the PWM, you need to log out ``deinit()`` 。

