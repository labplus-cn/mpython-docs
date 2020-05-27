.. currentmodule:: machine
.. _machine.I2C:

Class I2C --  Two-wire serial protocol
=======================================

I2C is a two-wire protocol for communication between devices. At the physical level, it consists of 2 lines: SCL and SDA, which are the clock and data lines, respectively.

Create an I2C object connected to a specific bus. They can be initialized at creation time or later.

Example::

        from machine import I2C,Pin

        i2c = I2C(scl=Pin(22), sda=Pin(23), freq=400000)          # create I2C peripheral at frequency of 400kHz
                                                                                                                                                                                                                                                # depending on the port, extra parameters may be required
                                                                                                                                                                                                                                                # to select the peripheral and/or pins to use

        i2c.scan()                      # scan for slaves, returning a list of 7-bit addresses

        i2c.writeto(42, b'123')         # write 3 bytes to slave with 7-bit address 42
        i2c.readfrom(42, 4)             # read 4 bytes from slave with 7-bit address 42

        i2c.readfrom_mem(42, 8, 3)      # read 3 bytes from memory of slave 42,
                                                                                                                                        #   starting at memory-address 8 in the slave
        i2c.writeto_mem(42, 2, b'\x10') # write 1 byte to memory of slave 42
                                                                                                                                        #   starting at address 2 in the slave
                                                                                                                                        
Construct object
------------

.. class:: I2C(id=-1, \*, scl, sda, freq=400000)

   Construct and return a new I2C object with the following parameters：
        


        - ``id`` Identify specific I2C peripherals. The default value -1 selects the software implementation of I2C
        - ``scl`` Should be a pin object, specify the pin used for SCL
        - ``sda`` Should be a pin object, specify the pin used for SDA
        - ``freq`` Should be an integer that sets the maximum frequency of SCL. 0 < freq ≤ 500000(Hz)。

.. Attention:: 

        I2C can use GPIO 0/2/4/5/9/16/17/18/19/21/22/23/25/26/27

Universal way
---------------

.. method:: I2C.init(scl, sda, \*, freq=400000)

        Initialise the I2C bus with the given arguments:

     - ``scl`` Pin object of the SCL clock line
     - ``sda`` Pin object of the SDA data line
     - ``freq`` SCL clock rate

.. method:: I2C.deinit()

   Turn off the I2C bus.

.. method:: I2C.scan()

 Scan all I2C addresses between 0x08 and 0x77 and return a list of responses. If the device is pull-down after sending its address (including the write bit) on the bus, the device will respond.

Primitive I2C operation
------------------------

The following methods implement Primitive I2C operations main bus operations, and can be combined to perform any I2C transaction. If you need more control bus, provide them,
Otherwise, standard methods can be used (see below).

.. method:: I2C.start()

   Generate a START condition on the bus (SDA transitions to a low level when SCL is high).

.. method:: I2C.stop()

        Generate a STOP condition on the bus (SDA transitions to high when SCL is high).

.. method:: I2C.readinto(buf, nack=True)

Read bytes from the bus and store them in  ``buf`` . The number of bytes read is the length of  ``buf`` . After receiving all but the last byte，
``ACK`` will be sent on the bus. After receiving the last byte, if ``NACK``   is true, then ``NACK``will be sent, otherwise  ``ACK`` will be sent (and in this case, the slave device assumes that More bytes will be read in the call).


.. method:: I2C.write(buf)

Write the bytes in ``buf`` to the bus. Check if ``ACK`` is received after each byte, if ``NACK`` is received, stop sending the remaining bytes. This function returns the number of  ``ACK`` received.


Standard bus operation
-----------------------

The following method implements standard I2C master read and write operations for a given slave device. 

.. method:: I2C.readfrom(addr, nbytes, stop=True)

Read ``addr`` from the specified program in ``nbytes`` . If  ``stop`` is true, a stop condition is generated at the end of the transmission. Return a ``bytes`` object that reads the data.

.. method:: I2C.readfrom_into(addr, buf, stop=True)

Read ``addr`` from the slave specified by ``buf`` . The number of bytes read will be the length of ``buf`` . If  ``stop`` is true, a stop condition is generated at the end of the transmission. 

This method returns ``None`` 。
  

.. method:: I2C.writeto(addr, buf, stop=True)

Write the bytes in  ``buf`` to the slave specified by ``addr`` . If NACK is received after writing a byte from  ``buf`` , the remaining bytes are not sent.
If ``stop`` is true, then even if a NACK is received, a STOP condition will be generated at the end of the transmission. This function returns the number of ACKs received. 


Register operation
-----------------

Some I2C devices act as memory devices (or register sets) that can be read and written. In this case, there are two addresses related to the I2C transaction: slave address and memory address.
The following methods are convenient functions for communicating with these devices.

.. method:: I2C.readfrom_mem(addr, memaddr, nbytes, \*, addrsize=8)

Starting from the memory address specified by ``memaddr`` read ``nbytes`` from the slave specified by ``addr`` . The parameter  ``addrsize`` specifies the address size in bits. 
Returns the ``bytes`` object that read the data. 

.. method:: I2C.readfrom_mem_into(addr, memaddr, buf, \*, addrsize=8)
    
Starting from the memory address specified by ``memaddr`` read ``buf``  from the slave specified by ``addr`` . The number of bytes read is the length of ``buf``.
The parameter ``addrsize`` specifies the address size in bits.

This method returns ``None`` .

.. method:: I2C.writeto_mem(addr, memaddr, buf, \*, addrsize=8)

Starting from the memory address specified by  ``memaddr`` write ``buf`` to the slave specified by ``addr`` . The parameter ``addrsize`` specifies the address size in bits.。

This method returns ``None`` 。
