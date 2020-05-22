:mod:`ubluetooth` --- Bluetooth Low Energy
=========================================

.. module:: ubluetooth
   :synopsis: BLE wireless function

The module provides Bluetooth Low Energy control interface. Currently, it supports BLE in central, peripheral, broadcast and observer roles, and the device can run in multiple roles simultaneously. 

This API is designed to match the BLE protocol and provides building blocks for more advanced abstractions (such as specific device types). 

.. note:: The module is still under development and its classes, functions, methods and constants may change. 


BLE Class
---------

Construct
-----------

.. class:: BLE()

    Returns BLE Object

Configure
-------------

.. method:: BLE.active([active])

    （Optional）Change the active state of the BLE wireless and return to the current state. 

    Before using any other method of this class, the radio to be at active state.

.. method:: BLE.config('param')
            BLE.config(param=value, ...)

    Obtain or set the configuration value of the BLE interface. In order to obtain a value, parameter names should be quoted in strings, and only one parameter is queried at a time. To set the value, use the keyword syntax, you can set one or more parameters at a time. 

    The current supported values are:

    - ``'mac'``: Returns the device MAC address. If the device has a fixed address (such as PYBD), it is returned. Otherwise (such as ESP32), when the BLE interface is active, a random address will be generated.

    - ``'rxbuf'``: Set the size (in bytes) of the internal buffer used to store incoming events. This buffer is a global buffer for the entire BLE driver, so it can handle incoming data for all events (including all characteristics). Increasing this value can better handle bursts of incoming data (for example, scan results) and enable the central device to receive larger feature values. 

Event Handler
--------------

.. method:: BLE.irq(handler, trigger=0xffff)

    Register callbacks for events in the BLE stack. The handler receives two parameters, ``event`` (See the event code below) and  ``data`` (Is a specific event tuple of values).

    The optional *trigger* parameter allows you to set a mask for events of interest to the program. The default is all events.

   

    Note:  The items in the ``addr``, ``adv_data`` and ``uuid``  uples are referenced data management :mod:`ubluetooth` module (i.e. the same instance will be reused multiple times to the event handler). 
    If your program wants to use this data outside of the handler, it must first copy them, for example using ``bytes(addr)`` or ``bluetooth.UUID(uuid)`` .

    An event handler displays all possible events::

        def bt_irq(event, data):
            if event == _IRQ_CENTRAL_CONNECT:
                # The central device is already connected to this peripheral device
                conn_handle, addr_type, addr = data
            elif event == _IRQ_CENTRAL_DISCONNECT:
                # The central device has been disconnected from this peripheral device
                conn_handle, addr_type, addr = data
            elif event == _IRQ_GATTS_WRITE:
                # The central device has written this feature or descriptor
                conn_handle, attr_handle = data
            elif event == _IRQ_GATTS_READ_REQUEST:
                # The central device has issued a read request. Note: This is a hardware IRQ
                # Return NONE to reject the read operation
                # Note: This event does not support ESP32.
                conn_handle, attr_handle = data
            elif event == _IRQ_SCAN_RESULT:
                # The result of a scan
                addr_type, addr, connectable, rssi, adv_data = data
            elif event == _IRQ_SCAN_COMPLETE:
                # Scan duration has been completed or manually stopped
                pass
            elif event == _IRQ_PERIPHERAL_CONNECT:
                #  gap_connect() connected
                conn_handle, addr_type, addr = data
            elif event == _IRQ_PERIPHERAL_DISCONNECT:
                # Connected peripherals are disconnected
                conn_handle, addr_type, addr = data
            elif event == _IRQ_GATTC_SERVICE_RESULT:
                # Call gattc_discover_services() for each service found
                conn_handle, start_handle, end_handle, uuid = data
            elif event == _IRQ_GATTC_CHARACTERISTIC_RESULT:
                # Call gattc_discover_services() every feature found
                conn_handle, def_handle, value_handle, properties, uuid = data
            elif event == _IRQ_GATTC_DESCRIPTOR_RESULT:
                # Call gattc_discover_descriptors() every descriptor found
                conn_handle, dsc_handle, uuid = data
            elif event == _IRQ_GATTC_READ_RESULT:
                # gattc_read() completed
                conn_handle, value_handle, char_data = data
            elif event == _IRQ_GATTC_WRITE_STATUS:
                # gattc_write() completed
                conn_handle, value_handle, status = data
            elif event == _IRQ_GATTC_NOTIFY:
                # The peripheral device has issued a notification request
                conn_handle, value_handle, notify_data = data
            elif event == _IRQ_GATTC_INDICATE:
                # Peripheral equipment issues instructions
                conn_handle, value_handle, notify_data = data

