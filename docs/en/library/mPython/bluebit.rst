
.. module:: bluebit
   :synopsis: blue:bit driver

:mod:`bluebit` --- blue:bit driver
==================================================


`blue:bit` The module provides the mPython Board library of bluebit kit.


.. contents::

.. image:: http://wiki.labplus.cn/images/0/07/Bluebit套件1.png


NTC Temperature module
-------------


.. autoclass:: bluebit.Thermistor
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource

.. autoclass:: bluebit.NTC
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource


LM35 Temperature module
-------------

.. autoclass:: bluebit.LM35
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource


Joy Button module
-------------

.. autoclass:: bluebit.joyButton
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource

Temperature-Humidity module
-------------

.. autoclass:: bluebit.SHT20
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource


Color module
-------------

.. autoclass:: bluebit.Color
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource

Light module
-------------

.. autoclass:: bluebit.AmbientLight
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource


Ultrasonic module
-------------

.. autoclass:: bluebit.Ultrasonic
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource

4*7 SEG Display module
-------------

.. autoclass:: bluebit.SEGdisplay
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource

8x8 Matrix module
-------------

.. py:class:: Matrix(i2c=i2c)

8x8 matrix module control class

- ``i2c`` : I2C instance object, default i2c=i2c. 

.. py:method:: Matrix.blink_rate(rate=None)

Set pixel flicker rate

- ``rate`` : Flashing interval time, in seconds. Default is None, always on.


.. py:method:: Matrix.brightness(brightness)

Set pixel brightness

- ``brightness`` : Brightness level, range 0~15.


.. py:method:: Matrix.fill(color)

Fill all

-  ``color`` : 1 ON ; 0 OFF

.. py:method:: Matrix.bitmap(bitmap)

Display bitmap

-  ``bitmap`` : 8x8 matrix data


.. py:method:: Matrix.show()

Display show


In addition to the above function methods, it also inherits the  ``FrameBuffer`` class, and other methods, such as displaying characters and drawing functions. For details, please refer to the  `FrameBuffer <https://mpython.readthedocs.io/zh/master/library/micropython/framebuf.html>`_ class of the micropython framebuf module.

LCD1602 module
-------------

.. autoclass:: bluebit.LCD1602
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource

MIDI module
-------------

.. autoclass:: bluebit.MIDI
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource



MP3 module
-------------

.. autoclass:: bluebit.MP3
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource


OLED module
-------------

.. autoclass:: bluebit.OLEDBit
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource


IR Receive module
-------------

.. autoclass:: bluebit.IRRecv
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource

IR Emission module
-------------

.. autoclass:: bluebit.IRTrans
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource


Science Exploration 
-------------

Applicable modules are Voltage Meter, Current Meter, Magnetic Sensor, TDS Meter, PH Sensor, Photogate Timer, Pressure Sensor, Force Sensor.

.. autoclass:: bluebit.DelveBit
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource


Motor Encoder module
-------------

.. autoclass:: bluebit.EncoderMotor
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource




RFID module
-------------

.. autoclass:: bluebit.Scan_Rfid
    :members:
    :undoc-members: True
    :exclude-members: 
    :member-order: bysource


.. autoclass:: bluebit.Rfid
    :members:
    :undoc-members: True
    :exclude-members: 
    :special-members: '__init__' 
    :member-order: bysource
