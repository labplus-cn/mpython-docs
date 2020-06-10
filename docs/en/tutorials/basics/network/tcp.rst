Socket - TCP
================


What is socket?
-----

``Socket`` is an abstract concept of network programming. Usually we use a Socket to mean “opened a network line”, and open a Socket need to know the IP address and port number of the target computer, and then specify the protocol type.

Introduction to TCP protocol
-----

TCP protocol, Transmission Control Protocol (Transmission Control Protocol, abbreviated as TCP) is a connection-oriented, reliable, byte stream-based transport layer communication protocol, defined by IETF RFC 793.

TCP communication needs to go through three steps: creating a connection, data transmission, and terminating the connection. In the TCP communication model, before communication starts, you must first create a relevant connection before sending data, similar to "calling"" in daily routine。

When the socket is working, the two sides of the connection are divided into server and client, that is, C / S mode, and the TCP communication principle is as follows:

.. figure:: /../images/tutorials/tcp principle.png
    :scale: 90 %
    :align: center

    Socket TCP communication process


---------------------------------

TCP programming
-----


This part of the tutorial will show how to use TCP sockets as a client or server. For more comprehensive use of the socket module, please refer to :mod:`usocket` module.
The following tutorials need to use TCP network debugging tools. The following is the  **Network Test Utility** of IOS，You can search and install in the APP Store, please click to download the android system 。 :download:`Network Test Utility.apk </../tools/com.jca.udpsendreceive.2.apk>` 

Announcement: The TCP client （tcpClient）here is your computer or mobile phone, and the TCP server （tcpServer）is the mPython Board.

TCP client
~~~~~~~~


The general steps of TCP programming client are：

1. Create a socket, use function socket()
2. To set the socket property, use the functions setsockopt() , *optional* 
3. Bind the IP address, port and other information to the socket, use the function bind() , *optional* 
4. Set the IP address and port of the other party to be connected
5. To connect to the server, use the function connect()
6. To send and receive data, use the functions send() and recv(), or read() and write()
7. Close network connection



.. literalinclude:: /../../examples/network/tcpClient.py
    :caption: TCP Client example:
    :linenos:


.. Attention:: 

    Since they are transmitted in bytes on the network, you need to pay attention to data encoding and decoding.

.. Attention:: In the above example, use ``connectWiFi()`` to connect to the same router wifi. You can also use ``enable_APWiFi()`` to turn on the AP mode and build a wifi network to allow other devices to access it.

First, the mPython Board and mobile phone must be connected to the same local area network. OPen Network Test Utility，Enter the “TCP Server” interface.
TCP Server IP selects the IP address of the mobile phone in the network, and the port number can be set from 0 to 65535. Then, click Listen to start listening on the port.
Set the TCP server IP address  ``host`` and port number ``port`` selected above in the program, restart the program。

When the connection to the Server is successful, the TCP Server will receive the text ``hello mPython,I am TCP Client`` sent by the Client. At this point, you send text to the Client in the TCP Server, the control panel will
receive text and display the text on the OLED screen.


.. image:: /../images/tutorials/socket_1.gif
   

TCP server
~~~~~~~~


The general steps of the TCP programming server are：

1. Create a socket, use function socket()
2. To set the socket attribute, use the functions setsockopt() , *optional* 
3. Bind the IP address, port and other information to the socket, use the function bind() 
4. Turn on monitoring and set the maximum monitoring number, use the function listen()
5. Wait for the client to request a connection, use the function accept()
6. To send and receive data, use the functions send() and recv()，or read() and write() 
7. Close network connection



tcpServer example:

.. literalinclude:: /../../examples/network/tcpServer.py
    :caption: TCP Server示例:
    :linenos:


.. Attention:: In the above example, use ``connectWiFi()`` to connect to the same router WiFi. You can also use ` ``enable_APWiFi()`` to turn on the AP mode and build a wifi network to allow other devices to access it.

First, the mPython Board and mobile phone must be connected to the same local area network. The control panel restarts the running program, and the TCP Server end waits for the Client connection request. Open the Network Test Utility, enter the “TCP Client”  interface, fill in the Remote host and port, namely ``socket.blind(ip,port)``
IP address and port. After the Connect is successfully connected, send text, and the control panel receives the text and displays it on the oled screen and returns it to the TCP Client. You can see the text from Client->Server，Server->Client in the receiving interface of the mobile phone.


.. image:: /../images/tutorials/socket_2.gif
    :scale: 60 %
    :align: center

