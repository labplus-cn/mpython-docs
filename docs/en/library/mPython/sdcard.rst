
.. module:: sdcard
   :synopsis: SD Card

:mod:`sdcard` --- SD Card
==================================================

Secure digital or SD cards and micro microSD cards are inexpensive and can add a lot of storage space to the device. MicroPython, only 1M flash memory to store code and data. 
If you have more flash memory space, you can connect the micro SD card to the control board through SPI communication to expand its storage space.


.. figure:: https://www.digikey.com/maker-media/520920e2-79cd-4b23-8e89-1acc572496e8
    :width: 400
    :align: center

    SD Card

SDCard class
-------------

.. Class:: SDCard(spi, cs)

Create SDCard object, initialize SD card.

First, make sure that the pins of the SPI bus are physically connected to the micro SD card correctly. Make sure your micro SD card is formatted with FAT or FAT32 file system. Then, use os.mount() to mount the virtual new FAT file system of the SD card into the specified directory.
After the mount is complete, you can use Python's file operations (such as open, close, read, and write) to access the file.

- ``spi`` - machine.SPI object
- ``cs``  - SPI CS control pin


.. literalinclude:: /../../examples/file/sdcard.py
    :caption: example - mount SD card
    :linenos:


.. literalinclude:: /../../examples/file/print_directory.py
    :caption: example - lsit all files
    :linenos:
 
