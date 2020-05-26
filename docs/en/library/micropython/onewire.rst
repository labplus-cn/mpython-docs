:mod:`onewire` --- Single Bus
====================================================

.. module:: onewire
    :synopsis: Single bus

Single bus is one-wire bus, which is the peripheral serial expansion bus technology launched by American DALLAS company.
Different from SPI and I²C serial data communication methods. It uses a single signal line to transmit both clock and data, and the data transmission is bidirectional. It has many advantages such as saving I/O lines, simple resource structure, low cost, and easy bus expansion and maintenance.

The single bus is suitable for a single master system and can control one or more slave devices. The host can be a microcontroller, the slave can be a single bus device, the data exchange between them only through a signal line. 
When there is only one slave device, the system can operate as a single-node system; when there are multiple slave devices, the system operates as a multi-node system. Figure 12-1 shows a single bus multi-node system.

.. figure:: https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=3459156120,798055718&fm=173&app=25&f=JPEG?w=574&h=232&s=88A07D3287AC4D091AF4C1DB0000C0B1
    :width: 400
    :align: center

    Schematic diagram of a single bus multi-node system




OneWire Class
------------


.. class:: OneWire(pin)

Create OneWire class

- ``pin`` - `machine.Pin` instance object.


.. method:: reset(required=False)


.. method:: readinto(buf)

Read byte

.. method:: write(buf)

Write byte

.. method:: select_rom(rom)

.. method:: scan()

Scan for devices on the bus


.. method:: crc8(data)

