.. _servo_api:

.. module:: servo
   :synopsis: Servo driver function


:mod:`servo` --- Servo driver function
==========

Servo class
-------

.. class:: Servo(pin, min_us=750, max_us=2250, actuation_range=180)

Construct Servo object, use SG90 servo by default. Different servos have different pulse width parameters and angle ranges, which can be set according to the servo model.

.. Hint:: 

    Servo control pin must be a pin that supports PWM (analog output). mPython Board supports PWM pins, for details, see :ref:`Pin description of the mPython Board interface <mPythonPindesc>` 。

.. Attention:: 

    * Set  ``actuation_range`` to apply the actual motion values observed for ``min_us`` and ``max_us`` .
    * To extend the pulse width above and below these limits. The servo may stop, buzz, and absorb additional current when stopped. Test carefully to find the safe minimum and maximum.
    * Because the servo PWM cycle is 20ms, the response time is 20ms. When programming, pay attention to the interval between writing the servo angle twice should be at least greater than 20ms。

- ``pin`` - Servo PWM control signal pin
- ``min_us`` - The minimum width of the pulse width of the servo PWM signal, in microseconds. Default min_us=750
- ``max_us`` - The maximum pulse width of the servo PWM signal, in microseconds. Default max_us=2250
- ``actuation_range`` - Maximum turning angle of servo


.. method:: Servo.write_us(width)

Send PWM signal with set pulse width。

    - ``width`` -Pulse width in microseconds.

.. method:: Servo.write_angle(angle)

Write servo angle

    - ``angle`` - servo angle.


::

    from mpython import *
    from servo import Servo                 #import servo module

    s=Servo(0)

    while True:
            for i in range(0,180,1):
                    s.write_angle(i)
                    sleep_ms(50)
            for i in range(180,0,-1):
                    s.write_angle(i)
                    sleep_ms(50)
