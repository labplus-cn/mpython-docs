

``mpython`` --- mpython module (mPython Classroom Kit)
===========================================


``mpython`` module controls the Starter Set thats compatible with the mPython Board, provide control of the built-in resources and its' related functions. The `mpython` module have some differences with that of the mPython Board.
For those identical functions and applications will not mentioned here, instead refers to :ref:`mpython module description <mpython.py>` .

.. Attention:: 

    The location of light sensor, microphone and buzzer in the mPython Starter Set had re-located compared to the mPython Board. Except for microphone, its application  `sound.read()` instead of the earlier  `sound.init()` . Other application method are identical as mPython Board.


Function
------------

Motion
+++++++++++


You can get the current 3-axis acceleration, angular velocity, Euler angle, and quaternion of the MPU6050 space motion sensor. Through these data, you can easily obtain the motion status of it.

.. method:: motion.get_accel()

Return the current three-axis acceleration tuple (x, y, z). Unit g, range -2~+2g。

.. method:: motion.get_gyro()

Returns the current three-axis angular velocity tuple (x, y, z), range ±500°/sec

.. method:: motion.get_euler()

Returns the current Euler angle tuple (Pitch, Roll, Yaw), unit angle

.. method:: motion.get_quat()

Return the current quaternion tuple (w, x, y, z)


The touchpads on mPython Board
++++++++++++++

Same as the mPython board, use  ``read()`` to get the analog value. Since this mPython Starter Set box does not support returning analog values, it can only return as 0 or 1023.！

.. method:: touchPad_[P,Y,T,H,O,N].read()

Returns touch value (0 or 1023)

RGB LED
++++++++++++++

Compared to only 3 on mPython Board, this mPython Starter Set had integrated 5*5 (total 25 pcs) of RGB LEDs. 
It is the same as the control panel in use. For more of ``rgb`` function, refers to mPython Board :ref:`mpython module description <mpython.py>` 。


Microphone
++++++++++++++

.. admonition:: differences

    Due to the addition of audio codec chip in the mPython Starter Set, specifically to deal with audio data. 
.. staticmethod:: sound.init()

Initialize, enable audio decoding

.. staticmethod:: sound.read()

Get the loudness of the sound

.. staticmethod:: sound.deinit()

Turn off audio decoding


