
.. _mpython.py:

.. module:: mpython
   :synopsis: 掌控板板载相关功能函数

:mod:`mpython` --- 掌控板板载相关功能函数
==========================

``mpython`` 是基于掌控板封装的专有模块,内含掌控板板载资源相关功能函数。 详细代码实现可查阅 :ref:`mpython.py源码 <mpython_code>` 。

延时
-------

.. method:: sleep(s)

秒级延时

    - ``s`` -单位秒。

.. method:: sleep_ms(ms)

毫秒级延时

    - ``ms`` -单位毫秒。

.. method:: sleep_us(us)

级延时

    - ``us`` -单位微秒。


映射
-------

.. method:: numberMap(inputNum,bMin,bMax,cMin,cMax)

映射函数，参数：

- ``inputNum`` 为需要映射的变量

- ``bMin`` 为需要映射的最小值

- ``bMax`` 为需要映射的最大值

- ``cMin`` 为映射的最小值

- ``cMax`` 为映射的最大值



板载传感器
-------

声音、光线
+++++++++

.. method:: light.read()

读取板载光线传感器值，范围0~4095。


.. method:: sound.read()

读取板载麦克风，范围0~4095。


加速度计
+++++++++

通过accelerometer对象，您可以获取3轴加速度计值，单位g。 加速度范围±2g/±4g/±8g/±16g,默认为±2g。

.. method:: accelerometer.get_x()

获取x轴上的加速度测量值，正整数或负整数，具体取决于方向。

.. method:: accelerometer.get_y()

获取y轴上的加速度测量值，正整数或负整数，具体取决于方向。

.. method:: accelerometer.get_z()

获取z轴上的加速度测量值，正整数或负整数，具体取决于方向。

.. method:: accelerometer.set_range(range)

设置加速度范围,在默认,不修改为,范围在±2g。

加速度范围值为以下常量:

    ========================== ========= =================
        常量                       值      定义
        RANGE_2G                   0        范围±2g
        RANGE_4G                   1        范围±4g
        RANGE_8G                   2        范围±8g
        RANGE_16G                  3        范围±16g
    ========================== ========= =================


.. method:: accelerometer.set_resolution(resolution)

设置加速度分辨率,默认,不修改为10bit分辨率。

分辨率值为以下常量:

    ========================== ========= =================
        常量                       值      定义
        RES_14_BIT                  0      14 bit 分辨率 
        RES_12_BIT                  1      12 bit 分辨率 
        RES_10_BIT                  2      10 bit 分辨率 
    ========================== ========= =================

.. method:: accelerometer.set_offset(x=None, y=None, z=None)

该函数用于校准加速度计的3个轴(x,y,z)的加速值偏差。一般情况下无需校准,只有当遇到加速度偏差较大时修正。
注意,校准数据断电后不会保存。``x`` , ``y`` , ``z`` 为调整偏差值,可修正范围±1g。
掌控板v2.3版本以上，掉电会保存校准数据。

.. method:: accelerometer.roll_pitch_angle()

返回通过加速度计计算得出的欧拉角(横滚角roll、俯仰角pitch)。注意，偏航角(yaw)需要角速度，故无法测得。返回2元组（roll,pitch），单位角度。

假定，掌控板为飞机：

- 横滚角指飞机两翼所在的平面与平行线之间的夹角，机体向右滚为正,范围为[-180,180].
- 俯仰角是指机头与水平面的夹角,当飞机平行时则为0,抬头时则为正,范围为[-180,180]

.. Attention:: 只通过3轴加速度计算方式，只适用于静态下，只受重力下的测量。实际中，会受到其他加速度干扰，如震动。

运动侦测事件
~~~~~~~~~~~~~

提供多种平面倾斜、翻转、敲击（类似鼠标点击）、掉落的运动姿态事件。用户可预先设定回调函数，当事件发生后，触发事件回调。
回调函数定义如，function_callback(event)。`event` 参数为对应事件常量。


.. data:: accelerometer.event_tilt_left

向左倾斜

.. data:: accelerometer.event_tilt_right

向右倾斜

.. data:: accelerometer.event_tilt_up

向前倾斜

.. data:: accelerometer.event_tilt_down

向后倾斜


.. data:: accelerometer.event_face_up

正面朝上

.. data:: accelerometer.event_face_down

正面朝下

.. data:: accelerometer.event_single_click

单次敲击，类似鼠标的单击操作。

