:mod:`ubluetooth` --- 低功耗蓝牙
=========================================

.. module:: ubluetooth
   :synopsis: 低功耗蓝牙无线电功能

该模块提供低功耗蓝牙控制接口。当前，它在中央，外围设备，广播和观察者角色中支持蓝牙低功耗（BLE），并且设备可以同时在多个角色中运行。

此API旨在与低功耗蓝牙协议相匹配，并为更高级的抽象(如特定的设备类型)提供构建模块。

.. note:: 该模块仍在开发中，其类，功能，方法和常量可能会发生变化。


BLE 类
---------

构建
-----------

.. class:: BLE()

    返回 BLE 对象

配置
-------------

.. method:: BLE.active([active])

    （可选）更改BLE无线电的活动状态，并返回当前状态。

    在使用此类的任何其他方法之前，必须使无线电处于活动状态。

.. method:: BLE.config('param')
            BLE.config(param=value, ...)

    获取或设置BLE接口的配置值。为了获得一个值，参数名称应该用字符串引号，并且一次只查询一个参数。要设置值，请使用关键字语法，一次可以设置一个或多个参数。

    当前支持的值为:

    - ``'mac'``: 返回设备的MAC地址。如果设备具有固定地址（例如PYBD），则将其返回。否则（例如ESP32），当BLE接口处于活动状态时，将生成一个随机地址。

    - ``'rxbuf'``: 设置用于存储传入事件的内部缓冲区的大小（以字节为单位）。该缓冲区是整个BLE驱动程序的全局缓冲区，因此可以处理所有事件（包括所有特征）的传入数据。增加此值可以更好地处理突发的传入数据（例如，扫描结果），并可以使中央设备接收较大的特征值。

事件处理
--------------

.. method:: BLE.irq(handler, trigger=0xffff)

    为BLE堆栈中的事件注册回调。handler接收两个参数，``event`` （看下文的事件代码）和 ``data`` （其是值的特定事件元组）。

    可选的 *trigger* 参数允许您设置程序感兴趣的事件的掩码。默认值为所有事件。

   

    注:  ``addr``, ``adv_data`` 和 ``uuid``  元组中的项是引用的数据管理 :mod:`ubluetooth` 模块(即相同的实例将被重新使用多次调用到事件处理程序)。
    如果您的程序想在处理程序之外使用此数据，则它必须首先复制它们，例如使用 ``bytes(addr)`` or ``bluetooth.UUID(uuid)`` 。

    一个事件处理程序显示所有可能的事件::

        def bt_irq(event, data):
            if event == _IRQ_CENTRAL_CONNECT:
                # 中央设备已经连接到这个外围设备
                conn_handle, addr_type, addr = data
            elif event == _IRQ_CENTRAL_DISCONNECT:
                # 中央设备已与此外围设备断开
                conn_handle, addr_type, addr = data
            elif event == _IRQ_GATTS_WRITE:
                # 中央设备已写入此特征或描述符
                conn_handle, attr_handle = data
            elif event == _IRQ_GATTS_READ_REQUEST:
                # 中央设备已发出读请求. Note: 这是一个硬件IRQ
                # 返回None来拒绝读操作
                # Note: 这事件不支持 ESP32.
                conn_handle, attr_handle = data
            elif event == _IRQ_SCAN_RESULT:
                # 一次扫描的结果
                addr_type, addr, connectable, rssi, adv_data = data
            elif event == _IRQ_SCAN_COMPLETE:
                # 扫描持续时间已完成或手动停止
                pass
            elif event == _IRQ_PERIPHERAL_CONNECT:
                #  gap_connect()连接成功
                conn_handle, addr_type, addr = data
            elif event == _IRQ_PERIPHERAL_DISCONNECT:
                # 已连接的外围设备已断开
                conn_handle, addr_type, addr = data
            elif event == _IRQ_GATTC_SERVICE_RESULT:
                # 调用gattc_discover_services()找到的每个服务
                conn_handle, start_handle, end_handle, uuid = data
            elif event == _IRQ_GATTC_CHARACTERISTIC_RESULT:
                # 调用gattc_discover_services()找到的每个特征
                conn_handle, def_handle, value_handle, properties, uuid = data
            elif event == _IRQ_GATTC_DESCRIPTOR_RESULT:
                # 调用gattc_discover_descriptors()找到的每个描述符
                conn_handle, dsc_handle, uuid = data
            elif event == _IRQ_GATTC_READ_RESULT:
                # gattc_read() 已完成
                conn_handle, value_handle, char_data = data
            elif event == _IRQ_GATTC_WRITE_STATUS:
                # gattc_write() 已完成
                conn_handle, value_handle, status = data
            elif event == _IRQ_GATTC_NOTIFY:
                # 外围设备已发出通知请求
                conn_handle, value_handle, notify_data = data
            elif event == _IRQ_GATTC_INDICATE:
                #外围设备发出指示请求
                conn_handle, value_handle, notify_data = data

