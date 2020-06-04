.. _music.py:

.. module:: music
   :synopsis: Music related functions

:mod:`music` --- Music related functions
=======================================

``music`` module is used in the same way as the music of micro:bit.

To use the music module, you need::

    import music

Note
++++

Note format:

    NOTE[octave][:duration]

    - ``NOTE`` - Express NOTE c、d、e、f、g、a、b. Note that “#” means to increase the basic level by a semitone; “b” means to decrease the basic level by a semitone. The Note ``R`` it is regarded as resting (silent). For example,c# is C- rising semitone, ab is A- falling semitone.
    - ``octave`` - indicates pitch, the default is 4, which is midrange
    - ``duration`` - Indicates the duration of the note duration, the default is 4 beats

|

Such as, ``A1:4`` "A" note with pitch 1 for 4 beats（The beat can also be set by the``set_tempo`` function-see below）.


The beginning of Beethoven's Fifth Symphony::

    ['r4:2', 'g', 'g', 'g', 'eb:8', 'r:2', 'f', 'f', 'f', 'd:8']

|

The definition and range of the octave scale are in accordance with the table on scientific pitch notation listed on this page `Scientific pitch notation`_.  Such as, middle "C" is ``c4`` and concert “A”（440） is ``a4`` . The octave note starts with the note "C" .

.. _ Scientific tone notation: https://en.wikipedia.org/wiki/Scientific_pitch_notation#Table_of_note_frequencies


Function
++++++++

.. function:: set_tempo(ticks=4, bpm=120)

    Set the playback rhythm。
    
    - ``ticks`` - Note time, integer. The default is 4, which means the quarter note is a beat.
  
    - ``bpm`` - Beat speed, integer. Unit, bmp (beats per minute).
 
|

    Referrence for playback rhythm setting:

    * ``music.set_tempo()`` - Restore the playback rhythm setting to ticks = 4, bpm = 120
    * ``music.set_tempo(ticks=8)`` - Only change the note time, eighth note is one beat
    * ``music.set_tempo(bpm=180)`` - Only change the tempo

|

    To compute the beat duration (in milliseconds)： `60000/bpm/ticks_per_beat` ::
    
        For the default value, 60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds

.. function:: get_tempo()

    Get current velocity as an integer tuple: ``(ticks, bpm)``.

.. function:: play(music, pin=6, wait=True, loop=False)

    - ``music`` 

        - Play ``music`` with the music DSL defined above。

        - If ``music`` is a string, it should be a single note, for example ``'c1:4'``。

        - If ``music``  is specified as a list of notes (as defined in the Music DSL section above), they are played one after another to perform the melody.

    - ``pin`` he default is the P6 pin of the mPython Board

    - ``wait`` blocking: If  ``wait`` is set as ``True``, it is blocking, otherwise it is not.

    - ``loop`` ：如果 ``loop`` 设置为 ``True`` ，则重复调整直到stop被调用（见下文）或阻塞调用被中断。
   

.. function:: pitch(frequency, duration=-1, pin=Pin.P6, wait=True)

    - ``frequency``, ``duration``:以给定指定毫秒数的整数频率播放频率。例如，如果频率设置为440并且长度设置为1000，那么我们会听到标准A调一秒钟。

        如果 ``duration`` 为负，则连续播放频率，直到阻塞或者被中断，或者在后台呼叫的情况下，设置或调用新频率stop（见下文）。

    - ``pin`` pin=Pin.P6,默认是掌控板的P6引脚。可重定义其他引脚。

        请注意，您一次只能在一个引脚上播放频率。

    - ``wait`` 阻塞：如果 ``wait`` 设置为 ``True``, 为阻塞,否则未不。


.. function:: stop()
    
   停止给定引脚上的所有音乐播放。


.. function:: reset()

    以下列方式重置以下属性的状态

        * ``ticks = 4``
        * ``bpm = 120``
        * ``duration = 4``
        * ``octave = 4``

内置旋律
++++++++

出于教育和娱乐的目的，该模块包含几个以Python列表表示的示例曲调。它们可以像这样使用：

    >>> import music
    >>> music.play(music.NYAN)

所有音乐都不受版权保护，由Nicholas H.Tollervey撰写并发布到公共领域或者有一位不知名的作曲家，并受到公平（教育）使用条款的保护。

