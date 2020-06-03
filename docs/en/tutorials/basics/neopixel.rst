RGB LED
=====================

mPython Board built-in with three WS2812 LED, WS2812 is a low-power RGB tri-color LED integrated WS2811 driver, an integrated current control chip, it can achieve 256-level brightness display and complete true color display of 16777216 colors. A special single-line communication method is used to control the color of RGB lights, which is easy to use.  

On-Board RGB LED
----------
Example：Light up RGB LED
::
    from mpython import *

    rgb[0] = (255, 0, 0)  # set to RED for full brightness
    rgb[1] = (0, 128, 0)  # set to GREEN for half brightness
    rgb[2] = (0, 0, 64)   # set to BLUE foe a quarter of brightness
    rgb.write()


First of all, import the mPython module::

    from mpython import *
    
.. Note:: Imported the mPython module, a NeoPixel object been created to control the WS2812 LEDs by just operate the RGB object. 

Set the color::

    rgb[0] = (255, 0, 0)  # set to RED at full brightness
    rgb[1] = (0, 128, 0)  # set to GREEN at half brightness
    rgb[2] = (0, 0, 64)   # set to BLUE at a quarter brightness


.. Note:: 
    * rgb[n] = (r, g, b) to set the color of each pixel，``n`` is the number of onboard RGB LED，The first been 0.  ``r``、``g``、``b`` are color brightness values, range is 0 ~ 255.
    * rgb.fill(rgb_buf) to fill the color of all pixels, such as：rgb.fill((255,0,0))，set all RGB LED to RED at full brightness.

Output colors to RGB LEDs::

    rgb.write()


.. _neopixel_strip:
    
External Striplight
----------


.. image:: /../images/tutorials/glamour.jpg
    :width: 600
    :align: center


Example：Light Up external striplight
::

    from mpython import *
    import neopixel
    np = neopixel.NeoPixel(Pin(Pin.P15), n=24,bpp=3,timing=1)


    def wheel(pos):
        # Generate a rainbow color spectrum by setting each color range parameter between 0 and 255
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos*3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos*3)
            g = 0
            b = int(pos*3)
        else:
            pos -= 170
            r = 0
            g = int(pos*3)
            b = int(255 - pos*3)
        return (r, g, b) 

    def cycle(np,r,g,b,wait=20):
        # Loop effect, with one pixel running at all light strip positions, while other pixels are off.
        for i in range(4 * np.n):
            for j in range(np.n):
                np[j] = (0, 0, 0)
            np[i % np.n] = (r, g, b)
            np.write()
            sleep_ms(wait)


    def bounce(np,r,g,b,wait=20):
        # Bounce effect, the waiting time determines the speed of the bounce effect
        n=np.n
        for i in range(4 * n):
            for j in range(n):
                np[j] = (r, g, b)
            if (i // n) % 2 == 0:
                np[i % n] = (0, 0, 0)
            else:
                np[n - 1 - (i % n)] = (0, 0, 0)
            np.write()
            sleep_ms(wait)


    def rainbow_cycle(np,wait_us):
        # rainbow effect
        n=np.n
        for j in range(255):
            for i in range(n):
                pixel_index = (i * 256 // n) + j
                np[i] = wheel(pixel_index & 255)
            np.write()
            sleep_us(wait_us)

    while True:
        cycle(np,50,50,50,wait=20)
        bounce(np,50,0,0,wait=20)
        rainbow_cycle(np,20)


.. figure:: /../images/tutorials/neopixel_control_leds_cycle.png
    :align: center

    cycle effect

.. figure:: /../images/tutorials/neopixel_control_leds_bounce.png
    :align: center

    bounce effect

.. figure:: /../images/tutorials/neopixel_control_leds_rainbow.png
    :align: center

    rainbow effect


If you need to use an external ribbon, you must first create a neopixel object and define the ``pin`` 、``bpp`` 、 ``timeing`` parameters before you can control the LEDs on the ribbon through this object.
For details, refer to :ref:`neopixel<neopixel>` module.

.. Hint:: 

   | mPyhton provide ``neopixel`` enhanced version ``led strip`` module, packaged with enhanced NEOPIXEL display effect, and the operation is simple. For detailed instructions, please go to the following link.
   | mPython-ledstrip：https://github.com/labplus-cn/awesome-mpython/tree/master/library
