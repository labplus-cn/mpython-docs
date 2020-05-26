Microphone
=============

The microphone built-in the mPython Board, use it to perceive the sound changes in the surrounding environment. 

Example：Display sound value
::
    from mpython import *
    
    while True:
        oled.fill(0) 
        oled.DispChar('声音：',0,16)
        oled.DispChar("%d" % (sound.read()),40,20)
        oled.show()


First, import the mPython module.
::

  from mpython import *

To use  ``sound.read()`` to obtain the microphone data.
::

    sound.read()



.. Note::

    Microphone used ``read()`` function to read data. The returned value is 12bit ADC sampling data, that is, the maximum value is 4095 decimal.


Learned how to collect sound data of the surrounding environment, combine with other functions to make it more interesting.

