Network Basic
==============

.. _network_base:

MicroPython :mod: The `network`  module is used to configure WiFi connection。 There are two WiFi interfaces, STA mode is workstation mode (ESP32 is connected to the router)，
AP mode provides access services (other devices connected to ESP32). For more information about MicroPython's network connection method, please refer to :mod:`network` module.

STA mode
-------

The mPython Board is packaged based on the network module :ref:`mpython.wifi()<mpython.wifi>` Simplified wifi connection design::

    from mpython import *       #import the mpython module

    mywifi=wifi()     #Instantiate wifi class
    mywifi.connectWiFi("ssid","password")  # WiFi connection，set the SSID and Password

.. Note:: 

    After instantiate the wifi(), Will create the ``sta`` and ``ap`` objects. ``sta`` object is in workstation mode, connected to the network via a router. ``ap`` is AP mode, provides wifi access.

After successful connection, the REPL serial port is printed as follows::

    Connecting to network...
    Connecting to network...
    WiFi Connection Successful,Network Config:('192.168.0.2', '255.255.255.0', '192.168.0.1', '192.168.0.1')


Disconnect the WiFi::

    mywifi.disconnectWiFi()

Check if the wifi connection has been established::

    mywifi.sta.isconnected()

.. Note:: If the connection is established, return  ``True`` , otherwise ``False`` .

You can check the network settings in the following ways::

    mywifi.sta.ifconfig()

.. Note:: Return value 4-tuple: (IP address, netmask, gateway, DNS)
    
``ifconfig()`` with parameters, configure static IP. E.G.::

    mywifi.sta.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '192.168.0.1'))

AP mode
-------

In addition to the STA mode to connect to the router wifi, the control panel can also use the AP mode to provide wifi access services.

::

    from mpython import wifi                    # import the WiFi class mpython module

    mywifi=wifi()                               # instantiate wifi
    mywifi.enable_APWiFi(essid = "mpython-wifi", password = "mpython123456")    # Configure and open AP mode

``wifi.enable_APWiFi(essid,password)`` used to configure and open the AP mode function, ``essid`` parameter is WiFi name, ``password`` parameter is wifi password setting. After the AP mode is turned on, other control boards or network devices can connect to the network for network communication.

.. Attention:: AP mode is not a hotspot function similar to mobile phones, the device can connect to the Internet through the hotspot.This point needs attention.

----------------------------

Once WiFi is set up, then use network sockets to access the network.
A network socket represents an endpoint on a network device, and when two network sockets are connected together, communication can continue.
The Internet protocol is built on network sockets, such as email (SMTP), Web (HTTP), telnet, ssh, etc.
Assign a specific port to each of these protocols, it is just an integer. Given an IP address and port number, you can connect to a remote device and start communicating with it.

The next part of this tutorial will discuss how to use network sockets to perform some common and useful network tasks.
