# The MIT License (MIT)

# Copyright (c) 2019, Tangliufeng for labplus Industries

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

#   网络倒计时闹钟
# - 自动网络校准
# - A键/开始,B键/停止,B键(长按)/操作说明
# - 触摸键/时间设置
# - 闹钟功能

import time
import music
import font.digiface_11
import font.digiface_30
import framebuf
import ntptime
from mpython import *

## wifi设置
WIFI_SSID = ''
WIFI_PSW = ''

my_wifi = wifi()

## 全局变量定义
prev_timestamp = time.time()
current_timestamp = None
DAYS, HOURS, MINUTES, SECONDS = [0]*4
pre_refresh = time.ticks_ms()
curr_refresh = 0
INTERVAL = 800
STATUS = 0
setting = False
countdown = 0
blink_dot =True
aBtn_prev, bBtn_prev = button_a.value(), button_b.value()
pBtn_prev, yBtn_prev, hBtn_prev, oBtn_prev, nBtn_prev = [0]*5
TOUCH_THRESHOLD = 250


## 函数定义
def display_font(_font, _str, _x, _y, _wrap, _z=0):
    """显示数码管字体"""
    _start = _x
    for _c in _str:
        _d = _font.get_ch(_c)
        if _wrap and _x > 128 - _d[2]:
            _x = _start
            _y += _d[1]
        if _c == '1' and _z > 0:
            oled.fill_rect(_x, _y, _d[2], _d[1], 0)
        oled.blit(framebuf.FrameBuffer(bytearray(_d[0]), _d[2], _d[1],
                                       framebuf.MONO_HLSB), (_x+int(_d[2]/_z)) if _c == '1' and _z > 0 else _x, _y)
        _x += _d[2]


def load_network():
    """开始加载网络、校准时间"""
    oled.DispChar('联网中…', 40, 20)
    oled.show()
    my_wifi.connectWiFi(WIFI_SSID, WIFI_PSW)
    oled.fill(0)
    oled.DispChar('联网成功', 40, 20)
    oled.show()
    ntptime.settime(timezone=8, server="time.windows.com")
    oled.DispChar('同步成功', 40, 20)
    oled.show()

def dot_blink(x,y,enable):
    """计时器点闪烁"""
    w=4
    h=5
    oled.fill_rect(x,y+h,w,h,enable)
    oled.fill_rect(x,y+h*3,w,h,enable)


def draw_countdown(seconds):
    """画倒计时表"""
    global blink_dot,STATUS
    sec = seconds % 60
    min = seconds // 60 % 60
    hour = seconds // (60*60) % 24
    day = seconds // (60*60*24) % 365
    display_font(font.digiface_30, "%02d" % hour, 0, 0, False, 2)
    dot_blink(39,3,blink_dot)
    display_font(font.digiface_30, "%02d" % min, 45, 0, False, 2)
    dot_blink(84,3,blink_dot)
    display_font(font.digiface_30, "%02d" % sec, 90, 0, False, 2)
    display_font(font.digiface_11, "%0*d" %(3,day), 0, 35, False, 2)
    oled.DispChar('天', 20, 32, 1)
    display_status(STATUS)

def display_status(stat):
    """画开始/结束键"""
    grid = 16//4
    x,y = 34,32
    oled.fill_rect(x,y,16,16,0)
    if not stat:
        oled.fill_triangle(x+grid,y+grid,x+grid,y+grid*3,x+grid*3,y+grid*2,1)
    else:
        oled.fill_rect(x+grid,y+grid,grid*2,grid*2,1)


def display_operation():
    """操作说明显示"""
    oled.DispChar("按A键,倒计时开始", 0, 0)
    oled.DispChar("按B键,倒计时停止", 0, 16)
    oled.DispChar("调整P增加,Y减少天数", 0, 32)
    oled.DispChar("调整H时针,O分针,N秒针", 0, 48)

def alarm(enable):
    """闹钟事件"""
    rgb.brightness(0.1)
    oled.fill_rect(80,32,128-80,16,0)
    if enable:
        music.play(music.MO_LI_HUA ,wait=False,loop=True)
        rgb.fill((100,0,0))
        rgb.write()
        oled.DispChar("时间到",80,32,2)
        oled.show()
    else:
        music.pitch(0)
        rgb.fill((0,0,0))
        rgb.write()
        


def sysnc_time():
    """同步时间事件"""
    t1 = time.ticks_ms()
    try:
        while not my_wifi.sta.isconnected():
            if utime.ticks_diff(time.ticks_ms(), t1) > 5000:
                oled.DispChar("连接超时", 80, 32, 2)
                return
            my_wifi.sta.connect()
    except Exception:
        oled.DispChar("连接失败", 80, 32, 2)
        return
    else:
        try:
            ntptime.settime(timezone=8, server="time.windows.com")
        except Exception:
            oled.DispChar("同步失败", 80, 32, 2)
        else:
            oled.DispChar("同步成功", 80, 32, 2)


def is_timeout(hours):
    """判断是否到设定时间间隔"""
    global current_timestamp
    return current_timestamp % (60*60*hours) ==0

