1. 把需要用到的esp-adf compononts添加到port/componts下
2. 为减小固件size，做些修改
   - 去除componts中不用到的c文件
   - 修改一些components CMakeList.txt，去除一些不用的components依赖。
   

修改：
复制以下components到项目中：audio_stream clouds dueros_service esp_dispatcher esp_peripherals esp-adf-libs esp-sr tone_partition 

esp_stream tone_partition wifi_service CMakeList.txt中去掉esp_actions依赖。

tone_partion 添加esp_partion依赖，tone_partion.c去掉：#include "partition_action.h"