.. data:: accelerometer.event_single_click

连续敲击两次，类似鼠标的双击操作。

.. data:: accelerometer.event_freefall

坠落

event事件定义如下:

    ================================== ========= 
        事件                              值     
        accelerometer.TILT_LEFT           0      
        accelerometer.TILT_RIGHT          1    
        accelerometer.TILT_UP             2    
        accelerometer.TILT_DOWN           3   
        accelerometer.FACE_UP             4     
        accelerometer.FACE_DOWN           5   
        accelerometer.SINGLE_CLICK        6    
        accelerometer.DOUBLE_CLICK        7     
        accelerometer.FREEFALL            8    
    ================================== =========

.. Attention:: 掌控板v2.3版本以上,去除加速度计运动侦测事件

.. literalinclude:: /../../examples/accelerometer/accelerometer_event.py
    :caption: accelerometer 事件的简单应用
    :linenos:

gyroscope
-----------------

通过gyroscope对象，您可以获取陀螺仪角速度值，角速度的单位是dps(°/S)。 
角速度范围±16dps/±32dps/±64dps/±128dps/±256dps/±512dps/±1024dps/±2048dps ,默认为±256 dps。

.. method:: gyroscope.get_x()

获取x轴上的角速度测量值，具体取决于方向。

.. method:: gyroscope.get_y()

获取y轴上的角速度测量值，具体取决于方向。

.. method:: gyroscope.get_z()

获取z轴上的角速度测量值，具体取决于方向。

.. method:: gyroscope.set_range(range)
设置角速度范围,默认不修改为,范围在±256 dps。

角速度范围值为以下常量:

    ========================== ========= =================
        常量                       值          定义
        RANGE_16_DPS               0         范围±16 dps
        RANGE_32_DPS               16        范围±32 dps
        RANGE_64_DPS               32        范围±64 dps
        RANGE_128_DPS              48        范围±128 dps
        RANGE_256_DPS              64        范围±256 dps
        RANGE_512_DPS              80        范围±512 dps
        RANGE_1024_DPS             96        范围±1024 dps
        RANGE_2048_DPS             112       范围±2048 dps
    ========================== ========= =================

.. method:: gyroscope.set_offset(x=None, y=None, z=None)

该函数用于校准陀螺仪的3个轴(x,y,z)的角速值偏差。一般情况下无需校准,只有当遇到角速度偏差较大时修正。
``x`` , ``y`` , ``z`` 为调整偏差值,可修正范围±1024dps。    

.. Attention:: 掌控板v2.3版本以上加入陀螺仪传感器


magnetic
-----------
MMC5983MA磁力计函数接口,可获取3轴地磁感应强度、地磁场强度、获取电子罗盘角度。

.. Attention:: 掌控板v2.0版本以上,才有MMC5983MA磁力计！

.. method:: magnetic.get_x()

获取x轴的磁感应值,正整数或负整数,范围±8191,单位mG(毫高斯)。

.. method:: magnetic.get_y()

获取y轴的磁感应值,正整数或负整数,范围±8191,单位mG(毫高斯)。

.. method:: magnetic.get_z()

获取z轴的磁感应值,正整数或负整数,范围±8191,单位mG(毫高斯)。

.. method:: magnetic.get_field_strength()

返回计算后的磁感应值,即3轴磁力的和。计算公式,x^2+y^2+z^2的平方根。

.. method:: magnetic.peeling()

磁力去皮。类似电子秤去皮功能, ``peeling()`` 后,下次 ``get_field_strength()`` 返回的值为减去当前磁力值后计算得出的结果。可用于去除地磁感应值的测量应用。 

.. method:: magnetic.clear_peeling()

磁力去皮功能取消。使用 ``peeling()`` 后,可用该函数,恢复正常地磁测量。

.. method:: magnetic.get_heading()

获取电子罗盘角度,即改方向与地磁北极的夹角,掌控板的正上方,即USB位置视为正北方。单位角度,范围0~360。

.. Attention:: 由于在角度计算并没有做z轴的倾斜补偿,在使用 ``get_heading()`` 读取罗盘角度时,掌控板应保持水平放置！

.. Attention:: 如需得到精准的罗盘角度,请确保周边无强磁场干扰或在使用前 ``calibrate()`` 校准。

.. method:: magnetic.calibrate()

电子罗盘校准。当掌控板周边存在强磁干扰,可使用该函数清除强磁分量,才能计算准确的地磁北偏角。注意,断电后不保存校准偏移值。

