:mod:`time` -- Time correlation function
======================================

.. module:: time
   :synopsis: time correlation function

This module implements the corresponding :term:`CPython` A subset of modules, as described below. Refers to CPython document for details: `time <https://docs.python.org/3.5/library/time.html#module-time>`_

The ``time`` module provides functions for obtaining the current time and date, measuring the time interval and delay.

**Time Epoch**: Unix port usage 1970-01-01 00:00-00:00 UTC's POSIX system time standard. However, the embedded port uses the time of ``2000-01-01 00:00:00 UTC``. 


**Maintain actual calendar date / time**: This requires real-time communication（RTC）。In systems with underlying OS, RTC may be implicit. Setting and maintaining the actual calendar time should be the function of OS / RTOS. 
And it's done outside of MicroPython, only use OS API to query date / time. In the baremetal port, System time depends on ``machine.RTC()`` object. 
The current calendar time may use ``machine.RTC().datetime(tuple)`` Function, and maintained in the following ways:
* By a back-up battery (may be an additional optional component for a specific board). 
* Use network time protocol (need to be installed through a port / user).
* Set manually each time the power is turned on (many boards maintain RTC time by hard reset, although some may need to be reset in this case).

If the actual calendar time is not maintained by the system / MicroPython RTC, functions that need to refer to the current absolute time may not match expectations. 

Function
---------

.. function:: localtime([secs])

   Converts a time in seconds to an 8-tuple containing:（Year、Month、Day、Hour、Minutes、Seconds、Day of the Week、Day of the Year）. If seconds not given or none, then RTC time is used.

   * Year（example: 2024）
   * Month as 1-12
   * Day as 1-31
   * Hour as 0-23
   * Minutes as 0-59
   * Secocnds as 0-59
   * Day of the Week as 0-6 （Sunday to Saturday）
   * Day of the Year as 1-366

    >>> time.localtime()
    (2019, 5, 27, 16, 48, 45, 0, 147)
    >>> time.localtime(611220968)
    (2019, 5, 15, 7, 36, 8, 2, 135)


.. function:: mktime()

    This is the inverse function of ``localtime()`` , Its parameter is an 8 tuple representing the local time. Returns an integer representing seconds since January 1, 2000.
    
    >>> data_tuple = (2019, 1, 1, 0, 0, 0, 0, 0)
    >>> time.mktime(data_tuple)
    599616000

.. function:: sleep(seconds)

   Time to sleep for a given number of seconds. Seconds can be a float number representing the sleep time. Note: floating point parameters may not be accepted by other ports. To meet compatibility, use the functions ``sleep_ms()`` and ``sleep_us()`` .。 

.. function:: sleep_ms(ms)

   Delay given number of milliseconds, expecting positive or 0.

.. function:: sleep_us(us)

   Delay the given number of microseconds, expecting a positive number or 0.
   
.. function:: ticks_ms()

    Returns an incremental millisecond counter for any reference point that ends after some value (unspecified). 。This value should be considered opaque and only applies to ticks_diff(). 

    The wrap value is not shown explicitly, but for discussion purposes，we call it  *TICKS_MAX* .  The period of this value is  *TICKS_PERIOD = TICKS_MAX + 1* 。
     *TICKS_PERIOD* must be a power of 2, but it also varies depending on the port.Same cycle value for `ticks_ms()` 、 `ticks_us()` 、
      `ticks_cpu()` function (for simplicity). As a result, these functions return a value between *[0 .. TICKS_MAX]* , include value of *TICKS_PERIOD* .
    Note: use only non negative values. In most cases, should treat the values returned by these functions as transparent. The only operations available for it are the following `ticks_diff()` and  `ticks_add()` function.

    Note: performing a standard mathematical operation(+, -) or relational operator (<, <=, >, >=) directly on these values will result in invalid results.
    Perform a number operation and pass the result as a parameter to ``ticks_diff()`` or ``ticks_add()`` will result in invalid result of the latter function.

.. function:: ticks_us()

   As above ``ticks_ms`` , but in microseconds.

.. function:: ticks_cpu()

   Same as  ``ticks_ms`` and ``ticks_us`` , But have higher resolution (usually CPU clock).
   
   This is the usual CPU clock, which is why the function is so named. But it is not necessary to be a CPU clock, other available timing sources in the system. 
   (For example, a high-resolution timer) can also be used as an alternative. The exact timing unit (resolution) of this function is not specified in the module layer ``time`` .
   But the documentation for a specific port may provide more specific information. This function is designed for very fine benchmarks or very compact real-time loops. Avoid using in portable program coding. 

   Availability: not every port can implement this function. 


