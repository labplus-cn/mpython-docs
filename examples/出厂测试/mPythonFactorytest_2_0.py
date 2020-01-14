from machine import Timer, UART
from mpython import *
import time, ubinascii, framebuf
import machine, music,audio
import ustruct,os

logo = bytearray([\
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X07,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X0F,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X1F,0X06,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X3E,0X0E,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X7C,0X1F,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XF8,0X3E,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X06,0X01,0XF0,0X7C,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X0F,0X03,0XE0,0XF8,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X1F,0X07,0XC1,0XF0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X3E,0X0F,0X83,0XE0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X7C,0X1F,0X07,0XC1,0XC0,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0XF8,0X3E,0X0F,0X83,0XC0,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X01,0XF0,0X7C,0X1F,0X07,0XC0,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X03,0XE0,0XF8,0X3E,0X0F,0X80,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X07,0XC0,0XF0,0X7C,0X1F,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X0F,0X81,0XE0,0XF8,0X3E,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X1F,0X01,0XE1,0XF0,0X7C,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X3E,0X01,0XE3,0XE0,0XF8,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X3C,0X01,0XE3,0XC1,0XF0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X78,0X01,0XE1,0X83,0XE0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X78,0XC1,0XE0,0X07,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0XF0,0XE0,0XF0,0X0F,0X83,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0XF0,0XE0,0XF8,0X1F,0X07,0X80,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XE7,0XF8,0X7C,0X1E,0X0F,0X80,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XE7,0XFC,0X3E,0X0C,0X1F,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XE7,0XF8,0X1F,0X00,0X3E,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XE0,0XE0,0X0F,0X80,0X7C,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XC0,0XE0,0X07,0XC0,0XF8,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XE0,0XC0,0X03,0XC1,0XF0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XE0,0X00,0X01,0XE3,0XE0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XE0,0X00,0X01,0XE7,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0XE0,0X00,0X00,0XFF,0X80,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0XF0,0XC0,0X18,0XFF,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0XF0,0XF0,0X38,0XFE,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X78,0XFF,0XF8,0XFC,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X7C,0X7F,0XF1,0XF8,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X3E,0X0F,0X81,0XF0,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X1F,0X00,0X07,0XE0,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X0F,0XC0,0X1F,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X07,0XFF,0XFF,0X80,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X03,0XFF,0XFE,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0XFF,0XF8,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X1F,0XE0,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
                  ])

# analog
P0 = MPythonPin(0, PinMode.ANALOG)
P1 = MPythonPin(1, PinMode.ANALOG)
P2 = MPythonPin(2, PinMode.ANALOG)
ext = MPythonPin(3, PinMode.ANALOG)

# 引脚PWM测试

P8 = None
# P8 = MPythonPin(8, PinMode.PWM)
P9 = MPythonPin(9, PinMode.PWM)
P13 = MPythonPin(13, PinMode.PWM)
P14 = MPythonPin(14, PinMode.PWM)
P15 = MPythonPin(15, PinMode.PWM)
P16 = MPythonPin(16, PinMode.PWM)

# P8.write_analog(512,20)
P9.write_analog(512,20)
P13.write_analog(512,20)
P14.write_analog(512,20)
P15.write_analog(512,20)
P16.write_analog(512,20)

FREQ = 2000  
FREQ_RNAG = 0.2
PEAK  = 6000

