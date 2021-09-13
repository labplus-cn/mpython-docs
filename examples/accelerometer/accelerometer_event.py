# The MIT License (MIT)
# Copyright (c) 2020, Tangliufeng for labplus Industries

# accelerometer event simple example

from mpython import *

def motion_callback_function(event):
    """ 运动事件回调函数 """
    if event == accelerometer.TILT_LEFT:
        print("tilt left")
    elif event == accelerometer.TILT_RIGHT:
        print("tilt right")
    elif event == accelerometer.TILT_UP:
        print("tilt up")
    elif event == accelerometer.TILT_DOWN:
        print("tilt down")
    elif event == accelerometer.FACE_UP:
        print("face up")
    elif event == accelerometer.FACE_DOWN:
        print("face down")
    elif event == accelerometer.SINGLE_CLICK:
        print("single click")
    elif event == accelerometer.DOUBLE_CLICK:
        print("double click")
    elif event == accelerometer.FREEFALL:
        print("freefall")

# 事件回调注册
accelerometer.event_tilt_up = motion_callback_function
accelerometer.event_tilt_down = motion_callback_function
accelerometer.event_tilt_left = motion_callback_function
accelerometer.event_tilt_right = motion_callback_function
accelerometer.event_face_up = motion_callback_function
accelerometer.event_face_down = motion_callback_function
accelerometer.event_single_click = motion_callback_function
accelerometer.event_double_click = motion_callback_function
accelerometer.event_freefall = motion_callback_function


