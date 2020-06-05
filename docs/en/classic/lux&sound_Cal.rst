Illuminance/Noise Meter
==========

With the microphone and light sensor on the mPython Board, coding to use it as noise meter or illuminance meter for detecting the environment！

::

    from mpython import *

    u=UI(oled)
    while True:
        oled.fill(0)
        lightValue=numberMap(light.read(),0,4093,0,100)
        soundValue=numberMap(sound.read(),0,4093,0,100)
        u.stripBar(35,8,10,40,soundValue,0)
        u.stripBar(90,8,10,40,lightValue,0)
        oled.DispChar("噪声计",23,50)
        oled.DispChar("照度计",76,50)
        oled.show()

.. image:: /../images/classic/soundlight.jpg
    :scale: 27%
    :align: left