Event code::

    from micropython import const
    _IRQ_CENTRAL_CONNECT                 = const(1 << 0)
    _IRQ_CENTRAL_DISCONNECT              = const(1 << 1)
    _IRQ_GATTS_WRITE                     = const(1 << 2)
    _IRQ_GATTS_READ_REQUEST              = const(1 << 3)
    _IRQ_SCAN_RESULT                     = const(1 << 4)
    _IRQ_SCAN_COMPLETE                   = const(1 << 5)
    _IRQ_PERIPHERAL_CONNECT              = const(1 << 6)
    _IRQ_PERIPHERAL_DISCONNECT           = const(1 << 7)
    _IRQ_GATTC_SERVICE_RESULT            = const(1 << 8)
    _IRQ_GATTC_CHARACTERISTIC_RESULT     = const(1 << 9)
    _IRQ_GATTC_DESCRIPTOR_RESULT         = const(1 << 10)
    _IRQ_GATTC_READ_RESULT               = const(1 << 11)
    _IRQ_GATTC_WRITE_STATUS              = const(1 << 12)
    _IRQ_GATTC_NOTIFY                    = const(1 << 13)
    _IRQ_GATTC_INDICATE                  = const(1 << 14)


To save space in the firmware, these constants are not included in :mod:`ubluetooth` . Add what you need from the above list to your program. 


Advertiser
-----------------------------

.. method:: BLE.gap_advertise(interval_us, adv_data=None, resp_data=None, connectable=True)

    Start broadcasting at the specified time interval (in microseconds). This interval will be rounded to the nearest 625 microseconds. To stop broadcasting, set `interval_us` to NONE.

    *adv_data* and *resp_data* can be any  `buffer` type (such as  ``bytes``, ``bytearray``, ``str``)。
    *adv_data*  is included in all broadcasts and *resp_data* 以is sent in response to a valid scan.
 

    Note：If *adv_data* （or *resp_data* ）is NONE, Then the data passed to the previous call ``gap_advertise`` will be reused.
    In this way, the broadcaster can use to resume the broadcast ``gap_advertise(interval_us)`` . In order to clear the broadcast load, pass an empty bytes, that is b'' .

Scanner
-----------------------

.. method:: BLE.gap_scan(duration_ms, [interval_us], [window_us])

    Run a scan operation that lasts for a specified time (in milliseconds).

   To scan indefinitely, set *duration_ms* to ``0`` . To stop scanning, set *duration_ms* to ``None`` .
    
    Use *interval_us* and *window_us* to choose to configure the duty cycle.
    The scanner will run once every microsecond *window_us* microseconds for a total duration of milliseconds. The default interval and window are 1.28 seconds and 11.25 milliseconds, respectively.

    For each scan result, *_IRQ_SCAN_RESULT* will raise the event. 

    When the scan is stopped (due to the end of the duration or an explicit stop), *_IRQ_SCAN_COMPLETE* will raise the event.



GATT Server
-----------------------------

BLE gatt have a set of registration services. Each service may contain features, and each feature has a value. Features can also contain descriptors, which themselves have values.

These values are stored locally and accessed through the “value handle” generated during the service registration process. 
In addition, the peripheral device can “notify” the feature to the connected central device through the connection handle. 

The default feature and descriptor maximum is 20 bytes. Anything written to them by the central device will be truncated to this length. However, any local write operation will increase the maximum size.
So if you want to write longer data, please use  ``gatts_write`` . Such as , gatts_write(char_handle, bytes(100))


.. method:: BLE.gatts_register_services(services_definition)

    Configure peripheral devices with specified services to replace all existing services. 

    *services_definition* is a list of services, where each service is a binary tuple containing a UUID and feature list.

    Each feature is a 2 or 3 element tuple containing `UUID`，`flags` value and an optional descriptor list.

    Each descriptor is a binary tuple containing UUID and a flags value.

    flags is a bitwise or combined :data:`ubluetooth.FLAG_READ`，:data:`ubluetooth.FLAG_WRITE` and :data:`ubluetooth.FLAG_NOTIFY` . as defined below:

    The return value is a list of tuples (one element per service) (each element is a value handle). Features and descriptor handles are flattened into the same tuple in the defined order.



    Examples of registers of two services (Heart Rate, and Nordic UART)::

        HR_UUID = bluetooth.UUID(0x180D)
        HR_CHAR = (bluetooth.UUID(0x2A37), bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY,)
        HR_SERVICE = (HR_UUID, (HR_CHAR,),)
        UART_UUID = bluetooth.UUID('6E400001-B5A3-F393-E0A9-E50E24DCCA9E')
        UART_TX = (bluetooth.UUID('6E400003-B5A3-F393-E0A9-E50E24DCCA9E'), bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY,)
        UART_RX = (bluetooth.UUID('6E400002-B5A3-F393-E0A9-E50E24DCCA9E'), bluetooth.FLAG_WRITE,)
        UART_SERVICE = (UART_UUID, (UART_TX, UART_RX,),)
        SERVICES = (HR_SERVICE, UART_SERVICE,)
        ( (hr,), (tx, rx,), ) = bt.gatts_register_services(SERVICES)

    These three value handles (``hr``, ``tx``, ``rx``) can be used with :meth:`gatts_read <BLE.gatts_read>`, :meth:`gatts_write <BLE.gatts_write>`,
    and :meth:`gatts_notify <BLE.gatts_notify>` 。

    Note：To stop advertising, then registering for the service.