校准方法,按照掌控板显示屏指示步骤操作:

    1. 掌控板水平放置,在水平面旋转数圈,过程约15秒。
    2. 掌控板垂直放置,沿着垂直于地面轴旋转数圈,过程约15秒。


.. literalinclude:: /../../examples/magnetic/compass.py
    :caption: 磁力计应用--指北针
    :linenos:


bme280
-------

BME280是一款集成温度、湿度、气压，三位一体的环境传感器。具有高精度，多功能，小尺寸等特点。

* 温度检测范围：-40℃~+85℃，分辨率0.1℃，误差±0.5℃
* 湿度检测范围：0~100%RH，分辨率0.1%RH，误差±2%RH
* 压力检测范围：300~1100hPa
* 湿度测量响应时间：1s

.. Attention:: 

    掌控板没有集成BME280传感器,掌控板会扫描I2C总线是否存在0x77(119)I2C设备,确定是否构建bme280对象!

.. method:: bme280.temperature()

返回温度值,单位摄氏度。

.. method:: bme280.pressure()

返回大气压值,单位Pa。

.. method:: bme280.humidity()

返回环境湿度,单位%。


蜂鸣器
-------

由 ``music`` 模块驱动掌控板蜂鸣器,具体操作详见 :mod:`music` 模块。


button_[a,b]对象
------

掌控板上的a,b按键。button_a/button_b 是 ``Button`` 类的实例对象。使用 :ref:`machine.Pin.irq<Pin.irq>` 中断实现。定义了
``event_pressed`` 和 ``event_released`` 按键按下、释放事件。 用户可轻易的实现事件回调。除此外，还实现当前或过去按键状态、按键次数等函数方法。

.. class:: Button(pin_num, reverse=False)

Button类，按键抽象类。

    - ``pin_num`` - IO引脚号
    - ``reverse`` - 默认为reverse为False。适用于触发为低电平按键。如是触发为高电平按键，将reverse设为True，翻转下。

掌控板上button_a、button_b的实例::

    button_a = Button(Pin.P5)
    button_b = Button(Pin.P11)


当按键事件发生，触发事件回调。回调函数定义如，function_callback(pin), ``pin`` 为该引脚的machine.Pin对象返回。

.. data:: Button.event_pressed

按键按下事件。

.. data:: Button.event_released

按键释放事件。


.. literalinclude:: /../../examples/button/button_event.py
    :caption: Button 事件回调的简单应用
    :linenos:



.. method:: Button.value()

获取按键引脚电平状态。1为高电平，0位低电平。

::

    >>> button_a.value()
    >>> 1
    >>> button_a.value()
    >>> 0


.. method:: Button.is_pressed()

返回当前是否按住。 ``True`` 表示按键按下，``False`` 则未按下。

.. method:: Button.was_pressed()

返回 ``True`` 或 ``False`` 指示自设备启动以来或上次调用此方法以来是否按下按钮。调用此方法将清除按下状态，因此必须再次按下按钮，然后才能再次返回 ``True`` 。

.. method:: Button.get_presses()

返回按键的按下总数，并在返回之前将该总数重置为零。注意，计数器超过100将不再计数。


.. _button.irq:

.. method:: Button.irq(handler=None, trigger=(Pin.IRQ_FALLING | Pin.IRQ_RISING), priority=1, wake=None)

配置在引脚的触发源处于活动状态时调用的中断处理程序。用法与 machine.Pin.irq 一样。

参数:

     - ``handler`` 是一个可选的函数，在中断触发时调用。

     - ``trigger`` 配置可以触发中断的事件。可能的值是：

       - ``Pin.IRQ_FALLING`` 下降沿中断
       - ``Pin.IRQ_RISING`` 上升沿中断
       - ``Pin.IRQ_LOW_LEVEL`` 低电平中断
       - ``Pin.IRQ_HIGH_LEVEL`` 高电平中断

       这些值可以一起进行 ``OR`` 运算以触发多个事件。

     - ``priority`` 设置中断的优先级。它可以采用的值是特定于端口的，但是更高的值总是代表更高的优先级。

     - ``wake`` 选择此中断可唤醒系统的电源模式。它可以是 ``machine.IDLE`` ， ``machine.SLEEP`` 或 ``machine.DEEPSLEEP`` 。
     这些值也可以进行 ``OR`` 运算，使引脚在多种功耗模式下产生中断。

