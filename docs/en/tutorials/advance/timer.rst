Timer
=======

The earliest timing tools used by humans were sand or water hourglasses, but later with watches and clocks, people began to try to use these new timing tool to improve the time accuracy and control. Timers makes time control much easier for many tasks that peoples' require. Such as timers used in many home appliances use timers to control switches or operating duration.

--------------------------------------

.. literalinclude:: /../../examples/timer/timer_alarm.py
    :caption: Alarm timer
    :linenos:



First, import the mpython、Timer、music modules::

    from mpython import *
    from machine import Timer
    import music

Define timer callback function, play alarm sound::

    def playMusic(_):             
        music.play(music.BA_DING,wait=False)

Configure the timer, the mode is cyclic execution, the cyclic period is 5 seconds::

    tim1.init(period=5000, mode=Timer.PERIODIC,callback=playMusic)

.. Note::

    ``Timer.init(period=5000, mode=Timer.PERIODIC,callback=None)`` to initialize the timer, `mode` can be one of the following：`Timer.ONE_SHOT` means that the timer runs once, until the time limit of the configured channel expires；`Timer.PERIODIC` means that the timer runs regularly at the channel ’s configured frequency.

Get and return the current count value of the timer, and then display it on the OLED display::

    timerNum=tim1.value()
    oled.DispChar("Timer：%d ms" %timerNum,20,25)
    oled.show()

.. Note::

    timer.value() function is to get and return the current count value.

.. Attention:: 

    您可能会看到定时器没到5000ms整警报声就响了，这是因为定时数据传送到OLED显示屏上这个过程中有延时。
