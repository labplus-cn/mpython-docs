Yeelight
=========


`Yeelight <https://www.yeelight.com>`_ has a complete smart home lighting product line, product series radiation home lighting series, desk lighting series, atmosphere lighting series and intelligent control series. It is Yeelight's consistent pursuit to integrate cutting-edge technology and beautiful design.
AI technology, BLE MESH technology, and house full intelligent lighting technology are all widely used in its products. The entire line of WiFi products support intelligent voice control, lighting changes, etc. 

LAN control
-----------

Yeelight supports Google Assistant and Amazon Alexa intelligent voice control. Also supports IFTTT. It can interact better with various network services such as social media and smart hardware. In the future, we will explain the relevant applications of IFTTT。
In addition, Yeelight is also launched for technology enthusiasts. A third-party control protocol can achieve personalized control within the LAN. This protocol is used to control the Yeelight intelligent lighting equipment by the control panel.

Yeelight third-party control protocol：https://www.yeelight.com/download/Yeelight_Inter-Operation_Spec.pdf

.. figure:: /../images/tutorials/yeelight/yeelight_lan.png
  :target: https://www.yeelight.com/zh_CN/developer
  :align: center

  Yeelight LAN control
Get Ready
++++++

- First of all, we must have a Yeelight intelligent lighting device. According to the official statement of Yeelight, all WiFi lighting devices on the market and subsequent WiFi products will support the LAN control protocol. I recommend the Yeelight LED light buld (color version), which is economical and can control the color.

.. figure:: /../images/tutorials/yeelight/yeelight_led.png
  :align: center
  :scale: 30 %

  Yeelight LED light bulb (color version)

- Before using the YeeLight smart light bulb, you must use the YeeLight APP to configure the wifi connection and turn on the "LAN Control" function.

.. figure:: /../images/tutorials/yeelight/yeelight_app.gif
  :align: center
  :width: 400

  Yeelight configuration process
  
- The mPython Board provides the  ``yeelight`` driver library, which can be obtained at  `awesome-mpython/libary/yeelight <https://github.com/labplus-cn/awesome-mpython/tree/master/library/yeelight>`_ . There is a more detailed API description of the  ``yeelight`` module.  ``yeelight.py`` downloaded to the file system of the mPython Board.

- The mPython Board is connected to the same LAN as Yeelight。 



Programming
++++++


Discover light bulb
~~~~~~~~


As the mPython Board and the Yeelight bulb are in the same LAN, we need to know the IP address of the bulb first, we can use the  ``discover_bulbs()`` function::

    from mpython import *                   # import mpython module
    from yeelight import *                  # import yeelight module

    my_wifi = wifi()                        # Connect to the same LAN as YeeLight
    my_wifi.connectWiFi("ssid","password")          


    discover_bulbs()                        # Discover device information of YeeLight in LAN


The Yeelight bulb in the network responds and returns a dictionary containing the bulbs attribute::

    >>> discover_bulbs()
    [{'ip': '192.168.0.8', 'capabilities': {'rgb': '16711680', 'bright': '100', 'support': 'get_prop set_default set_power toggle set_bright start_cf stop_cf set_scene cron_add cron_get cron_del set_ct_abx set_rgb set_hsv set_adjust adjust_bright adjust_ct adjust_color set_music set', 'sat': '100', 'power': 'off', 'id': '0x0000000007e7544d', 'name': '', 'fw_ver': '26', 'color_mode': '2', 'hue': '359', 'ct': '3500', 'model': 'color'}, 'port': '55443'}]


``discover_bulbs()`` function to get the attributes of Yeelight devices in the network. From the above return, the IP address of the bulb is ``192.168.0.8`` .

Switch Control
~~~~~~~~


Knowing the IP address, we construct the ``Bulb``  object and control the light bulb switch::


    bulb=Bulb("192.168.0.8")    # construct object
    bulb.turn_on()              # Turn ON instruction
    bulb.turn_off()             # Turn OFF instruction
 
In addition to ``turn_on()`` 、``turn_off()`` can also use ``toggle()`` to reverse the state.

Brightness Adjustment
~~~~~~~

::

    bulb.set_brightness(100)   

``set_brightness(brightness)`` , ``brightness`` parameter of brightness value, range of 0~100 .


Set the color
~~~~~~~~~

::

    bulb.set_rgb(255,0,0)           # Set bulb color via RGB
    bulb.set_hsv(180,100)           # Set bulb color via HSV
    bulb.set_color_temp(1700)       # Set the bulb color temperature

The ``yeelight`` module provides two functions, ``set_rgb(red, green, blue)`` and  ``set_hsv(hue, saturation)`` . "RGB" and "HSV" 2  color models to set the lamp light color. The RGB color model is more commonly used, I believe everyone is no stranger. Various colors can be obtained by changing the three color channels of red(R), green(G), and blue(B) and superimposing them.
HSV（Hue Saturation Value）：``hue`` measured in degrees, with a value range of 0 to 359, calculated counterclockwise from red, red is 0°, green is 120°, blue is 240°. ``saturation`` means the degree to which the color is close to the spectral color. The higher the saturation of the color. High saturation, deep and gorgeous colors. Range of 0~100.
Value brightness parameter, no support is provided. Just set the ``hue`` 、``saturation`` parameters. When doing some rainbow effects and color transitions, HSV is more natural.

You can also use the  ``set_color_temp(degrees)`` function to set the bulb color temperature,  ``degrees`` color temperature parameter, range 1700~6500。

.. figure:: /../images/tutorials/yeelight/hsv.png
  :align: center
  :scale: 70 %

  Yeelight HSV color model


------------------------

.. figure:: /../images/tutorials/yeelight/yeelight_show.gif
  :align: center
  :scale: 100 %

  mPython Board controled Yeelight

.. Attention:: 

  Yeelight, currently WiFi smart devices support up to 4 simultaneous TCP connections. Connection attempt will be rejected. For each connection, there is a command message quota limit, 
  That is 60 instructions per minute. All LANs also have a total quota limit of 144. 