def setting_process():
    """倒计时设置处理进程"""
    global DAYS, HOURS, MINUTES, SECONDS
    global STATUS,setting
    global aBtn_prev, bBtn_prev, pBtn_prev, yBtn_prev, hBtn_prev, oBtn_prev, nBtn_prev
    global target_timestamp
    global blink_dot
    aBtn_cur = button_a.value()
    bBtn_cur = button_b.value()
    pBtn_cur = 1 if touchPad_P.read() < TOUCH_THRESHOLD else 0
    yBtn_cur = 1 if touchPad_Y.read() < TOUCH_THRESHOLD else 0
    hBtn_cur = 1 if touchPad_H.read() < TOUCH_THRESHOLD else 0
    oBtn_cur = 1 if touchPad_O.read() < TOUCH_THRESHOLD else 0
    nBtn_cur = 1 if touchPad_N.read() < TOUCH_THRESHOLD else 0
    if aBtn_cur ^ aBtn_prev:
        time.sleep_ms(10)
        # A键按下
        if button_a.value() == 0:
            if STATUS==0:
                # 计算目标时间戳,倒计时开始
                target_timestamp = countdown +time.time()
                oled.fill_rect(0,48,128,16,0)
                oled.DispChar("{}/{}/{} {}:{}:{}" .format(*time.localtime(target_timestamp)[:6]),0,48,1)
                print("倒计时开始!")
                STATUS = 1
                blink_dot =False
            
        aBtn_prev = aBtn_cur
    if bBtn_cur ^ bBtn_prev:
        time.sleep_ms(10)
        # B键按下
        if button_b.value() == 0:
            DAYS, HOURS, MINUTES, SECONDS = [0]*4
            # 没有倒计时开始时,显示操作
            if STATUS==0:
                oled.fill(0)
                display_operation()
                oled.show()
                while not button_b.value():
                    pass
                setting = True
                oled.fill(0)
            # 如果倒计时开始,按下B键结束
            elif STATUS==1 or STATUS==2:
                STATUS = 0
                print("倒计时结束!")
                alarm(False)
                display_status(STATUS)
                oled.show()
                
        bBtn_prev = bBtn_cur

    if pBtn_cur ^ pBtn_prev:
        time.sleep_ms(10)
        # 按下P键
        if touchPad_P.read() < TOUCH_THRESHOLD:
            DAYS += 1
            if DAYS > 365:
                DAYS = 0
            setting = True
            # print("Day +")
        pBtn_prev = pBtn_cur
    if yBtn_cur ^ yBtn_prev:
        time.sleep_ms(10)
        # 按下Y键
        if touchPad_Y.read() < TOUCH_THRESHOLD:
            DAYS -= 1
            if DAYS < 0:
                DAYS = 365
            setting = True
            # print("Day -")
        yBtn_prev = yBtn_cur
    if hBtn_cur ^ hBtn_prev:
        time.sleep_ms(10)
        # 按下H键
        if touchPad_H.read() < TOUCH_THRESHOLD:
            HOURS += 1
            if HOURS > 24:
                HOURS = 0
            setting = True
            # print("hour +")
        hBtn_prev = hBtn_cur
    if oBtn_cur ^ oBtn_prev:
        time.sleep_ms(10)
        # 按下O键
        if touchPad_O.read() < TOUCH_THRESHOLD:
            MINUTES += 1
            if MINUTES > 60:
                MINUTES = 0
            setting = True
            # print("Minute +")
        oBtn_prev = oBtn_cur
    if nBtn_cur ^ nBtn_prev:
        time.sleep_ms(10)
        # 按下N键
        if touchPad_N.read() < TOUCH_THRESHOLD:
            SECONDS += 1
            if SECONDS > 60:
                SECONDS = 0
            setting = True
            # print("Second +")
        nBtn_prev = nBtn_cur

## Setup
load_network()
time.sleep_ms(500)
oled.fill(0)

draw_countdown(0)
oled.DispChar('按住B键查看使用说明', 0, 48)
oled.show()

## Loop
while True:
    # 设置处理进程
    setting_process()
    # 计算倒计时秒数
    countdown = DAYS*60*60*24 + HOURS * 60*60 + MINUTES*60 + SECONDS 
    # 在设置状态
    if setting and STATUS==0:
        blink_dot =True
        draw_countdown(countdown)
        oled.fill_rect(0,48,128,16,0)
        oled.DispChar('按住B键查看使用说明', 0, 48)
        oled.show()
        print("倒计时设置:{}天{}小时{}分{}秒" .format(DAYS, HOURS, MINUTES, SECONDS))
        setting=False

    current_timestamp = time.time()
    # 时间校准,6小时校准一次
    if is_timeout(6):
        sysnc_time()
    # 设置成功后进入倒计时
    if STATUS == 1 and (current_timestamp!=prev_timestamp):
        
        # 计算距离目标时间差
        time_diff = time.ticks_diff(target_timestamp, current_timestamp)
        # 时间没到,继续倒计时
        if time_diff >= 0:
            draw_countdown(time_diff)
            oled.show()
            prev_timestamp = current_timestamp
            blink_dot = not blink_dot
            
        # 时间到了
        else:
            STATUS=2
            # 闹钟事件
            alarm(True)

            
    
