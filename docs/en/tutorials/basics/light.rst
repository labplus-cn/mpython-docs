Light Sensor
=============

The built-in light sensor on the mPython Board, use it to sense light changes in the surrounding environment.

Example：Light control lamp::

    from mpython import *

    while True:
        oled.fill(0)                                   #Clear Screen
        oled.DispChar("亮度:",30,16)                    #Display brightness
        oled.DispChar("%d" % (light.read()), 60, 16)    #Display the built-in Light Sensor
        oled.show()                                     #Refresh
        sleep_ms(100)                                   #Delay 100ms

        if light.read() < 200 :                    # When the light brightness is less than 200, turn ON the light
        rgb.fill((50,50,50))
            rgb.write()
        else:                                      # else, OFF the light
            rgb.fill((0,0,0))
            rgb.write()


Use ``light`` object to obtain the light sensor data::

    light.read()


.. Note::

    The light sensor uses the  ``read()`` function to read data. The returned value is 12bit ADC sampling data, that is, the maximum value is decimal 4095。


Learned how to collect light data of the surrounding environment, we can combine other functions to make more interesting scenes.

