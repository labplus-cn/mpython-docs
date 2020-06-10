
.. _mpython.py:

.. module:: mpython
   :synopsis: mPython Board related built-in functions

:mod:`mpython` --- mPython Board related built-in functions
==========================

``mpython`` a proprietary module packed with built-in resources and functions. For details, refers to :ref:`mpython.py源码 <mpython_code>` 。

Delay
-------

.. method:: sleep(s)

Second time delay

    - ``s`` - unit in second.

.. method:: sleep_ms(ms)

Millisecond time delay

    - ``ms`` -unit in millisecond.

.. method:: sleep_us(us)

Time delay

    - ``us`` -unit in microsecond.


Mapping
-------

.. method:: numberMap(inputNum,bMin,bMax,cMin,cMax)

Mapping function，parameter：

- ``inputNum`` For variables require mapping

- ``bMin`` The minimum value require for mapping

- ``bMax`` The maximum value require for mapping

- ``cMin`` Minimum value

- ``cMax`` Maximum value



Built-in sensors
-------

Sound, Light 
+++++++++

.. method:: light.read()

Read Light Sensor value, range 0~4095。


.. method:: sound.read()

Read Sound Sensor (microphone） value， range 0~4095。


Accelerometer 
+++++++++

Through the accelerometer object, you can get the 3-axis accelerometer value in g. range:±2g/±4g/±8g/±16g, default at ±2g。

.. method:: accelerometer.get_x()

Get the acceleration measurement value on the x-axis, positive or negative integer, depending on the direction.

.. method:: accelerometer.get_y()

Get acceleration measurement value on y-axis, positive integer or negative integer, depending on direction.

.. method:: accelerometer.get_z()

Get the acceleration measurement value on the z axis, positive integer or negative integer, depending on the direction.

.. method:: accelerometer.set_range(range)

Set the acceleration range if not modified, default range is ±2g.

The acceleration range constant value is follows:

    ========================== ========= =================
        Constant                 Value      Definition
        RANGE_2G                   0        range ±2g
        RANGE_4G                   1        range ±4g
        RANGE_8G                   2        range ±8g
        RANGE_16G                  3        range ±16g
    ========================== ========= =================


.. method:: accelerometer.set_resolustion(resolution)

Set acceleration resolution, default is 10bit resolution。

The resolution constant value is follows:

    ========================== ========= =================
        Constant                  Value    Definition
        RES_14_BIT                  0      14 bit resolution 
        RES_12_BIT                  1      12 bit resolution 
        RES_10_BIT                  2      10 bit resolution 
    ========================== ========= =================

.. method:: accelerometer.set_offset(x=None, y=None, z=None)

This function is used to calibrate the acceleration value deviation of the three axes (x, y, z) of the accelerometer. Under normal circumstances, no calibration is required, only amend when there is large acceleration deviation.
Note that the calibration data will not be saved after power off. ``x``, ``y``, ``z`` is the adjustment deviation value, the correctable range is ±1g.


Magnetometer
-----------
MMC5983MA magnetometer function interface, which can obtain 3-axis geomagnetic induction intensity, geomagnetic field intensity, and electronic compass angle.

.. Attention:: The MMC5983MA magnetometer is only available for mPython Board version v2.0 and above！

.. method:: magnetic.get_x()

Obtain the x-axis magnetic induction value, positive or negative integer, range ±8191, unit mG (milliGauss).

.. method:: magnetic.get_y()

Get the magnetic induction value of the y-axis, positive integer or negative integer, range ±8191, unit mG (milliGauss).

.. method:: magnetic.get_z()

Obtain the magnetic induction value of the z axis, positive integer or negative integer, range ±8191, unit mG (milli Gauss).

.. method:: magnetic.get_field_strength()

Returns the calculated magnetic induction value, which is the sum of the three-axis magnetic force. Calculation formula, square root of x^2+y^2+z^2.

.. method:: magnetic.peeling()

Magnetic peeling. Similar to the peeling function of electronic scales, after  ``peeling()`` , the next time ``get_field_strength()`` returns the value calculated after subtracting the current magnetic value. 

.. method:: magnetic.clear_peeling()

The magnetic peeling function is cancelled. After using ``peeling()`` , you can use this function to resume normal geomagnetic measurement.

.. method:: magnetic.get_heading()

Obtain the angle of the electronic compass, that is, the angle between the re-orientation and the magnetic north pole, directly above the mPython Board, that is, the USB position is regarded as true north. Angle in degree, range 0~360。

.. Attention:: Because there is no z-axis tilt compensation in the angle calculation, when using ``get_heading()`` to read the compass angle, the control board should be kept horizontally placed！

.. Attention:: For accurate compass angle, please make sure there is no strong magnetic field interference or  ``calibrate()`` calibration before use.

.. method:: magnetic.calibrate()

Electronic compass calibration. When there is strong magnetic interference around the control panel, you can use this function to clear the strong magnetic component to calculate the accurate north declination of the geomagnetic field. Note that the calibration offset value is not saved after power off。

Calibration method, follow the instructions on the display of the mPython Board:

    1. The mPython Board is placed horizontally and rotates several times on the horizontal plane, the process is about 15 seconds.
    2. The mPython Board is placed vertically and rotates several times along the axis perpendicular to the ground, the process is about 15 seconds.


.. literalinclude:: /../../examples/magnetic/compass.py
    :caption: Magnetometer application--compass
    :linenos:


BME280
-------

BME280 is an environmental sensor with integrated temperature, humidity, and air pressure. With high precision, multi-function, compact and other unique characteristics。

* Temperature detection range：-40℃~+85℃，resolution 0.1℃，tolerance ±0.5℃
* Humidity detection range：0~100%RH，resolution 0.1%RH，tolerance ±2%RH
* Pressure detection range：300~1100hPa
* Humidity measurement response time：1s

.. Attention:: 

    The mPython Board scans the I2C bus for 0x77 (119) I2C devices to determine whether to construct the bme280 object!

.. method:: bme280.temperature()

Returns the temperature value in degrees Celsius。

.. method:: bme280.pressure()

Returns the atmospheric pressure value in Pa.

.. method:: bme280.humidity()

Return to ambient humidity, unit in %。


Buzzer
-------

mPython Board buzzer driven by ``music`` module. For details, see :mod:`music` module.


button_[A,B] object
------
The Button A and B on the mPython Board. button_a/button_b is a derived class of  ``machine.Pin`` and inherits Pin method. For application method, see :ref:`machine.Pin<machine.Pin>`  .



.. method:: button_[a,b].value()

Get button_[a,b] pin status. PIN I/O, value==1 when the button is not pressed, value==0 when pressed.

::

    >>> button_a.value()
    >>> 1
    >>> button_a.value()
    >>> 0

.. _button.irq:

.. method:: button_[a,b].irq(handler=None, trigger=(Pin.IRQ_FALLING | Pin.IRQ_RISING), priority=1, wake=None)

Configure the interrupt handler to be called when the trigger source of the pin is active。

Parameter:

     - ``handler`` is an optional function that is called when the interrupt is triggered.

     - ``trigger`` configures events that can trigger an interrupt. Possible values are：

       - ``Pin.IRQ_FALLING`` Falling edge interrupt
       - ``Pin.IRQ_RISING`` Rising edge interrupt
       - ``Pin.IRQ_LOW_LEVEL`` Low level interrupt
       - ``Pin.IRQ_HIGH_LEVEL`` High level interrupt

       These values can be used to perform ``OR`` operate together to trigger multiple events.

     - ``priority`` sets the priority of the interrupt. The values it can take are port specific, but higher values always represent higher priority. 

     - ``wake`` Select this interrupt to wake up the power mode of the system. It can be  ``machine.IDLE`` ， ``machine.SLEEP`` or ``machine.DEEPSLEEP`` 。
     These values can also be used for ``OR`` operations, which can interrupt the pin in various power consumption modes.

This method returns a callback object.

::

    >>> from mpython import *
    >>> button_a.irq(trigger=Pin.IRQ_FALLING, handler=lambda p:print("button-a press！")) 


touchPad_[ ] object
------
There are 6 touchpad on the mPython Board touchPad_P/Y/T/H/O/N。

.. method:: touchPad_[P,Y,T,H,O,N].read()

Return touch value

::

    >>> touchPad_P.read()
    >>> 523

rgb object
-------
mPython Board built-in with three WS2812 LED. The RGB object is a derivative of neopixel, methods of inheriting neopixel. For more application, see :ref:`neopixel<neopixel>` . 

.. method:: rgb.write()

Write data to RGB LEDs。 

.. Hint::

    Write RGB color values by assigning values to rgb[n] list. Such as, rgb[0]=(50,0,0)

::

    from mpython import *

    rgb[0] = (255, 0, 0)  # set to RED for full brightness
    rgb[1] = (0, 128, 0)  # set to GREEN for half brightness
    rgb[2] = (0, 0, 64)   # set to BLUE for a quarter of brightness

    rgb.write()

.. method:: rgb.fill(rgb_buf)

Fill all LED pixels.

.. method:: rgb.brightness(brightness)

Brightness adjustment, range 0~1.0


.. _oled:

OLED object
-------
The OLED object is a derivative of framebuf, inheriting the method of framebuf. For more application, see :mod:`framebuf<framebuf>` . 

.. method:: oled.poweron()

Power ON the OLED panel.

.. method:: oled.poweroff()

Power OFF the OLED panel.

.. method:: oled.contrast(brightness)

Set the display brightness。

    - ``brightness`` brightness, range 0~255


.. method:: oled.invert(n)

Flip the pixels. When n=1, the unfilled pixels are lit-up, and the filled pixels are off. Otherwise When n=0. The default start is to fill the pixels and light up.

.. method:: oled.DispChar(s, x, y,mode=TextMode.normal)

OLED panel text display. Apply  `Google Noto Sans CJK <http://www.google.cn/get/noto/help/cjk/>`_ open-source sans serif font. Font height 16 pixels, supports English, Simplified Chinese, Traditional Chinese, Japanese and Korean languages.
When the display string exceeds the width of the display, it will wrap automatically.

Returns the binary (the total pixel width of the character, the x, y coordinates of the subsequent display).

    - ``s`` -Text to display.
    - ``x`` 、``y`` - The upper left corner is the text start point coordinate.
    - ``mode`` - Set the text mode, the default is TextMode.normal

        - ``TextMode.normal`` - equals to 1 . In normal mode, the text is displayed in white and the background is black.
        - ``TextMode.rev`` - equals to 2 . Reverse mode, the text is displayed in black, and the background is white.
        - ``TextMode.trans`` - equals to 3 . Transparent mode, transparent text means that the text is written on top of what is already visible in the display. The difference is that the content on the previous screen can still be seen, while for normal, the background will be replaced by the currently selected background color.
        - ``TextMode.xor`` - equals to 4 . XOR mode, if the background is black, the effect is the same as the default mode (normal mode). If the background is white, the text is reversed.

.. method:: oled.show()

Send frame buffer to OLED display.

.. literalinclude:: /../../examples/display/helloworld.py
    :caption: hello world
    :linenos:

.. literalinclude:: /../../examples/display/oled_effect of typing.py
    :caption: Typing effect
    :linenos:


.. method:: oled.DispChar_font(font, s, x, y, invert=False)

Custom font display. Users can use Python script for  `otf` 、 `ttf` standard font files on the PC according to their own need `font_to_py.py <https://github.com/peterhinch/micropython-font-to-py/blob/master/font_to_py.py>`_ turn to output Python source code with font bitmap, and call to use.
Returns the binary (the total pixel width of the character, followed by the displayed x, y coordinates).

    - ``font`` - Font object. `font_to_py.py` put the python source code obtained from script conversion into the file system. Note that font file must be imported before using the function.   
    - ``s`` - Displayed string
    - ``x`` 、 ``y`` - The upper left corner is the text start point coordinate.
    - ``invert`` - Display pixel flip。




.. literalinclude:: /../../examples/display/custom_font/main.py
    :caption: Custom font display
    :linenos:

* :download:`In the above custom font examples imfang16、freescpt18、stxingkai20<https://github.com/labplus-cn/mpython-docs/tree/master/examples/display/custom_font>`

.. figure:: /../images/tutorials/helloworld_customfont.jpg
    :width: 400px
    :align: center

.. admonition:: `font_to_py.py` script instructions

    - This script requires Python 3.2 or higher. Depends on  `freetype` python package. Installation method, `pip3 install freetype-py`  
    - By default, only the ASCII character set（ `chr(32)` to `chr(126)` characters) is converted. Through the command line parameter `-c`, modify this range as needed to specify any Unicode character set, you can define non-English and non-contiguous character sets.
    - `oled.DispChar_font()` function only supports hmap horizontally mapped fonts, so when converting, you need to use the command line parameter `-x` to permanently convert to horizontal mapping.
    - Firmware parameters. Font file path, converted font height, output file path. Such as: font_to_py.py FreeSans.ttf 20 myfont.py

