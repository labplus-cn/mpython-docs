from mpython import *
import parrot
import time

def on_button_a_pressed(_):
    global data
    ir.learn()
    time.sleep(4)
    if 0 == ir.__get_learn_status():
        data = ir.get_learn_data()
        print(data)
    else:
        print('什么都没学到...')

button_a.event_pressed = on_button_a_pressed

def on_button_b_pressed(_):
    global data
    print(data)
    ir.send(data, 0)

button_b.event_pressed = on_button_b_pressed

ir = parrot.IR()
data = None