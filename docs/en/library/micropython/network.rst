
:mod:`network` --- Network Configuration
===============================

.. module:: network
   :synopsis: network configuration


This module provides network driver and routing configuration. This module provides the network driver of specific hardware to configure the hardware network interface. Then, you can use :mod:`usocket`
The module uses the network services provided by the configured interface。


Function
-----

.. function:: phy_mode([mode])

    Set the PHY mode. The defined pattern constants are as follows:

    - ``mode``

      - ``MODE_11B`` -- IEEE 802.11b,1
      - ``MODE_11G`` -- IEEE 802.11g,2
      - ``MODE_11N`` -- IEEE 802.11n,4


WLAN class
---------

This class provides drivers for WiFi network processors in esp32. Example::

  import network
  # enable station interface and connect to WiFi access point
  nic = network.WLAN(network.STA_IF)
  nic.active(True)
  nic.connect('your-ssid', 'your-password')
  # now use sockets as usual


Create object
~~~~~~~~~~~

.. class:: WLAN(interface_id)

  Create WLAN network interface object。 

- ``interface_id`` 

  - ``network.STA_IF`` site is also called client, connecting to upstream WiFi access point
  - ``network.AP_IF``  as a hotspot, allows other WiFi clients to access. Hotspot mode allows users to configure their devices as hotspots, which makes wireless connections between multiple devices possible without the aid of an external router network.

The availability of the following methods depends on the interface type. For example, only STA interface can ``connect()`` to the access point.

Method
------------

.. method:: WLAN.active(is_active)

With parameters, it means whether to activate or not. Without parameters, it means to query the current status. When you do not use WiFi function, you can use active to turn off the wireless of physical layer.

- ``is_active`` 

  -  ``True``   Activate network interface
  -  ``False``  Disable network interface

.. method::  WLAN.connect(ssid, password)

Use the specified password to connect to the specified wireless network

- ``ssid``：WiFi ID
- ``password``：WiFi Password


.. method:: WLAN.disconnect()

Disconnecting the currently connected wireless network. 



.. method:: WLAN.scan([ssid，bssid，channel，RSSI，authmode，hidden])

Scan available wireless networks (scan only on STA interface) and return tuple list of WiFi access point information. 

- ``ssid`` Service Set ID.
- ``bssid`` The hardware address of the access point, which is returned as a byte object in binary form. To use the ``ubinascii.hexlify()`` convert it to ASCII format. 
- ``channel`` Channel
- ``RSSI`` Received signal strength indication
- ``authmode`` 

  - ``AUTH_OPEN`` = 0
  - ``AUTH_WEP`` = 1
  - ``AUTH_WPA_PSK`` = 2
  - ``AUTH_WPA2_PSK`` = 3
  - ``AUTH_WPA_WPA2_PSK`` = 4
  - ``AUTH_MAX`` = 6
	
- ``hidden``

  - ``False`` Visible
  - ``True`` Hidden
  


.. method:: WLAN.status()

Returns the current status of the wireless connection. 

  - ``STAT_IDLE`` -- no connection, no activities-1000
  - ``STAT_CONNECTING`` -- Connecting-1001
  - ``STAT_WRONG_PASSWORD`` -- Failed due to password error-202
  - ``STAT_NO_AP_FOUND`` -- Failed, because there is no access point reply,201
  - ``STAT_GOT_IP`` -- Connected-1010
  - ``STAT_ASSOC_FAIL`` -- 203
  - ``STAT_BEACON_TIMEOUT`` -- Timeout-200 
  - ``STAT_HANDSHAKE_TIMEOUT`` -- Handshake timeout-204 



.. method:: WLAN.isconnected()

- In STA mode, returns true if you are connected to a WiFi access point and have a valid IP address, otherwise returns false. 
- In AP mode, returns true when the site is connected, otherwise returns false. 



.. method::  WLAN.ifconfig([(ip, subnet, gateway, dns)])


Without parameters, a 4-tuple is returned (ip, subnet_mask, gateway, DNS_server)。

- ``ip``：IP address
- ``subnet_mask``：Subnet Mask
- ``gateway``: Gateway
- ``DNS_server``：DNS Server


With parameters, configure static IP. For example::

  wlan.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))



.. method:: wlan.config('param')
.. method:: wlan.config(param=value, ...)

Gets or sets general network interface parameters. These methods allow other parameters that exceed the standard IP configuration（as  ``wlan.ifconfig()`` ）。 
These include network and hardware specific parameters. For setting parameters, keyword parameter syntax should be used, and multiple parameters can be set at once.

  =========  ===========
  mac        MAC address (bytes)
  essid      WiFi access point name (string)
  channel    WiFi channel (integer)
  hidden     Whether ESSID is hidden (boolean)
  authmode   Authentication mode supported (enumeration, see module constants)
  password   Access password (string)
  =========  ===========



For queries, the parameter name should be referenced as a string, and only one parameter can be queried::

  # Set WiFi access point name (formally known as ESSID) and WiFi channel
  ap.config(essid='My AP', channel=11)
  # Queey params one by one
  print(ap.config('essid'))
  print(ap.config('channel'))

  Following are commonly supported parameters (availability of a specific parameter
  depends on network technology type, driver, and MicroPython port).







For examples
------------



STA mode, access to WiFi network::

  import network

  SSID = "yourSSID"                  #WiFi ID
  PASSWORD = "yourPASSWD"            #WiFi Password

  wlan = network.WLAN(network.STA_IF)  #Create WLAN object
  wlan.active(True)                  #Interface Activation
  wlan.scan()                        #Scan access point
  wlan.isconnected()                 #Check if the site is connected to the AP
  wlan.connect(SSID, PASSWORD)       #Connected to AP
  wlan.config('mac')                 #Obtain the MAC adddress interface
  wlan.ifconfig()                    #Obtain the interface address of IP/netmask/gw/DNS



HOt Spot mode::

  import network

  ap = network.WLAN(network.AP_IF)     #Create access point interface
  ap.active(True)                      #Interface Activation
  ap.config(essid='micropython',password=b"micropython",channel=11,authmode=network.AUTH_WPA_WPA2_PSK)  #Set up an access point