Use font_to_py.py script to convert fonts on PC::

    # Convert height to 16 pixels contains only ASCII character set
    font_to_py.py -x FreeSans.ttf 16 myfont.py

    # The conversion height is 16 pixels to specify the Unicode character set, and the character set specified for you after the -c parameter
    font_to_py.py -x simfang.ttf 16 simfang.py -c  ¬!"#£$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~°Ωαβγδθλμπωϕ£


The function of this function is realized, the reference comes from  `peterhinch/micropython-font-to <https://github.com/peterhinch/micropython-font-to-py>`_ open source project, more details about `font_to_py.py` Instructions, you can go to this project for more information.


.. method:: oled.fill(c)

        Fill the entire frame buffer with the specified color. When ``c`` is 1, the pixel is on; when ``c`` is 0, the pixel is off.

.. method:: oled.circle(x, y, radius , c)

Draw a circle

    - ``x`` 、``y`` - the upper left corner as the starting point coordinate.
    - ``radius`` - Radius of circle
    - ``c`` - when it is 1, the pixel is on; when ``c`` is 0, the pixel is off.

.. method:: oled.fill_circle(x, y, radius , c)

Draw a solid circle

    - ``x`` 、``y`` - the upper left corner as the starting point coordinate.
    - ``radius`` - Radius of circle
    - ``c`` - when it is 1, the pixel is on; when ``c`` is 0, the pixel is off.

