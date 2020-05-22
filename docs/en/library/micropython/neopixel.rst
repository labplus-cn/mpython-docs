.. _neopixel:
:mod:`neopixel` --- WS2812 LED Striplight
=========================================


NeoPixels, also known as WS2812 LED Striplight, are full-color led striplight connected in series. You can set the value of RED, GREEN, BLUE colors individually. 
Values between 0 and 255. The neopixel module can generate WS2812 control signals through precise time control.

Create Object
------------

.. class:: NeoPixel(pin, n,bpp=3,timing=0, brightness=1.0)

  - ``pin`` :Output pins, refer to available pins below
  -  ``n`` :Number of series connected LED
  - ``bpp``:
  
    - ``3``:The default is 3 colors (RBG) LED
    - ``4``:For LEDs with more than 3 colors, such as RGBW pixels or RGBY pixels, use 4-tuple RGBY or RGBY pixels

  - ``timing``:The default is 0 for 400KHz rate; and 1 for is 800KHz rate
  - ``brightness``:Brightness adjustment, range 0 ~ 1, default is 1.0
  
.. Attention:: 

  The pin pins available for NeoPixel are P5, P6, P7 (RGB on board), P8, P9, P11, P13, P14, P15, P16, P19, P20 of the control board.


Example::

  from machine import Pin
  import neopixel

  pin = Pin(17, Pin.OUT)
  np = neopixel.NeoPixel(pin, n=3,bpp=3,timing=1)   #800khz


Method
-------

.. method:: NeoPixel.write()

Write data to LED.  

Example::

  np[0] = (255, 255, 255) # Set the first LED pixel to white
  np.write()

.. method:: NeoPixel.fill(rgb_buf)

Fill all LED pixels. 

  - ``rgb_buf`` :rgb color

Example::

  np.fill( (255, 255, 255) )



.. method:: NeoPixel.brightness(brightness)

Brightnedd adjustment, range: 0~1.0
