.. _extboard_tutorials:

Tutorials
============

This chapter will explain the basic use of mPython Expansion Board: Motor Drive, Audio Playback, TTS Speech Synthesis,infrared emission(ir learning). For technical parameter details, refers to :ref:`mPython Expansion Board Introduction <extboard_introduce>` chapter.  

.. image:: /../images/extboard/extboard_back.png


Motor Drive
-------

It supports 2-way PWM motor drive for use of DC motor, such as TT motor, N20.

Programming

First, import the parrot module::

    import parrot

M1、M2 set forward speed as 80::

    import parrot                           # import parrot module

    parrot.set_speed(parrot.MOTOR_1,80)       #  set M1 forward speed as 80
    parrot.set_speed(parrot.MOTOR_2,80)       #  set M2 forward speed as 80

Reverse::

    parrot.set_speed(parrot.MOTOR_1,-80)      #  set M1 reverse speed as 80
    parrot.set_speed(parrot.MOTOR_2,-80)      #  set M2 reverse speed as 80

Stop::

    parrot.set_speed(parrot.MOTOR_1,0)        # stop
    parrot.set_speed(parrot.MOTOR_2,0)        # stop


Function used to control the motor speed ``set_speed(motor_no, speed)`` 。``motor_no`` The parameter is the motor number, and the optional number constants are ``MOTOR_1`` 、``MOTOR_2`` 。 ``speed`` parameter are speed, range -100~100, +ve value means forward rotation, -ve value for backwards rotation.
To check the current speed setting   ``get_speed(motor_no)`` return to current motor speed.


Audio Playback
-------

The built-in speaker supports wav、MP3 format for playback of those audio files in the mPython Board or others from networks. 

Local Audio Playback
+++++++

.. Attention:: 

   Playing local MP3 audio is limited by the file system and ram size of micropython. When the file is larger than 1MB, it is difficult to download. As the size of the audio file is limited and should be as small as possible.

To download :download:`</../../examples/extboad_audio.rar>` upload to the mPython Board file system.


First, import the audio module::

    import audio


Play local MP3 audio::

    import audio                            # import audio object
    audio.player_init()                     # play initialization
    audio.play("music_1.mp3")               # play "music_1.mp3"

.. Hint:: 

    You can get the audio you need at the below website. Note: the uploading file to be compressed to reduce the file size!

    * Audio Sound Effects：http://www.aigei.com/sound/
    * Audio Converter：https://online-audio-converter.com/cn/


Play network audio files
++++++++++++

To play MP3 audio files on the network, needs to know their URL (web address). But currently most music networks are protected by copyright and don't provide their URL. You may search through use of some plug-ins to locate their URL.


.. literalinclude:: /../../examples/audio/audio_play.py
    :caption: play MP3 audio
    :linenos:

.. Note:: 

    Maintain stable network connectivity of mPython Board with the URL full web address.
    
The ``audio`` module use the audio decoding function of  ``audio.play(url)``, the parameter of ``url`` can be the path or network URL address of the local file system of the audio source. For the detail application of ``audio`` module audio decoding function, please refer to:
:ref:`audio chapter <audio>` 。

Speech Synthesis (TTS)
------------

TTS (Text To Speech), this is “from Text to Voice”，a big step of man-machine interaction. It transforms text into asking text so that the machine can speak.



Infrared emission
-------------------

We use a lot of infrared technology in our life, such as TV, air conditioning and other home appliances remote control.
The encoded data is transmitted through an infrared tube after the carrier wave. Infrared receiving equipment, decoding the encoded data, get effective data. Implement control.

Simply put, infrared encoded valid data consists of 1 BTYES user code + 1 BTYES command code. General user code is used to distinguish manufacturers or suppliers, the actual corresponding key value is the command code.

Before infrared emission, infrared encoded data needs to be generated, and NEC encoding is used here::

    >>> from parrot import IR_encode, IR
    >>> ir_buf = ir_code.encode_nec(0x01, 0x01)  # 用户码0x01 , 命令码0x01

Once we get the infrared encoded data, we can send the infrared data::

    >>> ir = IR()  # 实例红外抽象类
    >>> ir.send(ir_buf)  #发送预先编译好的红外编码

Because the infrared encoding protocol is many. Or when you don't know the code value of the infrared remote control, how can you copy its code? In this case, you need to use infrared learning.
It can record infrared signals. And then the infrared signal that's recorded is sent out.

The infrared tube of the expansion board is directly opposite the infrared tube of the learning object, and the distance should be within 1CM (the strength of the signal directly affects the success rate of learning).

Start to learn::

    >>> ir.learn()      

Hold down the key to learn as often as possible for 5 seconds. Wait for the result to be returned.


    >>> ir.learn()
    >>> True
    >>>

If return to True, it means learning succeeded, Fail means learning failed, repeat the above steps to learn again.

Get the learned infrared encoded data::

    >>> ir_learn = ir.get_learn_data()

Once you get the learning data, you can transmitted infrared data::

    >>> ir.send(ir_learn)