.. method:: oled.triangle(x0, y0, x1, y1, x2, y2, c)

Draw a triangle

    - ``x0`` 、``y0`` - Vertex coordinates on the triangle.
    - ``x1`` 、``y1`` - Coordinates of left vertex of triangle.
    - ``x2`` 、``y2`` - Coordinates of the left vertex of the triangle.
    - ``c`` - when it is 1, the pixel is on; when ``c`` is 0, the pixel is off. 

.. method:: oled.fill_triangle(x0, y0, x1, y1, x2, y2, c)

Draw a solid triangle

    - ``x0`` 、``y0`` - Vertex coordinates on the triangle.
    - ``x1`` 、``y1`` - Coordinates of left vertex of triangle.
    - ``x2`` 、``y2`` - Coordinates of left vertex of triangle.
    - ``c`` -when it is 1, the pixel is on; when ``c`` is 0, the pixel is off.


.. method:: oled.bitmap(x, y, bitmap, w, h,c)

Draw a bitmap pattern

    - ``x`` 、``y`` - the upper left corner as the starting point coordinate
    - ``bitmap`` - btyearray byte array of pattern bitmap
    - ``w`` - Pattern width
    - ``h`` - Pattern height
    - ``c`` - When 爱他1, the pixel lights up;


.. method:: oled.RoundRect( x, y, w, h, r, c)

