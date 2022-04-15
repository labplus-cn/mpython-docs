
.. _umqtt.simple:

.. module:: umqtt.simple
   :synopsis: MQTT client function

:mod:`umqtt.simple` --- MQTT client function
=========================================

MQTT is a release-based - Subscription “lightweight” messaging protocol for use on top of TCP/IP protocol.
Provide a subscription/publish model, which is more simple, lightweight, and easy to use. For limited environments (low bandwidth, high network latency, unstable network communication), it can be simply summarized as the IoT.

.. Hint:: 

   Module originate from ``MicroPython-lib`` : https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.simple

create object
-------------

.. class:: MQTTClient(client_id, server, port=0, user=None, password=None, keepalive=0,ssl=False, ssl_params={})

    - ``client_id``
    - ``server``
    - ``port``
    - ``user``
    - ``password``
    - ``keepalive``
    - ``ssl``
    - ``ssl_params``

Method
--------

.. method:: MQTTClient.set_callback(f)

    - ``f`` - f(topic, msg) is the callback function, the first parameter is ``topic``  the received topic, the second parameter is ``msg`` is the topic message



Set callback for received subscription message

.. method:: MQTTClient.set_last_will(topic, msg, retain=False, qos=0)

    ``topic`` and ``msg`` Byte type

Set MQTT “last will” message. Should be called before connect() .

.. method:: MQTTClient.connect( clean_session=True )

Connect to server. If this connection uses a persistent session stored on the server, it returns True (if the clean_session = True parameter is used, it returns False（default））.

.. method:: MQTTClient.disconnect()

Disconnect from the server, release resources.

.. method:: MQTTClient.ping()

Ping server (response is automatically handled by wait_msg()）

.. method:: MQTTClient.publish(topic, msg, retain=False, qos=0)

    ``topic`` and ``msg`` Byte type

Make an announcement

.. method:: MQTTClient.subscribe(topic, qos=0)

    ``topic`` Byte type

Subscribe to topics

.. method:: MQTTClient.wait_msg()

Waiting for server message. Subscription messages will be passed to the callback set via set_callback(）, any other messages will be processed internally. 

.. method:: MQTTClient.check_msg()

Check if the server has any pending messages. If it is, it is processed in the same way as wait_msg(）, if not, it returns immediately.


.. Attention:: 

    * wait_msg() and check_msg() are “main loop iteration” methods, blocking and non-blocking versions. wait_msg() if you do not have any other foreground tasks to execute (ie your application only responds to subscribed MQTT messages), check_msg() if you also handle other foreground tasks, you should call them in a loop periodically.
    * Please note that if you only post messages, you do not need to call wait_msg()/ check_msg(), and do not subscribe to messages.
    * Both publish and subscribe support QoS 0 and 1. Does not support QoS2 to keep code size small. Except for ClientID, currently only supports “clean session” parameter to connect.
    * All data related to MQTT messages are encoded as bytes. This includes the message content and topic name (even if the MQTT specification states that the topic name is UTF-8 encoded). The reason is：binary data (bytes) is received via a network socket.
    * MQTT Keep Alive: MQTT includes a keep alive function that provides a workaround for the issue of half-open connections (or at least makes it possible to assess if the connection is still open).Keep alive ensures that the connection between the broker and client is still open and that the broker and the client are aware of being connected. When the client establishes a connection to the broker, the client communicates a time interval in seconds to the broker. This interval defines the maximum length of time that the broker and client may not communicate with each other.
