.. _extboard_tutorials:

Tutorials
============

This chapter will explain the basic use of mPython Expansion Board: Motor Drive, Audio Playback, TTS Speech Synthesis. For technical parameter details, refers to :ref:`mPython Expansion Board Introduction <extboard_introduce>` chapter.  

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

Get ready
+++++

The online speech synthesis function mPython Board used  `iflytek on;ine speech synthesis API <https://www.xfyun.cn/services/online_tts>`_ , To start, users need to register in iFLYTEK open platform and do the corresponding configuration.

- Step 1. Register an account at https://www.xfyun.cn .

.. image:: /../images/extboard/xfyun_1.png
    :scale: 80 %


- Step 2. Create new application, on application platform select "WebAPI"

.. image:: /../images/extboard/xfyun_2.gif


- Step3. Add "Online Speech Synthesis" service，enter into the program APPID、APIKey example ``TTS`` ，get your own public network IP(http://www.ip138.com) and add to IP White list.

.. Attention:: 

    * While processing and after granted authorization, the server will check whether the caller's IP is in the IP white list configured on iFLYTEK open platform, for caller's IP not configured to the white list, the server will decline service.
    * IP White List, edit the application management card at the console - my application - corresponding service. It will take effect about five minutes after saving. 
    * Each IP white list can be set up to 5 IP, which are Internet IP. Do not set LAN IP.
    
.. image:: /../images/extboard/xfyun_3.gif


Text To Speech
++++++++

.. Attention:: TTS function depends on the network. connect to the network and pay attention to maintain the stable network connectivity!


.. literalinclude:: /../../examples/audio/tts.py
    :caption: TTS, Text To Speech example
    :linenos:




First, use  ``ntptime.settime()`` to calibrate RTC clock. Then ``player_init()`` initialize. Use ``xunfei_tts_config(api_key, appid )`` , ``appid`` , ``api_key`` as mandatory parameters, Application in the iFLYTEK platform APPID、API_KET. Finally apply ``xunfei_tts(text)``
To turn this page from Text To Speech.



TTS supports text conversion between Chinese and English.  You can turn what you want to say into speech in the form of text. In this way, you can add "human mouth" to your mPython Board to simulate the human-computer conversation scene.
