Hardware Overview
====================

The mPython Board is a MicroPython microcontroller board with full support for MicroPython/Python software features.

.. image:: /../images/掌控-立2.png

技术参数
-----------

mPython Board had the following hardware features:

  - ESP-32 microcontroller

    - Processor：Tensilica LX6 dual core microprocessor（one for Handling High Speed Connections and the other for Independent Application Development）
    - Main frequency: up to 240mhz clock frequency
    -	SRAM：520KB
    - Flash：8MB
    - Wi-Fi Standard：FCC/CE/TELEC/KCC
    - Wi-Fi Alliance：802.11 b/g/n/d/e/i/k/r (802.11n，high speed 150 Mbps)，A-MPDU and A-MSDU packed，support 0.4us protective interval
    - Frequency Range：2.4~2.5 GHz
    - BlueTooth Protocol：Comply to BlueTooth 4.2 BR/EDR and BLE standard
    - Bluetooth Audio Streaming：CVSD and SBC audio low power：10uA

  - Power Supply Mode：Micro USB
  - Operating Voltage：3.3V
  - Maximum Operating Current:200mA
  - Maximum Load Current:1000mA
  - mPython Board integrated hardwares

    - 3-axis Accelerometer MSA300, Range: ±2/4/8/16G
    - Deomagnetic Sensor MMC5983MA, Range: ±8 Gauss; Accuracy 0.4mGz, Electronic Compass error ±0.5°
    - Light Sensor
    - Microphone
    - 3x ws2812 LED, RGB
    - 1.3" OLED Panel，support 16*16 characters display，Resolution 128x64
    - Passive Buzzer
    - Supports 2x tact switch (User A/B), 1x Reset Button, 6x Touch Button
    - Supports 1x crocodile clip interface: resistive sensor input

  - Interface for external device expansion

    - 20x digital I/O， (it supports 12x PWM，6x Touch Pad)
    - 5x 12bit ADC，P0~P4  
    - 1x external hardware input via crocodile clip interface :EXT/GND
    - supports I2C、UART、SPI communication protocol


外观规格
--------------

.. image:: /../images/掌控板V2.0-2D图档-20200102-1.png
  :width: 800px

元件布局/引脚定义
--------------

.. figure:: /../images/mPython掌控板_pin_define.jpg
  :width: 800px
  :align: center


.. _mPythonPindesc:

掌控板接口引脚说明
+++++++++++++++++++++++++



=============== ======  ====================================  
 引脚            类型     描述
 P0              I/O     模拟/数字输入,模拟/数字输出,TouchPad
 P1              I/O     模拟/数字输入,模拟/数字输出,TouchPad 
 P2               I      模拟/数字输入
 P3               I      模拟输入,连接掌控板EXT鳄鱼夹,可连接阻性传感器
 P4               I      模拟输入,连接掌控板光线传感器  
 P5              I/O     数字输入,模拟/数字输出, 连接掌控板按键A,neopixel
 P6              I/O     数字输入,模拟/数字输出, 连接掌控板蜂鸣器,不使用蜂鸣器时,可以作为数字IO使用,neopixel
 P7              I/O     数字输入,模拟/数字输出, 连接掌控板RGB LED
 P8              I/O     数字输入,模拟/数字输出,neopixel
 P9              I/O     数字输入,模拟/数字输出,neopixel
 P10              I      模拟输入,连接掌控板声音传感器
 P11             I/O     数字输入,模拟/数字输出, 连接掌控板按键B,neopixel
 P12             I/O     保留
 P13             I/O     数字输入,模拟/数字输出,neopixel
 P14             I/O     数字输入,模拟/数字输出,neopixel
 P15             I/O     数字输入,模拟/数字输出,neopixel
 P16             I/O     数字输入,模拟/数字输出,neopixel
 3V3             POWER   电源正输入:连接USB时,掌控板内部稳压输出3.3V,未连接USB可以通过输入(2.7-3.6)V电压为掌控板供电
 P19             I/O     数字输入,模拟/数字输出，I2C总线SCL,与内部的OLED和加速度传感器共享I2C总线,neopixel
 P20             I/O     数字输入,模拟/数字输出，I2C总线SDA,与内部的OLED和加速度传感器共享I2C总线,neopixel
 GND             GND     电源GND
 Touch_P(P23)    I/O     TouchPad
 Touch_Y(P24)    I/O     TouchPad      
 Touch_T(P25)    I/O     TouchPad
 Touch_H(P26)    I/O     TouchPad
 Touch_O(P27)    I/O     TouchPad  
 Touch_N(P28)    I/O     TouchPad      
=============== ======  ==================================== 


相关下载
--------------

原理图
++++++

* :download:`mPython掌控板V2.0.3原理图 </../datasheet/掌控板-V2.0.3.pdf>`

主要数据手册
++++++++++++++++

* :download:`USB-to-UART Bridge：cp2104 </../datasheet/CP2104-SiliconLaboratories.pdf>`
* :download:`ESP32-WROOM </../datasheet/esp32-wroom-32_datasheet_cn.pdf>`
* :download:`LDO稳压:CE6210 </../datasheet/CE6210.jpg>`
* :download:`加速度计:MSA300 </../datasheet/MSA300-V1.0-ENG.pdf>`
* :download:`地磁传感器:MMC5983MA </../datasheet/MMC5983MA.pdf>`
* :download:`OLED：128x64 </../datasheet/1.30-SPEC QG-2864KSWLG01 VER A.pdf>`

外观规格图
+++++++++++++++++

* :download:`mPython掌控板v2.0外观规格图 </../datasheet/掌控板V2.0-3D-2D图档-20200102.rar>`
