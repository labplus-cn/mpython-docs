.. currentmodule:: machine
.. _machine.UART:

Class UART -- Duplex serial communication bus
=============================================

UART implements standard UART / USART duplex serial communication protocol. At the physical level, it consists of 2 wires：RX and TX.
Communication unit is a character (not to be confused with character string), it can be 8 or 9 bit wide.


Create object
------------

.. class:: UART(id, ...)

    create UART object

    - ``id`` - 串口号:1、2  

    .. Attention:: 
    
    ``UART(id=0)`` Used for REPL, cannot be used！

    ::
    
        from machine import UART
        from machine import Pin

        uart = UART(1, baudrate=115200, rx=Pin.P15, tx=Pin.P16, timeout=10)

Method
-------

.. method:: UART.init(baudrate=9600, bits=8, parity=None, stop=1, \*, ...)

Initialize the UART bus with the given parameters


    - ``baudrate`` - Baud Rate
    - ``bits``- Number of digits per character, 7, 8 or 9。
    - ``parity``- Parity: 0-even, 1-odd
    - ``rx`` , ``tx`` - UART read and write pins
    - ``stop`` - Number of stop bits:1、2
    - ``timeout``- Time-out time (unit: ms) < timeout ≤ 0x7FFF FFFF (Decimal：0 < timeout ≤ 2147483647)
    - ``txbuf`` - Specify the character length of the TX buffer
    - ``rxbuf`` - Specify the character length of the RX buffer

    .. Attention:: 

        * All pins can be used as the input RX of the serial port, except ``P2``、``P3`` 、``P4`` 、``P10`` can only be used as input, all other pins can theoretically be used as Output TX.
        * ``GPIO 1`` 、``GPIO 3`` are used for the USB serial port of the mPython Board. In the initial UART definition, the ``tx`` ，``rx``  pins are generally not used unless you want to use the mPython Board. USB interface as serial output.





.. method:: UART.deinit()

   Turn off the UART bus.

.. method:: UART.any()

    Returns an integer, counting the number of characters that can be read without blocking. If there are no characters available, it will return 0, if there are characters, it will return a positive number.
    Even if there are multiple readable characters, this method can return 1.

   For more complex available characters, please use select.poll::

    poll = select.poll()
    poll.register(uart, select.POLLIN)
    poll.poll(timeout)

.. method:: UART.read([nbytes])

    Read character. If ``nbytes``  is specified, at most read multiple bytes, otherwise read as much data as possible.

    Return value：A byte object containing the bytes read。 ``None`` Return on timeout. 

.. method:: UART.readinto(buf[, nbytes])

   Read bytes into ``buf`` . If ``nbytes`` is specified, at most multiple bytes are read. Otherwise, at most read ``len(buf)`` bytes.

   Return value：Number of bytes read and stored to timeout ``buf`` or ``None`` timeout.

.. method:: UART.readline()

   Read a line, ending with a newline.

   Return value：Read line or ``None`` timeout.

.. method:: UART.write(buf)

  Write byte buffer to bus.

   Return value：Number of bytes written or ``None`` timeout.

.. method:: UART.sendbreak()

  Send an interrupt on the bus. This makes the duration of the bus drive longer than the time required to transfer characters normally.