Draw arc rectangle

    - ``x`` 、``y`` - The upper left corner is used as the starting point coordinate
    - ``w`` - Pattern width
    - ``h`` - Pattern height
    - ``r`` - Arc radius
    - ``c`` - When it is 1, the pixel is on; when ``c`` is 0, the pixel is off.

i2c object
-------

The mPython Board has been instantiated in the  ``I2C`` class, P19 and P20 are the SCL and SDA pins of I2C. I2C devices can be connected to the I2C bus of the mPython Board for operation.


Deatils of read and write I2C operations, see :ref:`machine.I2C<machine.I2C>` 模块或 :ref:`I2C basic tutorial <tutorials_i2c>` chapter.

MPythonPin class
-------

.. class:: MPythonPin(pin, mode=PinMode.IN,pull=None)

CReate Pin object

- ``pin`` mPython Board pin number definition, see :ref:`mPython Board pins definition <mpython_pinout>` 。

- ``mode`` pin mode. Before setting, defahlt is  `mode` = `PinMode.IN`

        - ``PinMode.IN`` equals to 1，digital input mode
        - ``PinMode.OUT`` equals to 2，digital output mode
        - ``PinMode.PWM`` equals to 3，analog output mode
        - ``PinMode.ANALOG`` equals to 4，analog input mode
        - ``PinMode.OUT_DRAIN`` equals to 5，Open-drain output mode

