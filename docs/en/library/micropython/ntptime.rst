
.. _ntptime:
:mod:`ntptime` --- Time synchronization
=========================================

.. module:: ntptime

This module is used for time synchronization, providing accurate time, International Standard Time (UTC). 

.. admonition:: what is NTP

    Network Time Protocol (NTP) is a protocol used to synchronize the time of the computer. It can synchronize the computer to its server or clock source (such as quartz clock, GPS, etc.). It can provide highly precise time calibration.
Note: There's currently no timezone support in MicroPython, and the RTC is set in UTC time.


Method
------

.. method:: settime()

Example::

    from mpython import *
    import ntptime

    mywifi=wifi()
    mywifi.connectWiFi('tang','tang123456')        
    ntptime.host = 'ntp.ntsc.ac.cn'
    timeout = 1
    ntptime.settime()
    print("Success)

运行结果::

    Connecting to network...
    WiFi Connection Successful,Network Config:('172.20.10.4', '255.255.255.240', '172.20.10.1', '172.20.10.1')
    Success