事件代码::

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


为了节省固件中的空间，这些常量不包括在 :mod:`ubluetooth` 。将您需要的从上面的列表中添加到您的程序中。


广播者(Advertiser)
-----------------------------

.. method:: BLE.gap_advertise(interval_us, adv_data=None, resp_data=None, connectable=True)

    以指定的时间间隔（以微秒为单位）开始广播。该间隔将四舍五入到最接近的625微妙。要停止广播，请将 `interval_us` 设置 为None。

    *adv_data* 和 *resp_data* 可以是任何 `buffer` 类型 (例如 ``bytes``, ``bytearray``, ``str``)。
    *adv_data* 包含在所有广播中，并发送 *resp_data* 以应答有效的扫描。
 

    注意：如果 *adv_data* （或 *resp_data* ）为None，则将重用传递到上一个调用的数据 ``gap_advertise`` 。
    这样一来，广播者就可以使用来恢复广播 ``gap_advertise(interval_us)`` 。为了清除广播负载，传递一个空的bytes，即b''。

观察者 (Scanner)
-----------------------

.. method:: BLE.gap_scan(duration_ms, [interval_us], [window_us])

    运行持续指定时间（以毫秒为单位）的扫描操作。

    要无限期扫描，请将 *duration_ms* 设置为 ``0`` 。要停止扫描，请将 *duration_ms* 设置为 ``None`` 。
    
    使用 *interval_us* 和 *window_us* 可以选择配置占空比。
    扫描器将每间隔一微秒运行一次 *window_us* 微秒，总计持续时间为毫秒。默认间隔和窗口分别为1.28秒和11.25毫秒。

    对于每个扫描结果，*_IRQ_SCAN_RESULT* 将引发该事件。

    停止扫描（由于持续时间结束或明确停止）时，*_IRQ_SCAN_COMPLETE* 将引发该事件。



外围设备 (GATT Server)
-----------------------------

BLE外围设备具有一组注册服务。每个服务可能包含特性，每个特性都有一个值。特征也可以包含描述符，描述符本身具有值。

这些值存储在本地，并通过在服务注册过程中生成的“值柄”进行访问。它们也可以被远程的中央设备读取或写入。
此外，外围设备可以通过连接句柄将特征“通知”到已连接的中央设备。

特征和描述符的默认最大为20个字节。任何由中央设备写给它们的都会被截短到这个长度。但是，任何本地写操作都会增加最大大小,
所以，如果你写想更长的数据，请注册后使用 ``gatts_write`` 。例如, gatts_write(char_handle, bytes(100))


.. method:: BLE.gatts_register_services(services_definition)

    使用指定的服务配置外围设备，替换所有现有服务。

    *services_definition* 是一个服务的列表，其中每个服务都是一个包含UUID和特征列表的二元元组。

    每个特征都是一个包含 `UUID`，`flags` 值以及一个可选的描述符列表的2或3元素元组。

    每个描述符是一个包含UUID和一个flags值的二元元组。

    flags是一个按位或组合的 :data:`ubluetooth.FLAG_READ`，:data:`ubluetooth.FLAG_WRITE` 和 :data:`ubluetooth.FLAG_NOTIFY` 。如下文所定义的值:

    返回值是元组的列表（每个服务一个元素）（每个元素是一个值句柄）。特征和描述符句柄按照定义的顺序被展平到相同的元组中。



    以下示例注册了两个服务 (Heart Rate, and Nordic UART)::

        HR_UUID = bluetooth.UUID(0x180D)
        HR_CHAR = (bluetooth.UUID(0x2A37), bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY,)
        HR_SERVICE = (HR_UUID, (HR_CHAR,),)
        UART_UUID = bluetooth.UUID('6E400001-B5A3-F393-E0A9-E50E24DCCA9E')
        UART_TX = (bluetooth.UUID('6E400003-B5A3-F393-E0A9-E50E24DCCA9E'), bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY,)
        UART_RX = (bluetooth.UUID('6E400002-B5A3-F393-E0A9-E50E24DCCA9E'), bluetooth.FLAG_WRITE,)
        UART_SERVICE = (UART_UUID, (UART_TX, UART_RX,),)
        SERVICES = (HR_SERVICE, UART_SERVICE,)
        ( (hr,), (tx, rx,), ) = bt.gatts_register_services(SERVICES)

    这三个值柄(``hr``, ``tx``, ``rx``)可与使用 :meth:`gatts_read <BLE.gatts_read>`, :meth:`gatts_write <BLE.gatts_write>`,
    和 :meth:`gatts_notify <BLE.gatts_notify>` 。

    注意：注册服务之前，必须停止广告。

