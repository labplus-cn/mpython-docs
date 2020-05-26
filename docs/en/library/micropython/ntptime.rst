
.. _ntptime:
:mod:`ntptime` --- Time synchronization
=========================================

.. module:: ntptime

This module is used for time synchronization, providing accurate time, International Standard Time (UTC). 

.. admonition:: what is NTP

    Network Time Protocol (NTP) is a protocol used to synchronize the time of the computer. It can synchronize the computer to its server or clock source (such as quartz clock, GPS, etc.). It can provide highly precise time calibration.

Method
------


.. method:: settime(timezone=8,server = 'ntp.ntsc.ac.cn')

Synchronize local time

    - ``timezone`` - Time zone time difference, the default is East Eight District, compensation 8 hours
    - ``server``  -  You can specify the time server yourself, server is a string type. The default time server is "ntp.ntsc.ac.cn" .


Example::

    from mpython import *
    import ntptime

    mywifi=wifi()
    mywifi.connectWiFi('tang','tang123456')        

    print("Local time before synchronization：%s" %str(time.localtime()))
    ntptime.settime()
    print("Local time after synchronization：%s" %str(time.localtime()))

运行结果::

    Connecting to network...
    WiFi Connection Successful,Network Config:('172.20.10.4', '255.255.255.240', '172.20.10.1', '172.20.10.1')
    Local time before synchronization：(2000, 1, 1, 0, 40, 8, 5, 1)
    Local time after synchronization：(2018, 12, 27, 12, 10, 7, 3, 361)
    MicroPython v1.0.1-dirty on 2018-11-23; mPython with ESP32
    Type "help()" for more information.
    >>>
