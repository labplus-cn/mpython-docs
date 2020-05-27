.. currentmodule:: machine
.. _machine.SPI:

Class SPI -- Serial Peripheral Interface Bus Protocol (Master)
=====================================================================


.. admonition:: What is SPI？

    SPI is the abbreviation of Serial Peripheral Interface. It is a synchronous serial interface technology introduced by Motorola. It is a high-speed, full-duplex, synchronous communication bus. 
    The SPI protocol is mainly used in short-distance communication systems, especially embedded systems. Many chip peripheral devices, such as LED display drivers, I / O interface chips, UART transceivers, etc., widely use the SPI bus protocol. 

SPI is a synchronous serial protocol driven by the master device. At the physical level, the bus consists of 3 lines：SCK，MOSI，MISO。
Multiple devices can share the same bus. Each device should have a separate fourth signal SS (slave selection), used to select a specific device on the bus that communicates with.
SS signal management should be carried out in user code（via:class:`machine.Pin` class）。

Construct object
------------

.. class:: SPI(id, ...)

Construct an SPI object on the given bus. 

    - ``id`` -  hardware SPI at 1，the default value is to build software SPI. 


Construction of hardware SPI::

    >>> from machine import SPI
    >>> hspi = SPI(1)
    >>> hspi
    SPI(id=1, baudrate=500000, polarity=0, phase=0, bits=8, firstbit=0, sck=-1, mosi=-1, miso=-1)
    >>> 




软SPI的构建::

    from machine import SPI, Pin

    spi = SPI(baudrate=100000, polarity=1, phase=0, sck=Pin(17), mosi=Pin(27), miso=Pin(18))

Method
-------

.. method:: SPI.init(baudrate=1000000, \*, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=None, mosi=None, miso=None, pins=(SCK, MOSI, MISO))

   Initialize SPI bus with given parameters：

     - ``baudrate`` SCK clock frequency。
     - ``polarity`` 0 or 1, the level of the idle clock line。
     - ``phase`` 0 or 1 to sample data on the first or second clock edge, respectively. 
     - ``bits`` The width of each transmission (in bits). All hardware is guaranteed to support only 8。
     - ``firstbit`` can be  ``SPI.MSB`` or ``SPI.LSB``.
     - ``sck``, ``mosi``, ``miso`` is the pins (machine.Pin) object for bus signals. For most hardware SPI blocks (selected by the parameters of the ``id`` build object), the pins are fixed and cannot be changed. In some cases, the hardware module allows 2-3 alternative pin groups for the hardware SPI module. Any pin assignment only applies to bitbanging SPI driver（ ``id`` = -1）.
     - ``pins`` -  esp32 do not have ``sck`` ， ``mosi`` ， ``miso`` parameters, but allows specifying them as a tuple ``pins`` .

.. method:: SPI.deinit()

   Turn off the SPI bus.

.. method:: SPI.read(nbytes, write=0x00)

   Read the specified number of bytes, ``nbytes``  and write a single byte continuously by the given ``write`` . Return objects containing  ``bytes`` read data. 

.. method:: SPI.readinto(buf, write=0x00)

    Read in the buffer specified by  ``buf`` , while continuously writing the single byte given by ``write`` .

    Returns  ``None``。

    Note：On ``esp32`` , this function returns the number of bytes read.


.. method:: SPI.write(buf)

    Write the bytes in `` buf`` .

    Returns ``None``。

    Note：：On ``esp32`` , this function returns the number of bytes written.

.. method:: SPI.write_readinto(write_buf, read_buf)

    Write bytes from ``write_buf`` and read into ``read_buf`` . 缓冲区可以是相同的，也可以是不同的，但是两个缓冲区都必须具有
    same length.

    Returns ``None``。

    Note：On ``esp32`` , this function returns the number of bytes written.

Constant
---------

.. data:: SPI.MASTER

   Used to initialize the SPI bus to the host; this is only used for  ``esp32``.

.. data:: SPI.MSB

   Set the first digit to be the highest digit.

.. data:: SPI.LSB

   Set the first bit to the lowest bit.
