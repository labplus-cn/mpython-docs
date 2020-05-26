:mod:`esp` --- ESP32 related functions
=========================================================

.. module:: esp
    :synopsis: ESP32 related functions


This  ``esp``  module contains specific functions related to the ESP32 module.


Function
---------

.. function:: flash_size()

    Returns the size of flash.

.. function:: flash_user_start()

    Read the memory offset at the beginning of user flash space.

.. function:: flash_read(byte_offset, length_or_buffer)

    Read buf.len() length data from the starting point of flash with address byte_offset and put into buf.

    - ``byte_offset`` ：flash offset address.
    - ``buf`` ：Receive data buffer, the length of the buffer is len

    ::

        import esp

        buf = bytearray(100)
        esp.flash_read(2097152, buf)

.. function:: flash_write(byte_offset, bytes)

    Write all the data in buf to the flash area with  byte_offset .

    - ``byte_offset`` ：flash offset address
    - ``buf`` ：Data buffer, the buffer length is len

    ::

        buf = bytearray(100)
        esp.flash_write(2097152, buf)

.. function:: flash_erase(sector_no)

    Erase flash sector

    - ``ector_no`` :Sector to be erased

    ::

        esp.flash_erase(512)

.. function:: osdebug()
