新建板：labplus-Ledong-pro

1. port/boards下新建主控板：labplus_Ledong_pro，从ports/esp32/boards/ESP32_GENERIC_S3下所有文件。

2. 复制micropytnon/ports/esp32/main.c
   修改：
   - 加入屏显示异常代码。
   - 加入蜂鸣器定时器回调函数。
   - 加入停止main.py中用户配置的定时器代码
3. 修改mpconfigboard.h
   mpconfigport.h做了些公用配置，其包含了mpconfigboard.h，用于做板级配置，修改此文件：
   - 加入音乐模块
4. 修改boards/labplus_Ledong_pro/mpconfigboard.cmake
   - 设置目标芯片为s3
      set(IDF_TARGET esp32s3)
   - 修改SDKCONFIG_DEFAULTS变量，添加相关配置
   - 添加一些路径变量
   - 添加待编译的文件及路径变量
   - 设置manifest.py路径
5. 修改sdkconfig.board
   配置flash、分区表位置什么的。
6. 修改sdkconfig.usb
   配置CONFIG_ESP_CONSOLE_USB_SERIAL_JTAG=y，以实现内置usb-uart/jtag为repl固件自动下载功能
7. 修改sdkconfig.psram
   根据芯片型号正确配置片内或片外PSRAM。
   参考：
   硬件：https://docs.espressif.com/projects/esp-hardware-design-guidelines/zh_CN/latest/esp32s3/esp-hardware-design-guidelines-zh_CN-master-esp32s3.pdf
   配置：https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32s3/api-guides/flash_psram_config.html#:~:text=%E8%A6%81%E5%90%AF%E5%8A%A8%20PSRAM%EF%BC%8C
8. 配置分区表
9.  集成python模块
10. 加入labplus builtin module
    - machine_pin.c
      添加mpython基于esp32s3引脚
    - drivers/startup/i2c_master.h
      修改i2c引脚
11. 加入python库
    - mpython
      修改：
      i2c引脚
      mpython引脚
      各外设引脚
12. 
   