此方法返回一个回调对象。

::

    >>> from mpython import *
    >>> button_a.irq(trigger=Pin.IRQ_FALLING, handler=lambda p:print("button-a press！")) 


touch对象
------
掌控板上共有6个触摸引脚分别touchpad_p/y/t/h/o/n。是Touch类的实例对象，具体包含函数方法如下。


.. class:: Touch(pin)


.. data:: Touch.event_pressed

触摸按键按下事件。当按键事件发生，触发事件回调。回调函数定义如，function_callback(value), ``value`` 为该触摸按键的状态值。

.. data:: Touch.event_released

触摸按键释放事件。

.. method:: Touch.read()

返回触摸值

. method:: Touch.config(threshold)

触摸阈值设置

.. method:: Touch.is_pressed()

返回当前是否按住。 ``True`` 表示按键按下，``False`` 则未按下。

.. method:: Touch.was_pressed()

返回 ``True`` 或 ``False`` 指示自设备启动以来或上次调用此方法以来是否按下按钮。调用此方法将清除按下状态，因此必须再次按下按钮，然后才能再次返回 ``True`` 。

.. method:: Touch.get_presses()

返回按键的按下总数，并在返回之前将该总数重置为零。注意，计数器超过100将不再计数。

rgb对象
-------
用于控制掌控板的3颗RGB ws2812灯珠。rgb对象为neopixel的衍生类，继承neopixel的方法。更多的使用方法请查阅 :ref:`neopixel<neopixel>` 。 

.. method:: rgb.write()

把数据写入RGB灯珠中。 

.. Hint::

    通过给rgb[n]列表赋值来写入RGB颜色值。如，rgb[0]=(50,0,0)

::

    from mpython import *

    rgb[0] = (255, 0, 0)  # 设置为红色，全亮度
    rgb[1] = (0, 128, 0)  # 设定为绿色，半亮度
    rgb[2] = (0, 0, 64)   # 设置为蓝色，四分之一亮度

    rgb.write()

.. method:: rgb.fill(rgb_buf)

填充所有LED像素。

.. method:: rgb.brightness(brightness)

亮度调节,范围0~1.0


.. _oled:

oled对象
-------
oled对象为framebuf的衍生类，继承framebuf的方法。更多的使用方法请查阅 :mod:`framebuf<framebuf>` 。 

.. method:: oled.poweron()

开启显示屏电源。

.. method:: oled.poweroff()

关闭显示器电源。

.. method:: oled.contrast(brightness)

设置显示屏亮度。

    - ``brightness`` 亮度,范围0~255


.. method:: oled.invert(n)

翻转像素点。当n=1时,未填充像素点点亮,填充像素点灭。当n=0时,则反。默认启动是填充像素点点亮。

.. method:: oled.DispChar(s, x, y,mode=TextMode.normal,auto_return=False)

oled屏显示文本。采用 `Google Noto Sans CJK <http://www.google.cn/get/noto/help/cjk/>`_ 开源无衬线字体字体。字体高度16像素点,支持英文,简体中文繁体中文，日文和韩文语言。

返回(字符总像素点宽度,续接显示的x,y坐标)的二元组。

    - ``s`` -需要显示的文本。
    - ``x`` 、``y`` -文本的左上角作为起点坐标。
    - ``mode`` - 设置文本模式,默认为TextMode.normal

        - ``TextMode.normal`` - 等于1 。普通模式,文本显示白色,背景为黑色。
        - ``TextMode.rev`` - 等于2 。反转模式,文本显示黑色,背景为白色。
        - ``TextMode.trans`` - 等于3 。透明模式,透明文本意味着文本被写在显示中已经可见的内容之上。不同之处在于，以前屏幕上的内容仍然可以看到，而对于normal，背景将被当前选择的背景颜色所替代。
        - ``TextMode.xor`` - 等于4 。XOR模式,如果背景是黑色的，效果与默认模式(normal模式)相同。如果背景为白色，则反转文本。
    - ``auto_return`` - 自动换行,当显示字符串超出显示屏宽度可自动换行。默认不换行。

.. method:: oled.show()

将frame缓存发送至oled显示。

.. literalinclude:: /../../examples/display/helloworld.py
    :caption: hello world
    :linenos:

.. literalinclude:: /../../examples/display/oled_effect of typing.py
    :caption: 打字效果
    :linenos:


.. method:: oled.DispChar_font(font, s, x, y, invert=False)

