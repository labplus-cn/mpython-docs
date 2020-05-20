:mod:`framebuf` --- FRame Buffer Operation
=============================================

.. module:: framebuf
   :synopsis: Framebuffer operation

This module provides a general frame buffer that can be used to create bitmap images to send to monitor for display.

Class FrameBuffer
-----------------

The framebuffer class provides a pixel buffer that can be drawn using pixels, lines, rectangles, text, and even other framebuffersFrameBuffer to draw. Useful to generating output for display.

Example::

    import framebuf

    # FrameBuffer needs 2 bytes for every RGB565 pixel
    buffer=bytearray(10 * 100 * 2)
    fbuf = framebuf.FrameBuffer(buffer, 10, 100, framebuf.RGB565)

    fbuf.fill(0)
    fbuf.text('MicroPython!', 0, 0, 0xffff)

Constructor
------------

.. class:: FrameBuffer(buffer, width, height, format, stride=width)

    Construct a FrameBuffer object. The parameter is:

        - *buffer* is an object with a buffer protocol that must be large enough to contain each pixel defined by the width, height, and format of the framebuffer.
        - *width*  is the width of the framebuffer in pixels
        - *height* is the height of the framebuffer in pixels
        - *format* specifies the pixel type used in framebuffer; allowed values are listed under the following constants. These settings are used to encode the number of bits in the color value and the layout of those bits in the buffer. In case of passing the color value c to the method, C is a small integer whose encoding depends on the format of framebuffer.
        - *stride* is the number of pixels between each horizontal pixel line in framebuffer. The default is width, but it may need to be adjusted to implement FrameBuffer in another large FrameBuffer or screen.。
        The size of the buffer must accommodate the increased step size.

    Must specify a valid *buffer* , *width*, *height*, *format*  and the optional *stride*. Invalid buffer size or size may cause unexpected errors.

Draw the original shape
------------------------

The following methods to draw shapes on framebuffer。

.. method:: FrameBuffer.fill(c)

    Fills the entire framebuffer with the specified color。

.. method:: FrameBuffer.pixel(x, y[, c])

   If C is not given, the color value of the specified pixel is obtained. If C is given, the specified pixel is set to the given color. 

.. method:: FrameBuffer.hline(x, y, w, c)
.. method:: FrameBuffer.vline(x, y, h, c)
.. method:: FrameBuffer.line(x1, y1, x2, y2, c)

    Draws a line from a set of coordinates using a given color and a thickness of 1 pixel. The ``line`` method draws lines to the second set of coordinates, while the ``hline`` 和 ``vline``  methods draw horizontal and vertical lines respectively until the given length. 

.. method:: FrameBuffer.rect(x, y, w, h, c)
.. method:: FrameBuffer.fill_rect(x, y, w, h, c)

    Draws a rectangle at a given location, size, and color. The ``rect`` method only draws 1 pixel outline, while th ``fill_rect`` method for drawing contour and interior. 

Draw Text
------------

.. method:: FrameBuffer.text(s, x, y[, c])

    Use coordinates as top left corner of text to write text to `FrameBuffer` . The color of the text can be defined by optional parameters, but the default value is 1. The size of all characters is 8x8 pixels, and currently the font cannot be changed. 


Other methods
-------------

.. method:: FrameBuffer.scroll(xstep, ystep)

   Move the contents of  `FrameBuffer` according to the given vector. This may leave footprints of previous colors in `FrameBuffer` .

.. method:: FrameBuffer.blit(fbuf, x, y[, key])

 

    Draw another `FrameBuffer` on the current one at the given coordinates`. If *key* is specified, it should be a color integer, and the corresponding color will be treated as transparent: all pixels with that color value will not be drawn.

    This method works between instances of `FrameBuffer` with different formats, but due to color format mismatch, the resulting color may be unexpected. 

Constant
---------

.. data:: framebuf.MONO_VLSB

    Monochrome (1bit) color format this defines a mapping in which bits in bytes are mapped vertically and bits 0 are closest to the top of the screen. 
    Therefore, each byte occupies 8 vertical pixels. Subsequent bytes appear in consecutive horizontal positions until they reach the far right. 
    Render additional bytes starting from the extreme left, 8 pixels lower。

.. data:: framebuf.MONO_HLSB

    Monochrome (1-bit) color format this defines the mapping of bits in a byte to be mapped horizontally. Each byte occupies 8 horizontal pixels, of which bit 0 is the leftmost. 
    Subsequent bytes appear in successive horizontal positions until they reach the extreme right. Render more bytes on the next line, one pixel lower. 

.. data:: framebuf.MONO_HMSB

    Monochrome (1 bit) color format this defines the mapping of bits in a byte to be mapped horizontally. Each byte occupies 8 horizontal pixels, of which bit 0 is the leftmost. 
    Subsequent bytes appear in successive horizontal positions until they reach the extreme right. Render more bytes on the next line, one pixel lower. 

.. data:: framebuf.RGB565

    RGB color format（16bit，5 + 6 + 5）

.. data:: framebuf.GS2_HMSB

    Gray scale color format（2bit）

.. data:: framebuf.GS4_HMSB

    Gray scale color format（4bit）


.. data:: framebuf.GS8

    Gray scale color format（8bit）
