.. _dht:
:mod:`dht` --- dht module
=========================================

The dht module provides dht series temperature and humidity sensor reading related functions.


Class DHT22
---------

Create Object
~~~~~~~
.. class:: DHT22(pin)

Create a DHT22 sensor object connected to the pin。

  - ``pin``: pin

  .. admonition:: support pins
      :class: attention

      * ESP32:GPIO0/2/4/5/16/17/18/19/21/22/23/25/26/27
      * mPython Board: P0/1/8/9/13/14/15/16

Example::

  from machine import Pin
  import dht

  d = dht.DHT22(Pin(Pin.P0))

Method
~~~~~~~

.. method:: DHT22.humidity()

Read and return the humidity value of the sensor.  

Example::

  d.measure()
  print(d.humidity())

.. method:: DHT22.temperature()

Read and return the temperature value of the sensor.  

Example::

  d.measure()
  print(d.temperature())





Class DHT11
---------

Similar to DHT22() function, no more details.
