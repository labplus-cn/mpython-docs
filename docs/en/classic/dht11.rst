DHT11 Sensor (Temperature and Humidity)
==========


DHT11 digital temperature and humidity sensor is a temperature and humidity composite sensor with calibrated digital signal output. It uses a dedicated digital module acquisition technology for temperature and humidity sensing technology to ensure that the product has extremely high reliability and excellent long-term stability. The sensor includes a resistive humidity sensing element and an NTC temperature measuring element, and is connected with a high-performance 8-bit microcontroller. Therefore, the product has the advantages of excellent quality, ultra-fast response, strong anti-interference ability, and extremely high cost performance.

.. image:: /../images/classic/dht11.png
    :scale: 50 %
    :align: center

The connection between DHT11 digital temperature, humidity sensor with the mPython Board requires the Expansion Board, utilize its connection pins. The pins available for DHT11 are P0/1/8/9/13/14/15/16. Recommended to use Pin 0. Mount the mPython Board to the Expansion Board as shown, DHT11 to Expansion Board through the dual female Dupont cable, DHT11 "+" connect to Expansion Board "V",  "-" to "G", “out” to “0” respectively.

.. image:: /../images/classic/dhtconnect.jpg
    :scale: 60 %
    :align: center


Example: Display DHT11 temperature and humidity reading
::

    from mpython import *
    from dht import DHT11
    
    dht=DHT11(Pin(Pin.P0))

    while True:
        dht.measure()
        oled.fill(0)
        oled.DispChar("Temperature:",0,10)
        oled.text("%d" % (dht.temperature()), 48, 14)
        oled.DispChar("Humidity:",0,35)
        oled.text("%d" % (dht.humidity()), 48, 40)
        oled.show()
        sleep_ms(100)

.. image:: /../images/classic/dhtexample.jpg
    :scale: 60 %
    :align: center


First, import mPython module and DHT11 class::

  from mpython import *
  from dht import DHT11

Instantiate the DHT11 class and set the mPython pin P0::

  dht=DHT11(Pin(Pin.P0))

DHT11 measures and returns temperature and humidity data::

  dht.measure()
  dht.temperature()
  dht.humidity()

.. Note::

``dht.measure()`` is the instruction to measure temperature and humidity data for DHT11, use ``dht.temperature()`` 、 ``dht.humidity()`` to get the measured temperature and humidity value after measurement.
  。
