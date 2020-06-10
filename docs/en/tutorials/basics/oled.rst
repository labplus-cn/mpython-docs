Display
======================================

The mPython Board has a 1.3-inch OLED display with a resolution of 128x64. Use `Google Noto Sans CJK <http://www.google.cn/get/noto/help/cjk/>`_ Open source sans serif font. Font height 16 pixels. Supporting Chinese (both simplified and traditional), Korean, Japanese, latin alphabet and others text characters.

.. Hint::

  OLED is a derived class of ``machine.framebuf`` , so the method of inheriting framebuf can be consulted for details.  :meth:`framebuf`。


Text Display
-------

Before use, first import the mpython module::

  from mpython import *

`hello,world` text display::

  # It is easy to see how the characters are displayed on the display, and the mode selects the pixel flip mode
  oled.DispChar('hello,world!',0,0,mode=TextMode.rev)
  # In the default mode, the background pixels of the character are off
  oled.DispChar('hello,world!',0,16,mode=TextMode.normal)
  oled.show()

.. figure:: /../images/tutorials/display_char_pixel.png
   :width: 500px
   :align: center

   How character pixels are displayed on the mPython Board screen


- DispChar(str,x,y) function can write text with coordinates in the upper left corner to FrameBuffer. ``str`` is for displaying text content, supports simplified Chinese, traditional Chinese, Japanese and Korean languages. ``x`` ``y`` is OLED display
  Starting xy coordinates. `oled.show()` to send FrameBuffer to OLED to refresh and display the screen。
- Noto Sans CJK 16-pixel constant-height, unequal-width fonts are used. Different characters, the width will be different, as shown above。


.. literalinclude:: /../../examples/display/helloworld.py
    :caption: Display Chinese or other language text of HELLO WORLD on OLED display:
    :linenos:


.. figure:: /../images/mPython Board - Front View.png
    :align: center

    Multiple language hello,world display


::

  oled.fill(0)
  oled.show()

In addition to clearing the display, you can also light up the entire screen pixels::

  oled.fill(1)  
  oled.show()

.. Note::

  fill() fills the entire FrameBuffer area.

OLED display also supports setting of brightness of the screen::

  oled.contrast(brightness)

.. Note::

  Range of brightness value is 0~255。


Basic shape drawing
-------

.. literalinclude:: /../../examples/display/drawline.py
    :caption: Example: Draw lines.
    :linenos:


.. image:: /../images/tutorials/drawline.gif
   :scale: 100 %
   :align: center


OLED can draw some points, lines, rectangles and other shapes.

Pixel display::
                       
  oled.pixel(50,0,1)   #Set (50,0) pixel to 1, light up
  oled.show()          #Refresh the display

.. Note::

  oled.pixel(x, y, [c] ) Can display pixel points,  ``x`` ， ``y`` are point coordinates (x, y). ``c`` is the color value, when it is 1, the pixel is lit, if it is 0, it is no. If c is not given, get the color value of the specified pixel.
  If c is given, set the specified pixel to the given color.


Draw line::

  oled.hline(0,1,20,1)  #Draw a horizontal line, starting point coordinates (0,1), line length 20
  oled.show()
  oled.vline(10,10,20,1)  #Draw a vertical line, starting point coordinates (10, 10), line length 20
  oled.show()
  oled.line(15,15,80,20,1)  #Draw a line in the direction of the start coordinate (15, 15) and end coordinate (80, 20)
  oled.show()

.. Note::

  * oled.hline(x, y, w, c ) You can draw a horizontal line, ``x`` ， ``y`` are the point coordinates (x, y), ``w`` is the line width, and ``c`` is the color value.
  * oled.vline(x, y, l, c ) You can draw vertical lines same way as above.
  * oled.line(x1, y1, x2, y2, c) Can draw lines in any direction, starting coordinate (x1, y1), ending coordinate (x2, y2), ``c`` is the color value.


Draw hollow / solid rectangle::

  oled.rect(60,25,30,25,1)   #Draw a rectangle with starting coordinates (60, 25), width 30, height 25
  oled.show()
  oled.fill_rect(100,25,20,25,1)   #Draw the starting coordinates (100, 25), width 20, height 25 fill the rectangle with full color
  oled.show()

.. Note::

  * oled.rect(x, y, w, h, c) is used to draw a rectangular frame. A rectangular frame with a starting coordinate of (x, y), width  ``w`` , height ``h`` , ``c`` is the color value. 
  * oled.fill_rect(x, y, w, h, c) is used to draw a rectangle of fill color in the same way as rect(). Unlike rect(), only draw a rectangular frame. 