.. function:: ticks_add(ticks, delta)

   Offsets the ticks value with a given number, which can be positive or negative. Given a *ticks* value, this function allows to evaluate the ticks value  *delta*  ticks，
  And follow the modular arithmetic definition of the ticks value（see above `ticks_ms()` ）. The ticks parameter must be a call to the `ticks_ms()` 、 `ticks_us()` 、 `ticks_cpu()` function.
   Direct result of（Or previously called `ticks_add()` ）. However, delta can be expressed as an arbitrary integer or a number. `ticks_add()` Useful for calculating event / task deadlines.
   （Note：To use  `ticks_diff()` function to process the deadline. ） 

   Examples::

        # Find out what ticks value there was 100ms ago.
        print(ticks_add(time.ticks_ms(), -100))

        # Calculate deadline for operation and test for it.
        deadline = ticks_add(time.ticks_ms(), 200)
        while ticks_diff(deadline, time.ticks_ms()) > 0:
            do_a_little_of_something()

        # Find out TICKS_MAX used by this port
        print(ticks_add(0, -1))


.. function:: ticks_diff(ticks1, ticks2)

   Measure the period between successive calls to ticks_ms()、ticks_us()、ticks_cpu().
   The values returned by these functions may stop at any time, Therefore, it is not supported to subtract these values directly. Instead, use ticks_diff()。 
   The OLD value should actually override the new value in a timely manner, otherwise the result will not be defined. This function should not be used to measure any long period of time（because the ticks_*() function includes and usually has short periods).

  Report errors
   The expected usage mode is to use timeout to implement event polling:


   The order of the parameters is the same as the subtraction operator,  ``ticks_diff(ticks1, ticks2)`` and ``ticks1 - ticks2`` have the same meaning.
   However, the function may revolve around the value returned by `ticks_ms()` ，so using subtraction here will produce wrong results. So `ticks_diff()` emerge,
   It can be modularized even in the case of surround values（or rather, ring）The algorithm generates the correct values (as long as the distance between them is not too far, see below).
   The function returns a value between[ *-TICKS_PERIOD/2 ..TICKS_PERIOD/2-1* ] the signed integer value of (this is a typical range definition for two complementary binary integers). 
   If the result is negative, it means that *ticks1* occurs before *ticks2* . Otherwise, it means that *ticks1* occurs after *ticks2* .
   This is only true if the distance from each other does not exceed *TICKS_PERIOD/2-1*  ticks. If not, an error result is returned  *TICKS_PERIOD/2* ，
   This function returns *TICKS_PERIOD/2* , that is, the resulting value will wrap around a negative range of possible values.
   Common principles of the above limitations：Suppose you are locked in a room with only a standard 12 level clock to record the time progress. If you check your watch now,
   And don't look at the time for the next 13 hours (for example, you may have slept for a long time), Then when you look at your watch again, it's only an hour for you.
   To avoid this error, check the time regularly. Your application should do the same. The metaphor of “sleep too long” directly mirrors the behavior of an application：
   Do not let your application run a single program too long. Run the task step by step and time as the step progresses.

   `ticks_diff()` The design is applicable to various modes of use, including:

   * Use timeout polling. In this case, the sequence of events is known, You just need to deal with `ticks_diff()` positive result::

        # Wait for GPIO pin to be asserted, but at most 500us 
        start = time.ticks_us()
        while pin.value() == 0:
            if time.ticks_diff(time.ticks_us(), start) > 500:
                raise TimeoutError

   * Schedule events. In this case, if an event is overdue, the result of `ticks_diff()` may be negative::

        # This code snippet is not optimized 
        now = time.ticks_ms()
        scheduled_time = task.scheduled_time()
        if ticks_diff(now, scheduled_time) > 0:
            print("Too early, let's nap")
            sleep_ms(ticks_diff(now, scheduled_time))
            task.run()
        elif ticks_diff(now, scheduled_time) == 0:
            print("Right at time!")
            task.run()
        elif ticks_diff(now, scheduled_time) < 0:
            print("Oops, running late, tell task to run faster!")
            task.run(run_faster=true)

   Note：Do not pass the  `time()` value to  `ticks_diff()` , to use normal mathematical operation now. But please note that `time()` may (and will) overflow. This is called https://en.wikipedia.org/wiki/Year_2038_problem .


.. function:: time()

   Assuming that the underlying RTC is set and maintained as described above, an integer number of seconds is
   (for the embedded circuit board of RTC without battery support, usually after the power is started or reset).  If you want to develop portable MicroPython applications,
   You should not rely on this function to provide results higher than the second precision. If you need more precision, use the ``ticks_ms()`` and ``ticks_us()`` function.
     If you need calendar time, the ``localtime()`` without parameters is a good choice.

   .. admonition:: Difference to CPython
      :class: attention

      In CPython, this function returns the number of seconds in floating-point form starting from UNIX time, 1970-01-01 00:00 UTC,
      Its accuracy is usually microseconds. When MicroPython is used, only UNIX ports use the same time. If floating-point precision allows
      Then it returns the sub second precision. Embedded hardware usually does not have floating-point precision, which can represent a long time range and sub second second precision,
      So they use integer values with a second precision. Some embedded hardware also lacks battery powered RTC,
      Therefore, returns the number of seconds since the last power on or other relevant specified hardware point (example: reset).
