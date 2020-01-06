# The MIT License (MIT)
# Copyright (c) 2019, Tangliufeng for labplus Industries

# 掌控板磁力计Magnetic应用--指北针 

from mpython import *
import math

# 绘制罗盘中心坐标和半径
xc,yc,r= 64,32,30


def draw_heading(angle):
    """绘制磁北指针"""
    global xc,yc,r
    angle = 360 - angle
    am = math.pi * 2.0 * angle / 360
    xm = round(xc + r * math.sin(am))
    ym = round(yc - r * math.cos(am))
    oled.line(xc, yc, xm, ym, 1)

# 电子罗盘校准
magnetic.calibrate()
sleep(2)
oled.DispChar('指北针',0,0)
# 绘制罗盘轮廓
oled.circle(xc, yc, r+1, 1)
oled.show()
while True:
    # 获取磁力计电子罗盘角度
    angle = magnetic.get_heading()
    # 清除指针
    oled.fill_circle(xc, yc, r, 0)
    # 显示罗盘指针
    draw_heading(angle)
    oled.show()
    print("磁北极夹角: %d" %angle)
