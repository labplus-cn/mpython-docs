MQTT
=====



MQTT (Message Queue Telemetry Transport), a telemetry transport protocol, provides a subscription/publish mode, which is more simple, lightweight, and easy to use. For restricted environments (low bandwidth, high network delay, unstable network communication), it can be simply summarized as.


MQTT is a “light weight” messaging protocol based on publish-subscribe for use on top of the TCP/IP protocol, it is suitable for connections in remote locations that require "small code footprint" or limited network bandwidth.
A protocol that enables one-to-many communication (people call it publish or subscribe). It consists of 3 functions, namely broker, publisher and subscriber.

.. figure:: /../images/tutorials/IoT/mqtt.png
  :align: center
  :width: 600

  broker、publisher、subscriber

The intermediary assumes the role of a server that forwards MQTT communications. Relatively speaking, publishers and subscribers act as clients. The publisher is the client responsible for sending messages, and the subscriber is the client responsible for receiving messages.
Messages exchanged by MQTT are accompanied by a “subject” address, and each client regards this “subject” as a receiving address, and performs the operation of transmitting messages to it.
Metaphorically, an intermediary is a mailbox that receives mail.

.. figure:: /../images/tutorials/IoT/iot_publish.png
  :align: center
  :width: 600 

 Mechanism of MQTT communication

The intermediary is waiting for each client to connect to it. The subscriber connects to the intermediary and tells the intermediary the name of the topic he wants to subscribe to. This is called a subscription.
Then the publisher connects to the intermediary and sends the message with the subject as the receiving address. This is the release. As soon as the publisher publishes the topic, the intermediary will deliver the message to the subscribers who subscribe to the topic.

As shown in the figure above, if the subscriber subscribes to topic A, the intermediary will only deliver the message to the subscriber if the publisher posts topic A. 
Subscribers and intermediaries are always connected, and publishers only need to establish a connection at the time of publication, but to publish several times in a short period of time, you need to stay connected. 
Because the intermediary plays the role of forwarding messages, there is no need for each client to know the other party’s IP address and other mail receiving addresses on the network. And because multiple clients can subscribe to the same topic, the publisher and subscriber are in a one-to-many relationship.
In the communication between the device and the server, the device is equivalent to the publisher, and the server is equivalent to the subscriber.


.. figure:: /../images/tutorials/IoT/IoT_subscribe.png
  :align: center
  :width: 600 

  MQTT theme examples


The theme uses a layered structure. Multiple symbols can be specified with symbols like “#” and “+”. As shown in the figure above, the “#” symbol is used in /Sensor/temperature/# , so that all topics starting with /Sensor/temperature/  can be specified.
In addition, the symbol “+” is used in /Sensor/+/room1 , so that you can specify all topics that start with /Sensor/、and end with /room1 .

*The principle of MQTT is reproduced to [Illustrated Internet of Things/ Japan NTT DATA Group；Ding Ling translation. --北京：人民邮电出版社， 2017.4]*

Introduction to the Internet of Things platform
----------------

Announcement - subscribe messaging model requires a message broker server. The proxy server is responsible for distributing messages to interested clients based on the message subject.

.. Hint:: 

    At present, there are various MQTT IoT platforms on the Internet, you can choose the mqtt IoT platform that suits you according to your requirements. I recommend the following relatively good IoT platforms.

*  OneNet China Mobile IoT platform：https://open.iot.10086.cn/

    - Advantages: Support multiple communication protocols, such as MQTT, HTTP, etc.；Editable application function, can make page UI for data display and switch control.
    - Disadvantages: The platform operation is more complicated, slightly different from the official MQTT, and it is difficult to understand for beginners.

* DFRobot Easy IoT platform：http://iot.dfrobot.com.cn/

    - Advantages: simple operation, suitable for beginners to learn.
    - Disadvantages: Cannot customize topic; lack of UI interface editing on the application side, unable to present data.

* Adafruit IoT platform：https://io.adafruit.com/

    - Advantages: simple operation, suitable for MQTT teaching；There are ample dashboard editing functions, which can present data well；Support IFTTT, can be connected to many Internet services, and play variously.
    - Disadvantages: foreign servers, unstable connection, often unable to connect.

In addition to the above, you can also build an mqtt server yourself.



Connect to MQTT proxy server
-----------------

The following uses Easy IoT to explain how to use MQTT to subscribe to topics and publish messages.

First, import the required modules::

    from umqtt.simple import MQTTClient    # import umqtt.simple module for simple MQTT client function.  
    from mpython import *                  # import mpython module

