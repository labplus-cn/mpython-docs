.. _gui:

.. module:: gui
   :synopsis: Provide related functions of GUI class drawing

:mod:`gui` --- Provide related functions of GUI class drawing
==========


.. class:: UI

UI class
-------

Provide UI interface class controls

.. class:: UI(oled)

Create UI object.

    - ``oled``  - Objects coming into the framebuf class, such as mPython OLED display, then OLED object.

.. method:: UI.ProgressBar(x, y, width, height, progress)

Draw progress bar.

    - ``x`` 、 ``y`` - the upper left corner is used as the starting point coordinate
    - ``width`` - Progress bar width
    - ``height`` - Progress bar height
    - ``progress`` - Progress bar percentage

::

    from mpython import *

    myUI=UI(oled)
    myUI.ProgressBar(30,30,70,8,60)
    oled.show()

.. method:: UI.stripBar(x, y, width, height, progress,dir=1,frame=1)

Draw vertical or horizontal columnar bars

    - ``x`` 、 ``y`` - the upper left corner is used as the starting point coordinate
    - ``width`` - Column bar width
    - ``height`` - Column bar height
    - ``progress`` - Column bar percentage
    - ``dir`` - Column bar direction. dir= 1 for horizontal direction, dir= 0 for vertical direction.
    - ``frame`` - When frame=1 , the frame is displayed; when frame=0 , the frame is not displayed.

.. method:: UI.qr_code(str,x,y,scale=2)

    Draw 29*29 QR code

    - ``str`` - QR code data, type string
    - ``x`` 、 ``y`` - the upper left corner is used as the starting point coordinate
    - ``scale`` - amplification scale: can be 1, 2. Default is 2X.

::

    import gui
    from mpython import *
    ui=gui.UI(oled)
    ui.qr_code('https://mpython.readthedocs.io',0,0)
    oled.show()

Clock class
+++++++++

Provide analog clock display function

.. class:: Clock(oled,x,y,radius)

Create Clock object.

    - ``oled``  - Objects coming into the framebuf class, such as mPython OLED display, then OLED object。
    - ``x`` 、``y`` - The upper left corner is used as the starting point coordinate
    - ``radius`` - Clock radius


.. method:: Clock.settime()

Get local time and set analog clock time


.. method:: Clock.drawClock()

Draw a clock

.. method:: Clock.clear()

Clear the clock

::

    from mpython import*
    from machine import Timer
    import time


    clock=Clock(oled,64,32,30)

    def Refresh():
            clock.settime()
            clock.drawClock()
            oled.show()
            clock.clear()

    tim1 = Timer(1)

    tim1.init(period=1000, mode=Timer.PERIODIC, callback=lambda _:Refresh())



Image
+++++++++

Support `pbm` and `bmp` 1bit image formats.

.. Class:: Image()

Create Image object

.. method:: Image.load(path, invert=0)


Load the `pbm` or `bmp` picture format file and return the picture :class:`framebuf.FrameBuffer` object.   

- ``path`` - Picture file path
- ``invert`` - The pixels are inverted. 0 means no reversal, 1 means reverse.


Example::

    from mpython import *
    from gui import Image

    image = Image()
    fb = image.load('clown_1.bmp',1 )

    oled.blit(fb, 0, 0)
    oled.show()
