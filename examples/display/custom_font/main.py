# The MIT License (MIT)
# Copyright (c) 2019, Tangliufeng for labplus Industries

# 掌控板oled.DispChar_font()自定义字体显示的简单示例

from mpython import *

# 导入转换好的字体
import simfang16
import freescpt18
import stxingkai20

# 使用自定义字体显示
oled.DispChar_font(simfang16,'你好,世界', 23, 0)
oled.DispChar_font(stxingkai20,'你好,世界', 23, 21)
oled.DispChar_font(freescpt18,'hello,world', 23, 42)

oled.show()