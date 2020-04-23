Firmware Burn-in
====================


* Use the burning tools provided by Lexin official website `Flash SW Download <https://www.espressif.com/zh-hans/support/download/other-tools>`_。
*Access to mPython Board firmware :ref:`mPython Board firmware <release>` Chapter acquisition。

---------

Select **ESP32 DownloadTool** 

.. image:: /../images/flashburn/flashDownload_1.png

Select **SPIDownload** ，Browse to select the just downloaded mPython Board firmware mpython_v2.0.0.bin，and set the address to be 0x00。
Set CrystallFreq to 40M，SPI SPEED set to 40MHz，SPI MODE set as DIO，FLASH SIZE set to 64MBit，
set Serial port number as the actual serial port，Baud rate 1152000。

.. Caution:: 

    * Firmware versions after v1.1.1, Firmware burn-in initial address change as 0x00!
    * Firmware versions after v1.5.0, Integrate Noto font library! Firmware before v1.5.0 may need to be refresh font library, You can select a word library on the flash tool Noto_Sans_CJK_SC_Light16.xbf，And set 0x400000 burning, same firmware burning method.

.. image:: /../images/flashburn/flashDownload_2.png

Click "START", the mPython Board will enter download mode. Firmware downloading, as shown below.

.. Hint:: mPython Board hardware version before v1.0.1, Press the A and B keys simultaneously and hold for 2 seconds, then release to enter the manual download mode.

.. image:: /../images/flashburn/flashDownload_3.png

Download completed as shown below.

.. image:: /../images/flashburn/flashDownload_4.png
