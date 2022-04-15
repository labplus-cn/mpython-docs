
.. module:: parrot
   :synopsis: mPython Expansion Board driver

:mod:`parrot` --- mPython Expansion Board driver
==================================================


.. figure:: /../images/extboard/extboard_back.png
    :width: 600
    :align: center

PARROT, the mPython Expansion Board is derived from the mPython Board, which is compact and portable. The IO pin expansion board supporting motor drive, voice playback, voice synthesis and other functions can expand 12 IO interfaces and 2 I2C interfaces.
The library provides motor drive, LED drive and other functions for controlling the expansion board.

Motor control I2C communication protocol data format:

======== ======== =========== ===========
Type     Command   motor_no   speed(int)
Motor    0x01      0x01/0x02  -100~100
======== ======== =========== ===========

*When 'speed' is negative, reverse; when positive, forward.*

--------------------------------------------------

.. automodule:: parrot
   :members:
   :member-order: bysource


.. literalinclude:: /../../examples/mpython-shield/motor_simple.py
    :caption: Motor drive example
    :linenos:


.. literalinclude:: /../../examples/mpython-shield/ir_send.py
    :caption: NEC code Infrared code example
    :linenos:

.. literalinclude:: /../../examples/mpython-shield/ir_learn.py
    :caption: NEC code Infrared learning example
    :linenos: