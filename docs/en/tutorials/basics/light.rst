Light Sensor
=============

The built-in light sensor on the mPython Board, 掌控板板载光线传感器，use it to sense light changes in the surrounding environment.

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

    光线传感器使用 ``read()`` 函数来读取数据。返回的值为12bit的ADC采样数据，即最大值为十进制4095。


学会了如何收集周边环境的光线数据，我们可以结合其他功能做更多有趣的场景。