- ``pull`` specifies whether the pin is connected to a resistor, which can be one of the following：

       - ``None`` - No pull-up or pull-down resistors
       - ``Pin.PULL_UP`` - Pull-up resistor enable
       - ``Pin.PULL_DOWN`` - Pull-down resistor enable


Example::

        >>> from mpython import MPythonPin       # import MPython moduel
        >>> P0=MPythonPin(0,PinMode.IN)          # create pin 0 object, set digital input mode



.. method:: MPythonPin.read_digital()

Returns the level value of this IO pin. 1 represents high level, 0 represents low level

.. method:: MPythonPin.write_digital(value)

IO pin output level control. ``value`` =1 output high level, ``value`` =0 output low level.

.. method:: MPythonPin.read_analog()

Read ADC and return the read result, the returned value is between 0 and 4095.

.. method:: MPythonPin.write_analog(duty, freq=1000):

Set the duty ratio of the output PWM signal.

- ``duty`` 0 ≤ duty ≤ 1023
- ``freq`` PWM frequency, 0 < freq ≤ 0x0001312D（decimal base ：0 < freq ≤ 78125）


.. _MPythonPin.irq:

.. method:: MPythonPin.irq(handler=None, trigger=Pin.IRQ_RISING):

If the pin mode is configured as ``IN`` , you can configure the interrupt handler that is called when the trigger source of the pin is active.

Parameter:

     - ``handler`` is an optional function that is called when the interrupt is triggered.

     - ``trigger`` configures events that can trigger an interrupt. Value could be：

       - ``Pin.IRQ_FALLING`` falling edge interrupt
       - ``Pin.IRQ_RISING`` rising edge interrupt
       - ``Pin.IRQ_LOW_LEVEL`` low level interrupt
       - ``Pin.IRQ_HIGH_LEVEL`` high level interrupt

       These values can be used to perform  ``OR`` operations together to trigger multiple events.


.. _mpython.wifi:

WiFi class
------

Provide convenient WiFi connection network or wireless AP function. Note that turning on the WiFi function will increase power consumption.If not in use, turning off WiFi can reduce power consumption.

.. class:: wifi()

Build WiFi object and create ``sta`` object and  ``ap`` object. See :mod:`network` more application of modules.

    - STA is used by clients to connect to routers to connect to the network。
    - AP is used to mPython Board as a wireless AP access method
    
.. method:: wifi.connectWiFi(ssid,password,timeout=10)

Connect WiFi network

    - ``ssid`` -WiFi network ID
    - ``password`` -WiFi Password
    - ``tiemout`` - Link timeout, default 10 seconds

.. method:: wifi.disconnectWiFi()

Disconnect WiFi network connection

.. method:: wifi.enable_APWiFi(essid,password,channel=10)

Open WiFi wireless AP mode

 - ``essid`` - create WiFi network ID
 - ``password`` - Password
 - ``channel`` - Set WiFi channel,channel 1~13

.. method:: wifi.disable_APWiFi()

Turn off wireless AP
