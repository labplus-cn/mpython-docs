.. _tutorials_i2c:

I2C
===============

I²C (Inter-Integrated Circuit) literally means between integrated circuits, it is actually short for I²C Bus. The I2C bus type is a simple, bidirectional, two-wire, synchronous serial bus designed by Philips Semiconductors in the early 1980s, which is mainly used to connect the integrated circuit (ICS).

I2C protocol is a way for multiple devices to communicate with each other using only two lines (clock and data lines). Any device can be the master device that controls the I2C clock and data lines to communicate with other devices.
Each I2C device is assigned a unique address to identify it during read and write operations. When the device sees the address it sent on the I2C bus, it will respond to the request, when it sees a different address, it will ignore it.
Using unique addresses, many devices can share the same I2C bus without interference.



---------------------------------------

When using the mPython Board, you can use the :ref:`I2C class<machine.I2C>` function to interact with devices on the I2C bus. In most cases, you will act as an I2C “master” and can read and write data with other I2C devices.
You can also act as an I2C “slave” or peripheral, they are assigned an address and can listen to and respond to requests from other I2C devices.




Master
----------

Most I2C communication modules have similar operation methods. The mPython Board acts as an I2C master device, and the module acts as a slave device, responding to host requests.
The following SHT20 module is used as a demonstration to explain how to read slave device data.


.. figure:: http://wiki.labplus.cn/images/1/1c/黑色传感器最终版12.20-28.png
    :align: center
    :width: 250

    blue:bit Temperature Humidity module (SHT20)

Read SHT20 temperature function::

    def sht20_temperature():             
        i2c.writeto(0x40,b'\xf3')               
        sleep_ms(70)                                   
        t=i2c.readfrom(0x40, 2)                         
        return -46.86+175.72*(t[0]*256+t[1])/65535      

``i2c.writeto(addr, buf)`` is an I2C write operation function, which is  ``addr`` to the I2C device, and sends ``buf`` cache bytes. The control board needs to send ``0xf3`` bytes to the SHT20, telling it that I need to read the temperature data, after a delay of 70 ms.
Read 2 bytes of data to SHT20. The read operation uses ``i2c.readfrom(addr, nbytes)`` ，``nbytes`` is the number of bytes read.

After reading 2-byte data, you also need to do data processing to convert the temperature unit according to the description of SHT20 manual.


.. figure:: /../images/tutorials/sht20_temper.png
    :align: center
    :width: 400

    SHT20 temperature conversion formula

.. figure:: /../images/tutorials/sht20_humidi.png
    :align: center
    :width: 400

    SHT20 humidity conversion formula

The method of reading the humidity is also similar. First send the “0xf5” byte to tell SHT20 that I want to read the humidity data, and finally convert the humidity unit according to the formula::

    def sht20_humidity():
        i2c.writeto(0x40,b'\xf5')                 
        sleep_ms(25)                                    
        t=i2c.readfrom(0x40, 2)                      
        return -6+125*(t[0]*256+t[1])/65535           

.. Hint:: 

    For more I2C operation methods，see :ref:`I2C class<machine.I2C>` chapter.


The complete SHT20 example:

.. code-block:: python
    :linenos:

    from mpython import *                   # import all mpython object
                                                                                            
    def sht20_temperature():      
        """Obtain the temperature value of SHT20 module
        Return:Temperature
        """        
        i2c.writeto(0x40,b'\xf3')                       # Write byte “0xf3” to address 0x40, SHT20
        sleep_ms(70)                                    # SHT20 measurement takes time, must wait
        t=i2c.readfrom(0x40, 2)                         # Read 2 bytes of data from the x40 address, SHT20
        return -46.86+175.72*(t[0]*256+t[1])/65535      # Perform temperature conversion processing on the read data T=-46.86+175.72*St/2^16

    def sht20_humidity():
        """Obtain the humidity value of SHT20 module
        Return:Humidity
        """ 
        i2c.writeto(0x40,b'\xf5')                       # Write byte “0xf5” to address 0x40, SHT20
        sleep_ms(25)                                    # SHT20 measurement takes time, must wait
        t=i2c.readfrom(0x40, 2)                         # Read 2 bytes of data from the x40 address, SHT20
        return -6+125*(t[0]*256+t[1])/65535             # Perform humidity conversion processing on the read data RH=-6+125*Srh/2^16

    while True: 
        temper=sht20_temperature()
        humid=sht20_humidity()
        print("sht20 temperature: %0.1fC sht20 humidity: %0.1f%%" %(temper,humid))
        oled.DispChar("Temperature:%0.1fC, Humidity:%d%%" %(temper,humid),10,25)
        oled.show()
        sleep(1)