First, connect the mPython Board to the Internet::

    mywifi=wifi()                           # Instantiate wifi class
    mywifi.connectWiFi("ssid","password")   # WiFi connection, ssid is the username, password is the password

Example MQTTClient::

    SERVER = "182.254.130.180"       # Easy IoT MQTT server address
    username='yourIotUserName'       # Iot_id on your Easy IoT
    password='yourIotPassword'       # Iot_pwd on your Easy IoT
    CLIENT_ID = "yourClientID"       # Client ID on your Easy IoT

    c = MQTTClient(CLIENT_ID, SERVER,1883,username,password)  # MQTTClient class instance
    c.connect()         # mqtt connect

MQTTClient(client_id, server, port=0, user=None, password=None, keepalive=0), ``client_id`` parameter is the unique id of MQTT client； The ``server`` parameter is for the mqtt proxy server
IP address； The port number of the server accessed by the ``port`` parameter is mqtt, which is generally 1883, and the port will be different for different platforms；The ``user`` parameter is the username used to obtain mqtt authentication；The ``password`` parameter is the password for obtaining MQTT authentication；
The ``keepalive`` parameter is the connection save time.When there is no subscription or release package within the keepalive interval, the connection will be automatically disconnected.

.. image:: /../images/tutorials/mqtt_1.png
    :scale: 60%

Announcement
-------

Publish the device topic on Easy IoT::

    c.publish("Bkgk2zXb4",'hello')

.. Note:: 

    ``publish(topic, msg)`` , ``topic`` parameter is the published topic. On the management interface of Easy IoT, the devices are distinguished by topic and cannot be modified.；``msg`` parameter is the message of the topic；

After publishing, you can find the message just published in the “View Details” of the device in the Easy IoT workshop, as follows:

.. image:: /../images/tutorials/mqtt_2.png

.. image:: /../images/tutorials/mqtt_3.png

Subscribe to Topics
-------

Set to print out after receiving a message::

    def sub_cb(topic, msg):             
            print((topic, msg))  

    c.set_callback(sub_cb) 

Before subscribing to the topic, you need to set the callback function ``set_callback(sub_cb)``, ``sub_cb`` is the function to be processed after receiving the message, which must contain two parameters.

Topic subscription, ``topic`` parameter is the topic to be subscribed::

        
    c.subscribe(topic)


Finally use ``wait_msg()`` to wait for the message::

    while True:         
            c.wait_msg()  


Remote lights switching
^^^^^^^

The following example uses the remote control switch light made by the MQTT subscription theme function::

    from umqtt.simple import MQTTClient    
    from mpython import *   
    from machine import Timer               

    SERVER = "182.254.130.180"            # Easy IoT MQTT server address
    username='yourIotUserName'            # Iot_id on your Easy IoT
    password='yourIotPassword'            # Iot_pwd on your Easy IoT
    CLIENT_ID = "yourClientID"            # Client ID on your Easy IoT

    TOPIC='yourTopic'                     # Topic of your device on Easy IoT

    mywifi=wifi()                         # Instantiate WiFi class
    mywifi.connectWiFi("ssid","password")   # WiFi connection, ssid is the username, password is the password

    try:
        def sub_cb(topic, msg):             # Callback function when a subscription message is received
            print((topic, msg))             # Print the received topic message
    
            if topic == TOPIC.encode():     # If the topic is the topic of our device, received byte type. Here you need to convert TOPIC to byte type.
 
                if msg == b"on":                # If the message is "on", lights turn ON 
                        rgb.fill((0,20,0))
                        rgb.write()

                elif msg == b"off":         # If the message is "off", lights turn OFF
                    rgb.fill((0,0,0))
                    rgb.write()

        c = MQTTClient(CLIENT_ID, SERVER,1883,username,password,keepalive=30)   # MQTTClient class instance, and set the connection hold interval to 30 seconds
        c.connect()                             # mqtt connects
        c.set_callback(sub_cb)                  # Set callback function
        c.subscribe(TOPIC)                      # Subscribe to topics
        print("Connected to %s" % SERVER)

        tim1 = Timer(1)                          # Create Timer 1
        tim1.init(period=20000, mode=Timer.PERIODIC,callback=lambda n:c.ping())     # Send PING at 20-second intervals to keep connected

        while True:         
            c.wait_msg()                    # Waiting for messages in a loop
    finally:
        c.disconnect()                     # When abnormal, disconnect MQTT

Then click on the device “Send Message” to enter the Easy IoT workshop to send the topic message as follows:

.. image:: /../images/tutorials/mqtt_4.png

.. image:: /../images/tutorials/mqtt_5.gif
    :scale: 50%