def analysis_wav(file='test.wav'):
    """波形频率分析"""
    f = open(file,'rb')
    interval = 1/8000
    prev_sample =0
    serial=0
    # data chunk
    f.seek(0x28)
    size = ustruct.unpack('<H',f.read(4))[0]
    period_sum=0
    peak_sum=0
    sample_num=0
    for i in range(size//2):
        sample_temp = f.read(2)
        sample = ustruct.unpack('<h',sample_temp)[0]
        # print("%d," %sample,end='')
        if prev_sample <0 and sample > 0 :   
            preiod = i-serial
            period_sum += preiod
            # print("%d," %preiod,end='')
            peak_sum += sample
            sample_num +=1
            serial=i
        prev_sample =sample
    f.close()
    freq = 1/(period_sum/sample_num *interval)
    peak = peak_sum /sample_num

    return(freq,peak)

def record(file='test.wav'):
    rgb.write()
    audio.recorder_init()
    rgb[0] = (255, 0, 0)  # 用LED指示录音开始结束
    rgb.write()
    audio.record(file, 1)
    rgb[0] = (0, 0, 0)
    rgb.write()
    audio.recorder_deinit()


def play_wave(freq):
    global P8
    P8 = MPythonPin(8, PinMode.PWM)
    P8.write_analog(512, freq)
def stop_wave():
    global P8
    P8.pwm.deinit()


# MAC id
machine_id = ubinascii.hexlify(machine.unique_id()).decode().upper()


# a,b按键中断处理函数：蜂鸣器响
def btn_A_irq(_):
    if button_a.value() == 0:
        music.pitch(1000)
    else:
        music.stop()


def btn_B_irq(_):
    if button_b.value() == 0:
        music.pitch(1000)
    else:
        music.stop()


def testoled():
    """屏幕测试"""
    logo_ = framebuf.FrameBuffer(logo, 128, 64, framebuf.MONO_HLSB)
    #display.invert(1)
    oled.blit(logo_, 0, 0)
    oled.show()
    sleep_ms(1000)
    oled.fill(0)
    sleep_ms(200)
    oled.fill(1)
    oled.show()


# a,b 按键中断处理
button_a.irq(btn_A_irq)
button_b.irq(btn_B_irq)

# 创建定时器1
tim1 = Timer(1)

def Rgb_Neopixel():
    """板载RGB测试"""
    color_index = 0
    color = ((32, 0, 0), (0, 32, 0), (0, 0, 32))
    for i in range(0, 3):
        rgb[i] = color[color_index]
    rgb.write()
    color_index = color_index + 1
    color_index = color_index % 3


def Print_Serial_num():
    """镭射雕刻机通讯"""
    u = UART(2, baudrate=115200, bits=8, parity=None, stop=1, rx=26, tx=25, timeout=200)
    display.fill(1)
    display.show()
    while True:
        if u.readline() == 'COM:Give me string'.encode():
            sleep_ms(10)
            u.write(machine_id[:6] + '\n')
            u.write(machine_id[6:] + '\n\r')
            u.write(machine_id[:6] + '\n')
            u.write(machine_id[6:] + '\n\r')


# pixles timer
tim1.init(period=1000, mode=Timer.PERIODIC, callback=lambda t: Rgb_Neopixel())

#oled full pixel test
testoled()
sleep_ms(1500)
oled.fill(0)
oled.show()

MAGNETIC_HAVE = 48 in i2c.scan()


while True:
    touch_p, touch_y, touch_t, touch_h, touch_o, touch_n = touchPad_P.read(), touchPad_Y.read(), \
    touchPad_T.read(), touchPad_H.read(), touchPad_O.read(), touchPad_N.read()
    p0_value, p1_value, p2_value, p3_value = P0.read_analog(), P1.read_analog(), P2.read_analog(), ext.read_analog()
    light_value = light.read()
    sound_value = sound.read()
    acc_x, acc_y, acc_z = accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()
    if MAGNETIC_HAVE:
        mag_field,heading = magnetic.get_field_strength(),magnetic.get_heading()
    print("----------------------------")
    print('P:%d,Y:%d, T:%d, H:%d, O:%d, N:%d' % (touch_p, touch_y, touch_t, touch_h, touch_o, touch_n))
    print('P0:%d, P1:%d ,P2:%d, P3/ext:%d' % (p0_value, p1_value, p2_value, p3_value))
    print('light:%d,Sound:%d' % (light_value, sound_value))
    print('Accel,x = %.2f, y = %0.2f, z = %.2f ' % (acc_x, acc_y, acc_z))
    if MAGNETIC_HAVE:
        print('Magnetic [Field:%d,head:%d]' % (mag_field,heading))
    try:
        print("BME280 [Temp:{:.1f}C,Pressure:{:.1f}Pa,Humi:{:.1f}%]".format(bme280.temperature(), bme280.pressure(),
                                                                          bme280.humidity()))
    except Exception as er:
        print("Your mPython have not BME280!")
    print("\n\r")
    oled.rect(0, 0, 128, 64, 1)
    oled.text('s:%d,l:%d' % (sound_value, light_value), 3, 3)
    oled.text('%.1f,%.1f,%.1f' % (acc_x, acc_y, acc_z), 3, 16)
    if MAGNETIC_HAVE: 
        oled.text('Mag:%d,%d' % (mag_field, heading), 3, 32)
    oled.text('id:%s' % machine_id, 3, 48)
    oled.show()
    oled.fill(0)
    # P2和P3按键同时按下,向雕刻机发送指令
    if ext.read_analog() == 0 and P2.read_analog() == 4095:
        Print_Serial_num()
    # P1和P3按键同时按下,进入音频测试模式
    if ext.read_analog() == 0 and P1.read_analog() ==4095:
        tim1.deinit()
        oled.fill(0)
        oled.DispChar('Audio Test mode:',0,0)
        oled.show()
        rgb.fill((0,0,0))
        rgb.write()
        play_wave(FREQ)
        sleep_ms(100)
        print("Audio Recording...")
        record()
        print("Audio end!")
        stop_wave()
        result_freq,result_peak = analysis_wav()
        if (1-FREQ_RNAG)*FREQ<result_freq<(1+FREQ_RNAG)*FREQ and result_peak >=PEAK:
            audio_test = "Pass"
        else:
            audio_test = "Fail"
        print("Audio test Result is %s .[freq:%d,peak:%d]" %(audio_test,result_freq,result_peak))
        oled.DispChar("结果:%s" %audio_test,0,16)
        oled.DispChar("%d,%d" %(result_freq,result_peak),0,32)
        oled.show()
        sleep(3)
        oled.fill(0)
        tim1.init(period=1000, mode=Timer.PERIODIC, callback=lambda t: Rgb_Neopixel())
        os.remove('test.wav')
        P9.write_analog(512, 20)