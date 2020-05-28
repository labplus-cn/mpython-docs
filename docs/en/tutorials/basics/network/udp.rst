Socket - UDP
================

Introduction to UDP protocol
---------

UDP (User Datagram Protocol) is a connectionless, unreliable, transport protocol communication protocol based on datagram. 

The communication process of UDP is more simple than that of TCP. The three-way handshake and four-way handshake that do not need to be copied reflect the connectionless.
Therefore, UDP transmission speed is faster than TCP, but it is easy to lose packets, the data arrival order is not guaranteed, the lack of congestion control, adhering to the principle of best effort delivery, reflects the unreliability.

The following figure explains the interactive process of the UDP communication connection between the server and the client：

.. figure:: /../images/tutorials/udp原理.png
    :scale: 100 %
    :align: center

   Socket UDP communication process

-----------------

UDP Programming
--------

Usually when we talk about network programming, it refers to TCP programming by default, which is the TCP method we talked about in the previous chapter.
When the socket function creates a socket object, no parameters are given, and the default is SOCK_STREAM , which is socket (socket.AF_INET, socket.SOCK_STREAM), which means that a socket is created for streaming network communication.

``SOCK_STREAM``  is connection-oriented, that is, each time you send and receive data, you must create a connection through ``connect`` , which is also bidirectional, that is, any party can send and receive data. The protocol itself provides some guarantee mechanisms to ensure that it is reliable , Ordered, that is, each packet arrives at the receiver in the order in which it was sent. 

``SOCK_DGRAM`` is the network communication of the User Datagram Protocol. It is connectionless and unreliable, because the two parties of the communication do not know whether the other party has received the data or whether it has received the data normally.
After any socket, you can use  ``sendto`` to send data, and you can also use ``recvfrom`` to receive data. I don't care if the other party exists or if data is sent. It is characterized by relatively fast communication speed. Everyone knows that TCP is going to shake hands three times, but UDP does not.


UDP Client
~~~~~~~~

The usual steps of UDP programming client are： 

1. Create a UDP socket, use the function socket(socket.AF_INET, socket.SOCK_DGRAM) 
2. To set the socket attribute, use the function ``setsockopt()``  *optional* 
3. Bind the IP address, port and other information to the socket, use the function ``bind()``  *optional* 
4. Set the other party's IP address and port attributes
5. To send data, use the function ``sendto()``
6. Close network connection

Example of UDP client:


.. literalinclude:: /../../examples/network/udp_client.py
    :caption: UDP客户端的示例
    :linenos:

.. image:: /../images/tutorials/udpclient.gif
    :align: center

UDP Server
~~~~~~~~

The usual steps of the server side of UDP programming are： 

1. Create a UDP socket, use the function socket(socket.AF_INET, socket.SOCK_DGRAM)   
2. To set the socket attribute, use the function  ``setsockopt()``  *可选* 
3. Bind the IP address, port and other information to the socket, use the function ``bind()`` 
4. BReceive data in a loop, using the function ``recvfrom()``
5. Close network connection


.. literalinclude:: /../../examples/network/udp_server.py
    :caption: UDP服务端的示例
    :linenos:


.. Note:: 

    The return value of the``recvfrom()`` function is a binary (bytes, address), where bytes is the received byte data and address is the sender ’s IP address and port number,
    It is represented by a two-tuple (host, port). Note that the return value of the recv() function only has bytes data. UDP, each time you send ``sendto()`` and receive dat ``recvfrom`` , you need to specify the address information. Unlike TCP programming, you do not need to cal ``listen()`` and ``accept()`` .

.. Attention:: In the above example, use ``connectWiFi()`` to connect to the same router wifi. You can also use  ``enable_APWiFi()`` to turn on the AP mode and build a wifi network for other devices to access. So you don't need to rely on other router wifi network.