自定义字体显示。用户可根据自己需求,在PC端将 `otf` 、 `ttf` 标准字体文件通过Python脚本 `font_to_py.py <https://github.com/peterhinch/micropython-font-to-py/blob/master/font_to_py.py>`_ 转为输出含字体Bitmap的python源码,调用使用。
返回(字符总像素点宽度,续接显示的x,y坐标)的二元组。

    - ``font`` - 字体对象。`font_to_py.py` 脚本转换得到的Python源码, 放到文件系统中,注意,在使用函数前须导入font文件。   
    - ``s`` - 显示的字符串
    - ``x`` 、 ``y`` - 文本的左上角作为起点坐标。
    - ``invert`` - 显示像素点翻转。




.. literalinclude:: /../../examples/display/custom_font/main.py
    :caption: 自定义字体显示
    :linenos:

* :download:`以上自定义字体示例中simfang16、freescpt18、stxingkai20<https://github.com/labplus-cn/mpython-docs/tree/master/examples/display/custom_font>`

.. figure:: /../images/tutorials/helloworld_customfont.jpg
    :width: 400px
    :align: center

.. admonition:: `font_to_py.py` 脚本使用说明

    - 该脚本要Python 3.2或更高版本运行环境。依赖 `freetype` python包。安装方法, `pip3 install freetype-py`  
    - 默认情况下，只转换ASCII字符集（ `chr(32)` 到 `chr(126)` 字符）。通过命令行参数 `-c`,根据需要修改此范围，以指定任意的Unicode字符集,可以定义非英语和非连续字符集。
    - `oled.DispChar_font()` 函数只支持hmap水平映射的字体,所以在转换时,需要使用命令行参数 `-x` 固定转换为水平映射。
    - 固件参数。字体文件路径、转换后的字体高度、输出文件路径。例如: font_to_py.py FreeSans.ttf 20 myfont.py

在PC端使用font_to_py.py脚本转换字体::

    # 转换高度为16像素只包含ASCII字符集
    font_to_py.py -x FreeSans.ttf 16 myfont.py

    # 转换高度为16像素指定Unicode字符集,-c参数后面为你指定的字符集
    font_to_py.py -x simfang.ttf 16 simfang.py -c  ¬!"#£$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~°Ωαβγδθλμπωϕ£


该函数功能实现,参考来源于 `peterhinch/micropython-font-to <https://github.com/peterhinch/micropython-font-to-py>`_ 开源项目,更详细有关 `font_to_py.py` 详细使用说明,可到此项目获取更多资料。


.. method:: oled.fill(c)

        用指定的颜色填充整个帧缓存。 ``c`` 为1时,像素点亮；``c`` 为0时,像素点灭。

.. method:: oled.circle(x, y, radius , c)

绘制圆

    - ``x`` 、``y`` -左上角作为起点坐标。
    - ``radius`` -圆半径大小
    - ``c`` -为1时,像素点亮；``c`` 为0时,像素点灭。

.. method:: oled.fill_circle(x, y, radius , c)

绘制实心圆

    - ``x`` 、``y`` -左上角作为起点坐标。
    - ``radius`` -圆半径大小
    - ``c`` -为1时,像素点亮；``c`` 为0时,像素点灭。

.. method:: oled.triangle(x0, y0, x1, y1, x2, y2, c)

绘制三角形

    - ``x0`` 、``y0`` -三角形上顶点坐标 。
    - ``x1`` 、``y1`` -三角形左顶点坐标 。
    - ``x2`` 、``y2`` -三角形左顶点坐标 。
    - ``c`` -为1时,像素点亮；``c`` 为0时,像素点灭。

.. method:: oled.fill_triangle(x0, y0, x1, y1, x2, y2, c)

绘制实心三角形

    - ``x0`` 、``y0`` -三角形上顶点坐标 。
    - ``x1`` 、``y1`` -三角形左顶点坐标 。
    - ``x2`` 、``y2`` -三角形左顶点坐标 。
    - ``c`` -为1时,像素点亮；``c`` 为0时,像素点灭。


.. method:: oled.bitmap(x, y, bitmap, w, h,c)

绘制bitmap图案

    - ``x`` 、``y`` -左上角作为起点坐标
    - ``bitmap`` -图案bitmap 的btyearray字节数组
    - ``w`` -图案宽度
    - ``h`` -图案高度
    - ``c`` -为1时,像素点亮;


