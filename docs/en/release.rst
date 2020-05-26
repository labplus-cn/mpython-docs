.. _release:

Firmware Release
========

mpython_v2.0.1
------------------

===============  ====================================
 **Release Date**：    2020/01/13
 **Firmware Download**:     :download:`mpython_firmware_v2.0.1 <https://github.com/labplus-cn/mpython/releases/download/v2.0.1/mpython_v2.0.1.bin>`
===============  ====================================

**Journal**：

* Fixed the bug that sometimes cannot be recorded
* Add compass correction function
* urequests modify ssl to default not to shake hands
* Increase font display function
* Add logging module
* Update weather icon module
* Modify some known small bugs

mpython_v2.0.0
------------------

===============  ====================================
 **Release Date**：    2019/12/25
 **Firmware Download**:     :download:`mpython_firmware_v2.0.0 <https://github.com/labplus-cn/mpython/releases/download/v2.0.0/mpython_v2.0.0.bin>`
===============  ====================================

**Journal**：

* Upgrade MicrPpython IDF to v4.0
* Rebuild the project framework
* Add Bluetooth BLE
* Add recording function
* Add magnetometer
* Modify of USB interface and key button hardwares
* urequest module, add POST form function
* oled.DispChar() increase the return character width parameter
* Add urllib.parse module (URL resolution)

mpython_v1.5.1
------------------

===============  ====================================
 **Release Date**：    2019/9/25
 **Firmware Download**:     :download:`mpython_firmware_v1.5.1 </../../firmware/mpython_firmware_v1.5.1.bin>`
===============  ====================================

**Journal**：

* `music` Added 5 Chinese songs to Music module:

   * GE_CHANG_ZU_GUO（歌唱祖国）
   * DONG_FANG_HONG（东方红）
   * CAI_YUN_ZHUI_YUE（彩云追月）
   * ZOU_JIN_XIN_SHI_DAI（走进新时代）
   * MO_LI_HUA（茉莉花）
   * YI_MENG_SHAN_XIAO_DIAO(沂蒙山小调)

* Fix the problem of mutual interference between the servo and motor sharing one LED PWM high-speed channel。
* Fix known bugs


mpython_v1.5.0
-----------------

===============  ====================================
 **Release Date**：    2019/7/22
 **Firmware Download**:     :download:`mpython_firmware_1.5.0-23 </../../firmware/mpython_firmware_v1.5.0-23.bin>`
===============  ====================================

**Journal**：

* Firmware merge font, burn firmware start address 0x00;
* The file system space is expanded from 1M to 2M (the starting address of the font is changed from 0x300000 to 0x400000);
* Added `gui.Image` class to support 1bit bmp and pbm image formats;
* Added `gui.UI.qr_code` QR code display;
* Added striplight `NeoPixel.brightness` brightness adjustment function
* Added `sdcard` module;
* `request` adds file parameter to support file upload;
* `audio` module adds recording function;
* C layer realizes drawing function to improve efficiency;
* Built-in bluebit, parrot.py, etc.;
* Fix known bugs;



mpython_v1.4.0
------------

===============  ====================================
 **Release Date**：    2019/4/22
 **Firmware Download**:     :download:`mpython_firmware_1.4.0 </../../firmware/mpython_firmware_1.4.0.zip>`
===============  ====================================

**Journal**：

* Add ``radio`` wireless module, support wireless broadcast function；
* Added Timer and Thread will be closed when catching KeyboardInterrupt interrupt or exiting the main loopd；
* Fix bug (music module)；


mpython_v1.3.0
------------

===============  ====================================  
 **Release Date**：    2019/4/8
 **Firmware Download**:     :download:`mpython_firmware_1.3.0 </../../firmware/mpython_firmware_1.3.0.zip>`
===============  ====================================

**Journal**：

* Add ``audio`` module to support the audio playback function of the control panel and the TTS text-to-speech function；
* Fix ntptime.py bug of wrong time zone;


mpython_v1.2.0
------------

===============  ====================================  
 **Release Date**：    2019/1/29
 **Firmware Download**:     :download:`mpython_firmware_1.2.0 </../firmware/mpython_firmware_1.2.0.zip>`
===============  ====================================

**Journal**：

* Built mpython library firmware, and the file system does not need to be flashed in;
* Modify the boot animation to a static image without occupying boot time;
* Modify the prompt page code error to indicate the error location and detail information, and no more display the error prompt on the keyboardinterrupt;
* Fix some problems with reading of i2c blue: bit modules;
* Enhanced the reading stability of the built-in sensor, retry 5 times after an error to report an error;

mpython_v1.1.1
--------------

===============  ====================================  
 **Release Date**：      
 **Firmware Download**:     :download:`mpython_firmware_1.1.1 </../../firmware/mpython_firmware_1.1.1.zip>`
===============  ====================================

**Journal**：

* The firmware burning start address is changed from 0x1000 to 0x00
* Change the animation start-up time to 0.5S
* Fix some errors of urequest
* Modify the server address of ntptime and provide user-specified address interface
