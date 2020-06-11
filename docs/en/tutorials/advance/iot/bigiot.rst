
BIGIOT
==============

BIGIOT is an IoT cloud platform that makes it easier for you to communicate with smart devices. You can chat with your smart device, send instructions, and view real-time data in the form of conversations and remote controls through the Internet,  
set alarm conditions according to actual needs, and notify users through APP, email, SMS, Weibo, WeChat, etc.

.. figure:: https://www.bigiot.net/Public/upload/UEditor/image/20181024/1540363897144665.jpg
    :width: 550
    :align: center

    BIGIOT architecture

- BIGIOT platform communication protocol：https://www.bigiot.net/help/1.html

Connect mPython Board to BIGIOT
----------------------------------

Get ready
+++++++++++++++++++++

* First, needs to register an account at https://www.bigiot.net and to add a smart device.

* In the program, you need to use bigiot's mPython library, get it at  https://github.com/labplus-cn/awesome-mpython/tree/master/library . bigiot.py upload to the file system.



Communication between devices
++++++++++++++++++++++++


.. literalinclude:: /../../examples/IoT/bigiot.py
    :caption: simple bigiot communication examples::
    :linenos:



Prior connection to BIGIOT platform, ensure the mPython Board is connected to Internet. While instantiating ``Device(id,api_key)`` , use the smart device information of BIGIOT, ``ID`` and  ``API KEY`` .
Set the callback function for say communication  ``say_callback(f)`` . f(msg,id,name)callback function,  ``msg`` parameter is the received message,  ``id`` parameter is the sending device ID,  ``name`` parameter is the device name.
``check_in()`` is the online function of the device, you can see the connection status of the device on BIGIOT.
In the above example, set the callback function and print out the data received by say communication.

The client sends a message to the dashboard
++++++++++++++++++++++++++++++++++++++++

BIGIOT supports communication between multiple clients and devices, such as browsers, WeChat mini-program public accounts, and APP (Android).


.. figure:: /../images/tutorials/IoT/bigiot_1.gif
  :align: center

  Browser

.. figure:: /../images/tutorials/IoT/bigiot_2.gif
  :align: center
  :width: 500

  WeChat Mini Program

The mPython Board sends to the device or client
++++++++++++++++++++++++++++++++++++++++++

Device
~~~~~~~~~


You can add multiple smart devices on the Shell IoT platform at the same time. As long as the smart device is online and knows the ``ID`` of the device, you can send messages to the smart device.

To ID: 7947 device sends a message::

  >>> device.say(device_id = 7947, msg = 'hello I am mPython')

Client
~~~~~~~~~

Send messages to clients such as web or WeChat, you can view your user ID on the platform "Personal Information" ::

  >>> device.say(user_id = 5600, msg = 'hello I am mPython')

Group
~~~~~~~~~

You can also set up multiple smart devices on the platform to form a group and send messages to the group, so that all members of the group can receive messages, similar to the IP multicast function::

  >>> device.say(group_id = 145, msg = 'hello I am mPython')

``say(user_id, group_id, device_id, msg)`` this function is used for device or client conversation. ``user_id`` 、``group_id`` 、``device_id`` parameters are user ID, group ID, device ID. Use parameters according to the dialogue object.
``msg`` is a conversation message, the type is a string.

Send data to the interface
++++++++++++++++++++++

To the interface: 9564, send the light data of the mPython Board::

  while True:
      val=light.read()
      device.update(9564,str(val))
      sleep(1)

BIGIOT provides an interface for collecting real-time sensor data and drawing charts. update(id, data) is the function of uploading data.  ``id`` is the interface ID, and the ``data`` parameter is the uploaded sensor data. Note that this type is a string. If it is int, it needs to be converted to str.
Also, data transmission should not be too fast, at least 1 second interval.

Voice Assistant
------------------

BIGIOT can also connect with Tmall Genie and Baidu Voice Assistant, and Shell Internet of Things devices as clients. Receive voice commands from the server. Realize the application of voice control for smart home.

Tmall Genie control method for BIGIOT
++++++++++++++++++++++++++++++++++++++++++++++++

Tmall Genie control methodd reference tutorial: https://www.bigiot.net/talk/359.html



