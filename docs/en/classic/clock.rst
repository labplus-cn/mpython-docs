Digital analog clock
==========

Integrate the OLED display and the WiFi function to construct a digital analog clock, connect to the network via WiFi to obtain the international standard time, and display it on the OLED display.

Digital clock
+++++++

:: 

    import ntptime,network     # Import international standard time, network module
    from mpython import*
    from machine import Timer  # Import timing module

    mywifi=wifi()
    mywifi.connectWiFi("ssid","password")  # WiFi setting

    try:
        ntptime.settime()
    except OSError :
        oled.DispChar("ntp link timeout, please restart!",0,20)    
        oled.show()
    else:

        def get_time(_):   #Define clock refresh time
            t = time.localtime()
            print("%d年%d月%d日 %d:%d:%d"%(t[0],t[1],t[2],t[3],t[4],t[5]))  
            oled.DispChar("{}年{}月{}日" .format(t[0],t[1],t[2]),20,8)
            oled.DispChar("{}:{}:{}" .format(t[3],t[4],t[5]),38,25)
            oled.show()
            oled.fill(0)  

        tim1 = Timer(1) 

        tim1.init(period=1000, mode=Timer.PERIODIC, callback=get_time)  

The digital clock is a timepiece that displays digitally instead of the analog dial. It displays the time at this time with numbers. The digital clock in the case can display hours, minutes, and seconds at the same time.

::

    mywifi=wifi()
    mywifi.connectWiFi("ssid","password")

To display the time, first connect to the network, then set the WiFi name and its password。

.. admonition:: prompt

 For WiFi connection，see :ref:`wifi class<mpython.wifi>` learn the use.
 
::

    try:
        ntptime.settime()   #Get International Standard Time
    except OSError :
        oled.DispChar("ntp link timeout, please restart!",0,20)    
        oled.show()

For better understanding of the situation of network connection, set to catch exceptions and display some prompts. First obtain the international standard time, when an exception is obtained, a prompt is displayed.

::

    tim1 = Timer(1)    #Create a Timer
    tim1.init(period=1000, mode=Timer.PERIODIC, callback=get_time)  

Create and initialize a timer, initialize the time to a timing mode with a cycle of 1000 milliseconds, get the time and return the current count value of the timer（for time parameter, see :mod:`machine.Timer` module）.

::

    time.localtime()

Obtain the local time and display the time as 8 tuples (including year, month, day, hour, minute, and second) (more details, see :mod:`time` module).

:: 

    oled.DispChar("{}年{}月{}日" .format(t[0],t[1],t[2]),20,8)
    oled.DispChar("{}:{}:{}" .format(t[3],t[4],t[5]),38,25)
    oled.show()
    oled.fill(0)   #clear screen

First obtain the time, then displayed it on the OLED display

.. admonition:: annotation

    Display the year, month and day at the position of coordinates (20,8)：t[0] corresponds to the year, t[1] corresponds to the month, and t[2] corresponds to the day; hour, minute, and second are displayed at the coordinates (38, 25): when t[3] corresponds to hour, t[4] corresponds to the minute, t[5] corresponds to seconds. 


.. image:: /../images/classic/digital.jpg
    :scale: 50 %
    :align: center

Analog clock
+++++++

::
    
    import ntptime,network   
    from mpython import*
    from machine import Timer

    mywifi=wifi()
    mywifi.connectWiFi("ssid","password")

    try:
        ntptime.settime()
    except OSError :
        oled.DispChar("ntp link timeout, please restart!",0,20)
        oled.show()
    else:
        clock=Clock(oled,64,32,30)      

        def Refresh(_):
            clock.settime()
            clock.drawClock() 
            oled.show()
            clock.clear()
        
        tim1 = Timer(1)

        tim1.init(period=1000, mode=Timer.PERIODIC, callback=Refresh) 

Construct Clock object：
::

    clock=UI.Clock(64,32,30) 
    
UI.Clock(x, y, radius)is used to construct clock objects，x、y are the starting point coordinates on the OLED display, radius is the radius of the clock drawn.

Get local time and set analog clock time：
::
    clock.settime()

Draw the clock：
::
    clock.drawClock()

Clear the clock：
::
    clock.clear()   

Clear the clock, that is, clear the time displayed on the OLED display to display the new time acquired, otherwise it will cause each time value to overlap and display on the OLED.

.. image:: /../images/classic/analog.jpg
    :scale: 50 %
    :align: center
