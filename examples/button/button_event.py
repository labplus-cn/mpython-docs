# The MIT License (MIT)
# Copyright (c) 2020, Tangliufeng for labplus Industries

# 按键事件回调简单的示例

from mpython import *

def on_button_a_pressed(pin):
    """ a键按下事件回调函数 """
    print("按键A，按下了。")

def on_button_b_pressed(pin):
    """ b键按下事件回调函数 """
    print("按键B，按下了。")

# 按键事件注册
button_a.event_pressed = on_button_a_pressed
button_b.event_pressed = on_button_b_pressed