它们是:

    * ``DADADADUM`` - 贝多芬第五交响曲C小调开幕式。
    * ``ENTERTAINER`` - 斯科特乔普林的Ragtime经典作品“The Entertainer”的开场片段。
    * ``PRELUDE`` - JSBach的48首前奏曲和赋格曲的第一首C大调前奏曲的开篇。
    * ``ODE`` - 贝多芬第七交响曲D小调的“欢乐颂”主题。
    * ``NYAN`` - Nyan Cat主题 (http://www.nyan.cat/). 作曲家不详。
    * ``RINGTONE`` - 听起来像手机铃声的东西。用于指示传入消息。
    * ``FUNK`` - 为秘密特工和犯罪主谋提供的时髦低音系列。
    * ``BLUES`` - 一个boogie-woogie 12杆蓝调步行低音。
    * ``BIRTHDAY`` - “生日快乐" 版权状态见: http://www.bbc.co.uk/news/world-us-canada-34332853
    * ``WEDDING`` - 来自瓦格纳歌剧“Lohengrin”的新娘合唱。.
    * ``FUNERAL`` -  “葬礼进行曲”，也被称为FrédéricChopin的钢琴奏鸣曲第2号B-minor,Op 35。
    * ``PUNCHLINE`` -一个有趣的片段表明一个笑话已经被创造出来了。
    * ``PYTHON`` - John Philip Sousa的游行“Liberty Bell”又名“Monty Python's Flying Circus”的主题（之后以Python编程语言命名）。
    * ``BADDY`` - 沉默的电影时代入口的一个坏人。
    * ``CHASE`` - 无声电影时代的追逐场景。
    * ``BA_DING`` - 表示发生了某些事情的短信号
    * ``WAWAWAWAA`` - 一个非常悲伤的长号。
    * ``JUMP_UP`` - 用于游戏，表示向上移动。
    * ``JUMP_DOWN`` - 用于游戏，表示向下移动。
    * ``POWER_UP`` - 一种炫耀，表明一项成就被释放。
    * ``POWER_DOWN`` - 一种悲伤，表示一项成就已经失去。
    * ``GE_CHANG_ZU_GUO`` - 歌唱祖国
    * ``DONG_FANG_HONG`` - 东方红
    * ``CAI_YUN_ZHUI_YUE`` - 彩云追月
    * ``ZOU_JIN_XIN_SHI_DAI`` - 走进新时代
    * ``MO_LI_HUA`` - 茉莉花
    * ``YI_MENG_SHAN_XIAO_DIAO`` - 沂蒙山小调

示例::

    """
        music.py
        ~~~~~~~~

        Plays a simple tune using the Micropython music module.
        This example requires a speaker/buzzer/headphones connected to P0 and GND.
    """
    from mpython import *
    import music

    # play Prelude in C.
    notes = [
        'c4:1', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5', 'c4', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5',
        'c4', 'd', 'a', 'd5', 'f5', 'a4', 'd5', 'f5', 'c4', 'd', 'a', 'd5', 'f5', 'a4', 'd5', 'f5',
        'b3', 'd4', 'g', 'd5', 'f5', 'g4', 'd5', 'f5', 'b3', 'd4', 'g', 'd5', 'f5', 'g4', 'd5', 'f5',
        'c4', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5', 'c4', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5',
        'c4', 'e', 'a', 'e5', 'a5', 'a4', 'e5', 'a5', 'c4', 'e', 'a', 'e5', 'a5', 'a4', 'e5', 'a5',
        'c4', 'd', 'f#', 'a', 'd5', 'f#4', 'a', 'd5', 'c4', 'd', 'f#', 'a', 'd5', 'f#4', 'a', 'd5',
        'b3', 'd4', 'g', 'd5', 'g5', 'g4', 'd5', 'g5', 'b3', 'd4', 'g', 'd5', 'g5', 'g4', 'd5', 'g5',
        'b3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5', 'b3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5',
        'a3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5', 'a3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5',
        'd3', 'a', 'd4', 'f#', 'c5', 'd4', 'f#', 'c5', 'd3', 'a', 'd4', 'f#', 'c5', 'd4', 'f#', 'c5',
        'g3', 'b', 'd4', 'g', 'b', 'd', 'g', 'b', 'g3', 'b3', 'd4', 'g', 'b', 'd', 'g', 'b'
    ]

    music.play(notes)
