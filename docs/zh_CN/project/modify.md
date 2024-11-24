1. machine_pin.c
   esp32_common.cmake去掉对machine_pin.c编译，复制micropython/ports/esp32/machine_pin.c到port/builtins/，此文件添加mpython pin定义。

2、修改partition-8MiB.csv文件，保持跟乐动掌控的一致，但会出固件区域不够情况，扩容之，暂不知会有什么问题，之前似似乎有利用扩容区。

3、添加micropython-lib库的neopixel.py到port/modules,参照唐工的对应文件做修改。注释掉boards/manifest.py内的对本库的引用。

4. machine_touchpad.c
   esp32_common.cmake去掉对machine_touchpad.c编译，复制micropython/ports/esp32/machine_touchpad.c到port/builtins/，按之版本修改本文件。
   mpconfigboard.cmake添加此文件编译