.. method:: oled.RoundRect( x, y, w, h, r, c)

绘制弧角矩形

    - ``x`` 、``y`` -左上角作为起点坐标
    - ``w`` -图案宽度
    - ``h`` -图案高度
    - ``r`` -圆弧角半径
    - ``c`` -为1时,像素点亮；``c`` 为0时,像素点灭。

i2c对象
-------

mPython掌控板已实例 ``I2C`` 类，P19、P20 为I2C的SCL、SDA引脚。I2C设备可连接掌控板I2C总线进行操作。


详细有关I2C的读写操作，请查看 :ref:`machine.I2C<machine.I2C>` 模块或 :ref:`I2C基础教程<tutorials_i2c>` 章节。

MPythonPin类
-------

.. class:: MPythonPin(pin, mode=PinMode.IN,pull=None)

构建Pin对象

- ``pin`` 掌控板定义引脚号，具体定义看查看 :ref:`掌控板引脚定义<mpython_pinout>` 。

- ``mode`` 引脚模式。未设定时,默认 `mode` = `PinMode.IN`

        - ``PinMode.IN`` 等于1，数字输入模式
        - ``PinMode.OUT`` 等于2，数字输出模式
        - ``PinMode.PWM`` 等于3，模拟输出模式
        - ``PinMode.ANALOG`` 等于4，模拟输入模式
        - ``PinMode.OUT_DRAIN`` 等于5，开漏输出模式

- ``pull`` 指定引脚是否连接了电阻，可以是以下之一：

       - ``None`` - 无上拉或下拉电阻
       - ``Pin.PULL_UP`` - 上拉电阻使能
       - ``Pin.PULL_DOWN`` - 下拉电阻使能


示例::

        >>> from mpython import MPythonPin       #导入MPython模块
        >>> P0=MPythonPin(0,PinMode.IN)          #构建引脚0对象，设置数字输入模式



.. method:: MPythonPin.read_digital()

返回该IO引脚电平值。1代表高电平，0代表低电平

.. method:: MPythonPin.write_digital(value)

IO引脚输出电平控制。``value`` =1时输出高电平， ``value`` =0时输出低电平。

.. method:: MPythonPin.read_analog()

读取ADC并返回读取结果，返回的值将在0到4095之间。

.. method:: MPythonPin.write_analog(duty, freq=1000):

设置输出PWM信号的占空比。

- ``duty`` 0 ≤ duty ≤ 1023
- ``freq`` PWM波频率,0 < freq ≤ 0x0001312D（十进制：0 < freq ≤ 78125）


.. _MPythonPin.irq:

.. method:: MPythonPin.irq(handler=None, trigger=Pin.IRQ_RISING):

如果引脚模式配置为 ``IN`` ,可配置该引脚的触发源处于活动状态时调用的中断处理程序。

参数:

     - ``handler`` 是一个可选的函数，在中断触发时调用。

     - ``trigger`` 配置可以触发中断的事件。可能的值是：

       - ``Pin.IRQ_FALLING`` 下降沿中断
       - ``Pin.IRQ_RISING`` 上升沿中断
       - ``Pin.IRQ_LOW_LEVEL`` 低电平中断
       - ``Pin.IRQ_HIGH_LEVEL`` 高电平中断

       这些值可以一起进行 ``OR`` 运算以触发多个事件。


.. _mpython.wifi:

wifi类
------

提供便捷的wifi连接网络方式或无线AP功能。注意,开启WiFi功能功耗会增大,如不使用情况下,可关闭WiFi可降低功耗。

.. class:: wifi()

构建wifi对象并会创建 ``sta`` 对象和 ``ap`` 对象。可参见 :mod:`network` 模块了解更多使用方法。

    - sta用于客户端连接路由器来连接网络。
    - ap用于掌控板作为无线AP接入方式。

.. method:: wifi.connectWiFi(ssid,password,timeout=10)

连接wifi网络

    - ``ssid`` -WiFi网络名称
    - ``password`` -WiFi密码
    - ``timeout`` -链接超时,默认10秒

.. method:: wifi.disconnectWiFi()

断开wifi网络连接

.. method:: wifi.enable_APWiFi(essid,password,channel=10)

开启wifi的无线AP模式

 - ``essid`` - 创建WiFi网络名称
 - ``password`` - 密码
 - ``channel`` -设置wifi使用信道,channel 1~13

.. method:: wifi.disable_APWiFi()

关闭无线AP