Draw arc rectangle::

  oled.RoundRect(40, 20, 50, 30, 5, 1)   #Draw an arc rectangle with starting coordinates (40, 25), width 50, height 30, and arc radius 5
  oled.show()

.. Note::

  oled.RoundRect(x, y, w, h, r, c)is used to draw arc rectangle. A rectangular frame with a starting coordinate of (x, y), width  ``w`` ， height ``h`` , arc radius  ``r`` and ``c`` as color value.
 
For more OLED display operation and shape drawing, please refer to :ref:`oled object <oled>` 。


Display Image
-------

First of all, we need to process the image into a size 128 * 64, a color depth of 1 or bmp format in black and white mode. You can use Photoshop or other image processing software. 

The next step is to use the modulo tool to modulo the picture. There are PCtoLCD, lcd image converter and other module-taking software on the Internet, you can choose according to your preferences. The following is used :download:`Img2Lcd tool </../docs/tools/Image2Lcd.zip>` 。

* Step 1. Import 128x64, bmp format pictures
* Step 2. Select parameters, output data type [C language array]、  scan mode [horizontal scan]、grayscale output [monochrome]、width and height [128*64]
* Step 3. Click Save to automatically generate modulus data. 

.. image:: /../images/tutorials/image2lcd.png


Assign the modulus data to the bmp array and display it on the OLED display.

.. literalinclude:: /../../examples/display/chinamap.py
    :linenos:

.. image:: /../images/tutorials/earth.png
  :scale: 50 %
  :align: center

After assigning the modulus data to the bmp array, draw the picture to the OLED display::

  oled.bitmap(0, 0, bmp, 128, 64, 1)
  oled.show()

.. Note::

  oled.bitmap(x, y, bitmap, w, h, c) can draw bitmap patterns, ``x`` 、``y`` are the coordinates x, y of the starting point of the upper left corner, ``bitmap`` is the name of the pattern btyearray byte array, ``w`` is the width of the pattern, ``h`` is the height of the pattern, ``c`` is the color value, the pixel is on when ``1`` and the pixel is off when``0`` .


Dynamic display
-------

Combined with the display of the above still frames, you can divide the dynamic picture to be displayed into each frame and send it to the OLED display to display it frame by frame！

Different from the above picture using bmp format. This time use pbm (Portable BitMap) format pictures, you can use Photoshop to convert to pbm format. 

pbm data format::

  P4
  #CREATOR：GIMP PNM filter version 1.1
  128 64
  <data>

The first three lines of the pbm data format are set to label the image. Then the image data. The first line indicates the image format, and the second line is a comment, usually the program used to create it. The third line is the image size。
The latter is the image data we need. Data storage per pixel bit stream, ``1`` means pixel is on, ``0`` means pixel is off.

:download:`Dynamic display material download </../../examples/display/material/scatman.zip>`

First upload the pre-prepared pbm pictures of each frame to the root directory of the file system of the control panel.

.. literalinclude:: /../../examples/display/scatman.py
    :caption: Read the image data stream frame by frame and display it on the OLED display:
    :linenos:

.. image:: /../images/tutorials/scatman.gif
  :align: center


IMport mpython and framebuf module::

  from mpython import *
  import framebuf

Open each frame of picture in binary read-only format::

  with open('scatman.%s.pbm' % n, 'rb') as f:
      f.readline()       # Image format
      f.readline()       # explanatory note
      f.readline()       # Image size
      data = bytearray(f.read())
  fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
  images.append(fbuf)     #Assign each frame of data to the list


Use ``file.read()`` in the program to read the image data stream frame by frame. Note, the first three lines are not the data we need, use  ``readlines()``  to discard it. Create a FrameBuffer object for each frame of data stream and store all frame buffers in the images list.

.. Note::

  open(file, mode) is used to open a file and return the file object. ``file``  is the file name, ``mode`` mode to open file, ``rb``  Open a file in binary format for read-only, generally used for non-text files such as pictures, etc.

.. Note::
 
  framebuf.FrameBuffer(buffer, width, height, format) can build frame buffer objects,  ``buffer`` buffer data, ``width`` is the picture width，``height`` is the picture height，``format`` is the format of FrameBuffer, That is, the scan mode of data output when the corresponding picture is taken：``framebuf.MONO_HLSB`` is horizontal；``framebuf.MONO_VLSB`` is vertical.

Display the stored frame buffer frame by frame to the OLED display::

  oled.blit(i, 0, 0)
  oled.show()

.. Note::

 oled.blit(fbuf, x, y) use OLED to display picture frames，``fbuf`` as FrameBuffer object, ``x`` 、``y`` coordinates x、y of the starting point.

