.. method:: BLE.gatts_read(value_handle)

    读取本地的值柄 (该值由 :meth:`gatts_write <BLE.gatts_write>` 或远程的中央设备写入)。

.. method:: BLE.gatts_write(value_handle, data)

    写入本地的值柄，该值可由中央设备读取。


.. method:: BLE.gatts_notify(conn_handle, value_handle, [data])

    通知连接的中央设备此值已更改，并且应发出此外围设备的当前值的读取值。

    如果指定了数据，则将该值作为通知的一部分发送到中央设备，从而避免了需要单独的读取请求的情况。请注意，这不会更新存储的本地值。


.. method:: BLE.gatts_set_buffer(value_handle, len, append=False)


    设置内部缓冲区大小（以字节为单位）。这将限制可以接收的最大值。默认值为20。
    将 ``append`` 设置为 `True` 会将所有远程写入追加到当前值，而不是替换当前值。这样最多可以缓冲len个字节。
    使用时 :meth:`gatts_read <BLE.gatts_read>` ，将在读取后清除该值。这个功能在实现某些东西时很有用,比如Nordic UART服务。



中央设备 (GATT Client)
--------------------------

.. method:: BLE.gap_connect(addr_type, addr, scan_duration_ms=2000)

    连接到外围设备。成功,将触发 ``_IRQ_PERIPHERAL_CONNECT`` 事件。

.. method:: BLE.gap_disconnect(conn_handle)

    断开指定的连接句柄。成功,将触发 ``_IRQ_PERIPHERAL_DISCONNECT`` 事件。
    如果未连接连接句柄，返回 ``False`` ,否则返回 ``True`` 。


.. method:: BLE.gattc_discover_services(conn_handle)

    查询已连接的外围设备的服务。

    对于发现的每个服务, 会触发 ``_IRQ_GATTC_SERVICE_RESULT`` 事件。

.. method:: BLE.gattc_discover_characteristics(conn_handle, start_handle, end_handle)

    在已连接的外围设备上查询指定范围内的特征。
    每次特征发现,会触发 ``_IRQ_GATTC_CHARACTERISTIC_RESULT`` 事件。


.. method:: BLE.gattc_discover_descriptors(conn_handle, start_handle, end_handle)

    在连接的外围设备中查询指定范围内的描述符。

    每次特征发现,会触发 ``_IRQ_GATTC_DESCRIPTOR_RESULT`` 事件。


.. method:: BLE.gattc_read(conn_handle, value_handle)

    向连接的外围设备发出远程读取，以获取指定的特性或描述符句柄。

    如果成功,会触发 ``_IRQ_GATTC_READ_RESULT`` 事件

.. method:: BLE.gattc_write(conn_handle, value_handle, data, mode=0)

    针对指定的特征或描述符句柄向连接的外围设备发出远程写操作。

    - ``mode``

        -  ``mode=0`` （默认）是无响应写操作：写操作将发送到远程外围设备，但不会返回确认信息，也不会引发任何事件。
        -  ``mode=1`` i是响应写入：请求远程外围设备发送其已接收到数据的响应/确认。

    如果从远程外围设备收到响应，``_IRQ_GATTC_WRITE_STATUS`` 事件将触发。


UUID 类
----------

构建
-----------

.. class:: UUID(value)

    用指定的值创建一个UUID实例。

    该值可以是：

    - 一个16位整数。例如 ``0x2908``.
    - 128位UUID字符串。例如 ``'6E400001-B5A3-F393-E0A9-E50E24DCCA9E'``.


常量
---------

.. data:: ubluetooth.FLAG_READ
          ubluetooth.FLAG_WRITE
          ubluetooth.FLAG_NOTIFY


.. literalinclude:: /../../examples/ble/ble_advertising.py
    :caption: ble_advertising.py(BLE广播)
    :linenos:


.. literalinclude:: /../../examples/ble/ble_temperature.py
    :caption: 这个例子演示了一个简单的温度传感器外设
    :linenos:
