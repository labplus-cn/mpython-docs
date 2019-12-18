# 打字效果
from mpython import *
oled.fill(0)

# 显示的字符串
_str = "掌控板是创客教育专家委员会、猫友汇、广大一线老师共同提出需求并与创客教育行业优秀企业代表共同参与研发的教具、学具,是一块为教育而生的开源硬件，也是一个公益项目。mPython掌控板是一块MicroPython微控制器板，它集成ESP32高性能双核芯片,使用当下最流行的Python编程语言，以便您轻松地将代码从桌面传输到微控制器或嵌入式系统。"

# 起点坐标    
axis = (0, 0)

# 逐字显示,根据返回的坐标续接显示
for c in _str:
    response = oled.DispChar(c, axis[0], axis[1])
    char_width = response[0]
    axis = response[1]
    oled.show()

    # 满屏时,清屏
    if axis[1] >= 64 - 16 and char_width >= 128-axis[0]:
        print('Clear screen')
        oled.fill(0)
