Introduction to TCP/IP
================

*re-copy to* `[Liao Xuefeng Python tutorial] <https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320037768360d53e4e935ca4a1f96eed1c896ad1217000>`_



Although everyone is familiar with the Internet now, the emergence of computer networks is much earlier than the Internet.

In order for a computer to be networked, it is necessary to specify communication protocols. In the early computer networks, each manufacturer specified a set of protocols. IBM, Apple, and Microsoft all have their own network protocols, which are incompatible with each other. This is like a group of people say. English, some speak Chinese, some speak German, and people who speak the same language can communicate, but not between different languages.

In order to connect all the different types of computers all over the world, a set of universal protocols must be specified. In order to achieve the goal of the Internet, the Internet Protocol Suite (Internet Protocol Suite) is a universal protocol standard. The Internet is composed of the words inter and net. The original meaning is to connect to the "network" network. With the Internet, any private network can connect to the Internet as long as it supports this protocol.

Because the Internet protocol contains hundreds of protocol standards, but the two most important protocols are the TCP and IP protocols, so everyone refers to the Internet protocol as TCP / IP protocol.

When communicating, both parties must know each other's logo, just like sending emails must know the other party's email address. The unique identifier of each computer on the Internet is the IP address, similar to ``123.123.123.123`` . If a computer is connected to two or more networks, such as a router, it will have two or more IP addresses, so the IP address corresponds to the computer's network interface, usually a network card. 

The IP protocol is responsible for sending data from one computer to another through the network. The data is divided into small pieces, and then sent out through IP packets. Due to the complexity of the Internet link, there are often multiple lines between the two computers, so the router is responsible for deciding how to forward an IP packet. The characteristics of IP packets are that they are sent in blocks and that there are multiple routes, but they are not guaranteed to arrive, nor are they guaranteed to arrive in sequence.

.. image:: /../images/tutorials/tcpip.png

The IP address is actually a 32-bit integer (called IPv4). The IP address represented by a character string such as 192.168.0.1 is actually a digital representation of the 32-bit integer grouped by 8 bits. The purpose is to facilitate reading.

The IPv6 address is actually a 128-bit integer, which is an upgraded version of IPv4 currently in use, represented by a string similar to ``2001:0db8:85a3:0042:1000:8a2e:0370:7334`` 。

TCP protocol is based on IP protocol. The TCP protocol is responsible for establishing a reliable connection between the two computers to ensure that the data packets arrive in order. The TCP protocol will establish a connection through a handshake. Then, each IP packet is numbered to ensure that the other party receives it in order. If the packet is dropped, it will be automatically resent.

Many commonly used higher-level protocols are based on the TCP protocol, such as the HTTP protocol for browsers, the SMTP protocol for sending mail, etc.

In addition to the data to be transmitted, a TCP packet also contains the source and destination IP addresses, source and destination ports.

What does the port do? When two computers communicate, it is not enough to send only the IP address, because there are multiple network programs running on the same computer. After a TCP packet comes, whether it is handed over to the browser or QQ, you need to distinguish the port number. Each network program applies to the operating system for a unique port number. In this way, the two processes need their own IP addresses and respective port numbers to establish a network connection between the two computers.



Understand the basic concepts of TCP / IP protocol, the concept of IP address and port, we can start network programming.