.. method:: BLE.gatts_read(value_handle)

    Read local value handle (the value is determined by :meth:`gatts_write <BLE.gatts_write>`  or write by remote central device).

.. method:: BLE.gatts_write(value_handle, data)

    Write a local value handle, the value can be read by the central device.


.. method:: BLE.gatts_notify(conn_handle, value_handle, [data])

    Notify the connected central device that this value has changed, and should issue a reading of the current value of this peripheral.

    If data is specified, the value is sent to the central device as part of the notification, thereby avoiding the need for a separate read request. Please note that this will not update the stored local value.


.. method:: BLE.gatts_set_buffer(value_handle, len, append=False)


    Set internal buffer size (in bytes). This will limit the maximum value that can be received. The default value is 20.
    Setting ``append`` to `True` will append all remote writes to the current value instead of replacing the current value. This can buffer up to len bytes.
    Upon using :meth:`gatts_read <BLE.gatts_read>` ，the value will be cleared after reading. This feature is useful when implementing something, such as Nordic UART service。



GATT Client

--------------------------

.. method:: BLE.gap_connect(addr_type, addr, scan_duration_ms=2000)

    Successfully connected to peripheral devices, the ``_IRQ_PERIPHERAL_CONNECT`` event will be triggered.

.. method:: BLE.gap_disconnect(conn_handle)

    Upon successfully disconnect the specified connection handle, the ``_IRQ_PERIPHERAL_DISCONNECT`` event will be triggered.
    If the connection handle is not connected, return  ``False`` , otherwise return ``True`` .


.. method:: BLE.gattc_discover_services(conn_handle)

    Query services of connected peripheral devices.

    For each service discovered, the ``_IRQ_GATTC_SERVICE_RESULT`` event will be triggered.

.. method:: BLE.gattc_discover_characteristics(conn_handle, start_handle, end_handle)

    Query the characteristics within the specified range on the connected peripheral device.
    
    Every time a feature is found, the  ``_IRQ_GATTC_CHARACTERISTIC_RESULT``  event will be triggered.


.. method:: BLE.gattc_discover_descriptors(conn_handle, start_handle, end_handle)

    Query the descriptors in the specified range in the connected peripheral device.

    Every time a feature is found, the ``_IRQ_GATTC_DESCRIPTOR_RESULT`` event will be triggered.


.. method:: BLE.gattc_read(conn_handle, value_handle)

    Send a remote read to the connected peripheral device to obtain the specified characteristic or descriptor handle.

    If successfully, the ``_IRQ_GATTC_READ_RESULT`` event will be triggered.

.. method:: BLE.gattc_write(conn_handle, value_handle, data, mode=0)

    Send a remote write operation to the connected peripheral device for the specified feature or descriptor handle.

    - ``mode``

        -  ``mode=0`` (Default) is an unresponsive write operation：The write operation will be sent to the remote peripheral device, but no confirmation message will be returned, and no event will be raised.
        -  ``mode=1``  i is the response write：Request a remote peripheral device to send a response / acknowledgement that it has received data.

    If a response is received from a remote peripheral device，the ``_IRQ_GATTC_WRITE_STATUS`` event will be triggered.


UUID class
----------

Create
-----------

.. class:: UUID(value)

    Create a UUID instance with the specified value。

    The value can be：

    - A 16-bit integer. For example ``0x2908``.
    - 128-bit UUID string. Such as  ``'6E400001-B5A3-F393-E0A9-E50E24DCCA9E'``.


Constant
---------

.. data:: ubluetooth.FLAG_READ
          ubluetooth.FLAG_WRITE
          ubluetooth.FLAG_NOTIFY


.. literalinclude:: /../../examples/ble/ble_advertising.py
    :caption: ble_advertising.py(BLE advertising)
    :linenos:


.. literalinclude:: /../../examples/ble/ble_temperature.py
    :caption: This example demonstrates a simple temperature sensor peripheral
    :linenos:
