.. currentmodule:: machine
.. _machine.TouchPad:

.. module:: TouchPad

Class TouchPad -- Touch
=============================

ESP32 provides up to 10 capacitive sensing GPIOs, capable of detecting differences in capacitance caused by direct contact or proximity of fingers or other objects.

Create object
------------

.. class:: TouchPad(Pin)

Create a TouchPad object associated with the set pin.

 - ``Pin`` - available pins are：

  ================================== =============== ====================== =================
  Capacitive sensing signal name     ESP32 GPIO      Pin on mPython Board    Remark
  TOUCH0                             GPIO4           P28/Touch_N
  TOUCH1                             GPIO0           P5/Button_A             Pin pull-up cannot be used
  TOUCH2                             GPIO2           P11/Button_B            Pin pull-up cannot be used
  TOUCH3                             GPIO15          P27/Touch_O
  TOUCH4                             GPIO13          P26/Touch_H
  TOUCH5                             GPIO12          P25/Touch_T
  TOUCH6                             GPIO14          P24/Touch_Y
  TOUCH7                             GPIO27          P23/Touch_P
  TOUCH8                             GPIO33          P0
  TOUCH9                             GPIO32          P1
  ================================== =============== ====================== =================


 .. Note:: 

  ESP32 has 10 touch sensors. The control panel has 8 touch functions, 6 of which lead to the touch panel on the front of the control panel. For details, see :ref:`掌控板引脚定义<mPythonPindesc>` 。
 

Example::

    from machine import TouchPad, Pin

    tp = TouchPad(Pin(14))



Method
---------

.. method:: TouchPad.read()

Read TouchPad level。

``TouchPad.read`` Returns the value relative to the capacitive variable. When touched, it is a small number(usually within *10* ),when there is no touch, it is a large number (greater than *1000*) is usual. However, these values are “relative” and can vary depending on the circuit board and surroundings, so some calibration may be required.
Note that if other non-touch pins are called, it will cause ``ValueError`` .

.. method:: TouchPad.config(value)

Set the touchpad threshold

  - ``value`` 整数
