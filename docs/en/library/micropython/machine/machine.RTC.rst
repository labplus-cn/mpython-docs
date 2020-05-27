.. currentmodule:: machine
.. _machine.RTC:

Class RTC -- Real Time Clock
============================

RTC is an independent clock that track date and time.

Example::

      import machine
      from machine import RTC 
      rtc = machine.RTC()
      rtc.init((2018, 11, 21, 3, 9, 0, 0, 0))
      print(rtc.datetime())


Construct object
------------

.. class:: RTC()

Construct RTC object.

Method
-------

.. method:: RTC.init([datetimetuple])

Initialize RTC. The date and time are 8 tuples of the form：

( year,month,day,weekday,hour,minute,second,microsecond )


.. Attention:: 

    *  ``weekday``: Monday to Sunday correspond to  [0-6] instead of [1-7]
    * The value in the millisecond is actually the value after the decimal point in seconds


.. method:: RTC.datetime([datetimetuple])

When the time tuple is given, the RTC date and time are set, and if the parameter is not given, the current time tuple is returned. The 8-tuple format is the same as above. 


::

    >>> rtc.datetime()
    (2018, 11, 18, 6, 12, 15, 8, 142409)
    >>>
    >>> rtc.datetime((2018, 11, 18, 6, 12, 15, 5, 607409))
    (2018, 11, 18, 6, 12, 15, 8, 142409)


Although RTC can track the time and date for us, the accuracy of RTC has certain defects. Every 7: 45h there will be an error overflow of the second level, so it is recommended to perform time calibration every 7 hours. 

Since the timer cannot perform timing work after a power failure, this will cause your device to enter the initial time before the next start-up January 1, 2000. So if we want to control the time accurately, we need to calibrate the time when we turn on. 
Use :mod:`ntptime` module performs network timing calibration time.
