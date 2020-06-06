MQTT protocol: Access to OneNET cloud platform
==========

With the development of mobile Internet, mqtt will make more contributions in the field of mobile message push because of its open source code and low power consumption,
In the field of IoT, MQTT is a solution for the communication between sensors and servers, the collection of information.
Soon, MQTT will enter all aspects of our lives, this article demonstrate the mPython Board to use the MQTT protocol to access the OneNET platform, and remotely control the RGB LED.


What is the MQTT protocol
--------------

Earlier in 1999, Dr. Andy Stanford-Clark of IBM and Dr. ArlenNipper of Arcom Company invented MQTT (Message Queuing Telemetry Transport) technology. MQTT is an instant messaging protocol developed by IBM and may become an important part of the Internet of Things. The protocol supports all platforms and can connect almost all networked items with the outside world. It is used as a communication protocol for sensors and actuators (such as connecting houses to houses via Twitter).

OneNET Platform
+++++++++

OneNET platform creates MQTT protocol products and adds devices。
OneNET Platform official website address：https://open.iot.10086.cn/，Login to the developer center and to add a new product.

.. image:: /../images/classic/oneNet_1.gif

Create a new device for the new product mPython.

.. image:: /../images/classic/oneNet_2.gif


Programming
+++++++

Program sample::

    from umqtt.simple import MQTTClient
    from mpython import *
    from machine import Timer

    # MQTT server address domain name：183.230.40.39
    SERVER = "183.230.40.39"
    #Device ID
    CLIENT_ID = "deviceID"
    #产品ID
    username='productID'
    #Product APIKey:
    password='APIKey'

    mywifi=wifi()

    def sub_cb(topic, msg):

        print((topic, msg))
        if msg == b"on":
            rgb.fill((50,0,0))       #Turn on the red light
            rgb.write()
        elif msg == b"off":        #Lights off
            rgb.fill((0,0,0))
            rgb.write()


    def main(server=SERVER):
        #Port number：6002
        c = MQTTClient(CLIENT_ID, server,6002,username,password,keepalive=10)    # Keep connected, set 10 seconds for interval
        c.set_callback(sub_cb)
        c.connect()
        tim1 = Timer(1)           #Create Timer 1
        tim1.init(period=2000, mode=Timer.PERIODIC,callback=lambda n:c.ping())   #  Send heartbeat packets and keep connected  
        print("Connected to %s" % server)
        try:
            while 1:
                c.wait_msg()
        finally:
            c.disconnect()

    mywifi.connectWiFi("ssid","password")
    main()


.. Hint::

    Modify the device ID, product ID and APIKEY parameters in the program, as shown.

.. image:: /../images/classic/oneNet_3.png

.. image:: /../images/classic/oneNet_4.png


Display the effect
+++++++


When reset and restart the mPython Board, execute the start program.


.. image:: /../images/classic/oneNet_5.png


At this time, the device status light on our OneNET cloud platform is green, indicating that it is online.


.. image:: /../images/classic/oneNet_6.png

When send  ``on`` 、``off`` instructions through the page, the message received at the terminal will be printed. The RGB LED on the mPython Board will change accordingly.

.. image:: /../images/classic/oneNet_7.gif

.. image:: /../images/classic/oneNet_8.png
