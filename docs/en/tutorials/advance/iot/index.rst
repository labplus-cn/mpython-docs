Internet of Things
=====


IoT basics
--------------

The birth of the IoT
+++++++++++++

Lets start IoT tutorial by introducing the person who coiled the term “Internet of Things”. The term “Internet of Things”（(IoT) was coined by Kevin Ashton in a speech by Proctor & Gamble in 1999. He is the co-founder of the MIT Auto-ID Lab. He pioneered the use of RFID (for barcode detectors) in the field of supply chain management. He also founded Zensi, a company that produces energy sensing and monitoring technology.
So, let me first introduce you to a sentence by Kevin Ashton, who wrote this article for the RFID journal in 2009. This will help you understand the Internet of Things from the core.

If we have a computer that can understand everything - using the data they collected without any help from us - we will be able to track and calculate everything and greatly reduce waste, losses and costs. We know when they need to be replaced, repaired or recalled, and whether they are fresh or past. 
We need to empower computers with their own way of collecting information so they can see, hear and smell the world at will.

The above Kevin Kevin application will let you understand the ideology behind the development of the Internet of Things. Now let us try to further simplify the term and fundamentally understand the Internet of Things. After this, we will continue to move forward and seek the benefits of the Internet of Things.

What is the Internet of Things?
+++++++++++++++

When you hear the Internet of Things, what kind of impression will appear in your mind? The English of the Internet of Things is Internet of Things, abbreviated as IoT. The “thing” here refers to all the things around us that can be connected to the network. For example, the clothes you wear, those that you wear.
Watches, household appliances and cars at home, or the house itself, or even the book you are reading, as long as you can connect to the Internet, they are all "things" of the Internet of Things.

Just like we use the Internet to transfer information between each other, the Internet of Things is to share information and generate useful information between “things” to share information and generate useful information by connecting to the Internet, and it can operate without human management.
They can perceive and communicate with each other. Now imagine whether inanimate objects can perceive and interact without any human intervention. Sounds amazing, doesn't it?


.. figure:: /../images/tutorials/IoT/IoT.png
  :align: center

  what is IoT?

IoT architecture
+++++++++++++++

The current IoT architecture is usually divided into three layers: the perception layer, the network layer, and the application layer. There are also four-layer architecture, five-layer architecture, and seven-layer architecture. However, we will use the commonly used three-layer architecture for illustration. The icon is as follows:


.. figure:: /../images/tutorials/IoT/three-layer-iot-architecture.png
  :align: center
  :width: 400

  Three-tier IoT architecture

Perception layer
~~~~~~

Sensors, actuators and edge devices that interact with the environment

The perception layer is the five senses features of the Internet of Things. It is used to identify objects, perceive objects, collect information, and automatically control. For example, the temperature sensor installed on the air conditioner recognizes that the indoor temperature is higher than 30 degrees. After collecting this information, it turns on automatically. Air conditioning for cooling；This level involves various identification technologies, information collection technologies, and control technologies. Moreover, these technologies are used cross-wise. Some perceptions are single and some are comprehensive. For example, robots integrate various perception systems.
The most common ones in this layer are various sensors used to replace or extend human senses to complete the perception of the physical world, and also include RFID and two-dimensional code technologies used in the process of enterprise informatization.

Network layer
~~~~~~

Discover, connect and convert devices through the network and coordinate with the application layer

The network layer mainly realizes the transmission of information, routing (deciding the way of information transmission) and control (how to control the transmission of information), which is divided into two parts,
one part is the communication technology of the Internet of Things, and the other is the communication protocol of the Internet of Things. The communication technology is responsible for physically linking things and things and can communicate. The communication protocol is responsible for establishing communication rules and unified formats.

IoT communication protocols are as many as communication technologies, such as MQTT、DDS、AMQP、XMPP、JMS、REST、CoAP、OPC UA. The network layer is equivalent to the human brain and nerve center, and is mainly responsible for transmitting and processing the information obtained by the perception layer.

Application layer
~~~~~~

Provide users with professional services and functional data processing and storage

I understand that the application layer is supported by various communication protocols of the Internet of Things, analyzes the data formed by the Internet of Things at a macro level and feeds back to the perception layer to perform specific control functions, including controlling the coordination between objects and the environment Self-adaptive, collaboration between people and things.
The personal understanding of the application layer can be divided into two parts, one part is the general Internet of Things platform, built on the cloud platform, can be a kind of IAAS / PASS / SAAS or a hybrid.
At present, many enterprises have launched IoT platforms, such as Root Internet, Baidu Cloud Tiangong, Tencent QQ IoT Intelligent Hardware Open Platform, Ali Link IoT Platform, SAP Leonardo, Amazon AWS, Microsoft Azure, Google Cloud IoT Core.
The other part is to generate specific applications on this general Internet of Things platform. These applications are similar to mobile phone apps. Specific applications are how to specifically control how these things collect information and how to control things. These specific application scenarios include：

* Personal applications: wearable devices, sports and fitness, health, entertainment applications, sports, toys, parent-child, caring for the elderly；
* Smart home: home automation, smart routing, security monitoring, smart kitchen, home robot, sensor detection, smart pet, smart garden, tracking device；
* Intelligent transportation: Internet of vehicles, smart bicycles / motorcycles (helmet equipment), unmanned driving, drones, space exploration；
* Enterprise applications: healthcare, retail, payment / credit card, smart office, modern agriculture, building construction；
* Industrial Internet: smart manufacturing, energy industry, supply chain, industrial robots, industrial wearable devices (smart helmets, etc.)；
* From the application level, it can be seen that the Internet of Things can really be used everywhere and everywhere. The ultimate goal of the Internet of Things is to achieve the link of any object at any time and any place, to help humans have “a comprehensive perception ability, thorough cognitive ability and intelligent processing ability” in the physical world.



.. figure:: /../images/tutorials/IoT/IoT_smarthome.png
  :align: center
  :width: 700

  Automatically control the environment according to the human condition-take smart home as an example

IoT tutorial
---------

At present, there are multiple protocols such as MQTT、REST/HTTP、CoAP etc. There are also many integrated IoT platforms that can be accessed. This chapter focuses on how to access an IoT platform, IoT applications, and how to display the communication between objects.

.. toctree::
    :maxdepth: 1

    mqtt.rst
    yeelight.rst
    bigiot.rst
   
