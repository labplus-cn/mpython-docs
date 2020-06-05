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

    - ``loop`` ：If ``loop`` set as ``True`` ，then repeat the adjustment until stop is called (see below) or blocking call is interrupted.
   

.. function:: pitch(frequency, duration=-1, pin=Pin.P6, wait=True)

    - ``frequency``, ``duration``:Play frequency at an integer frequency given a specified number of milliseconds. For example, if the frequency is set to 440 and the length is set to 1000, then we will hear the standard A tune for one second.

        If ``duration`` is negative, the frequency will be played continuously until it is blocked or interrupted, or in the case of a background call, set or call a new frequency stop (see below).

    - ``pin`` pin=Pin.P6, the default is the P6 pin of the control board. Redefinable other pins.

        Please note that you can only play frequencies on one pin at a time.

    - ``wait`` blocking：If ``wait`` is set to ``True``,  it is blocking, otherwise it is not.


.. function:: stop()
    
   Stop all music playback on a given pin.


.. function:: reset()

    Reset the status of the following properties in the following way

        * ``ticks = 4``
        * ``bpm = 120``
        * ``duration = 4``
        * ``octave = 4``

Built-in melody
++++++++

For educational and entertainment purposes, this module contains several example tunes expressed in Python lists. They can be used like this：

    >>> import music
    >>> music.play(music.NYAN)

All music is not protected by copyright, written by Nicholas H. Tollervey and released to the public domain or has an unknown composer, and is protected by fair (educational) terms of use.

They were:

    * ``DADADADUM`` - Opening Ceremony of Beethoven's Fifth Symphony in C minor.
    * ``ENTERTAINER`` - The start portion of Scott Joplin's Ragtime classic "The Entertainer"。
    * ``PRELUDE`` - The start portion of JSBach’s 48 preludes and the first prelude in C major.
    * ``ODE`` - Theme of "Ode to Joy" in D minor by Beethoven's Seventh Symphony.
    * ``NYAN`` - Nyan Cat theme (http://www.nyan.cat/). Composer unknown.
    * ``RINGTONE`` - Ringtone for incoming messages.
    * ``FUNK`` - Trendy bass series for secret agents and criminal masterminds.
    * ``BLUES`` - A boogie-woogie 12-bar blues walking bass。
    * ``BIRTHDAY`` - See the copyright status of “Happy Birthday" : http://www.bbc.co.uk/news/world-us-canada-34332853
    * ``WEDDING`` - Chorus of the bride from Wagner's opera "Lohengrin".
    * ``FUNERAL`` -  “Funeral March”, also known as Frédéric Chopin's Piano Sonata No. 2 B-minor, Op 35.
    * ``PUNCHLINE`` - An interesting clip shows that a joke has been created。
    * ``PYTHON`` - John Philip Sousa's parade “Liberty Bell” aka “Monty Python's Flying Circus” theme (later named after the Python programming language).
    * ``BADDY`` - A bad guy at the entrance to the silent movie era.
    * ``CHASE`` - Chase scenes in the silent movie era.
    * ``BA_DING`` - A short signal that something happened.
    * ``WAWAWAWAA`` - A very sad trombone.
    * ``JUMP_UP`` - Used for games, which means moving up.
    * ``JUMP_DOWN`` - Used for games, means moving down.
    * ``POWER_UP`` - A flaunt, indicating that an achievement was released.
    * ``POWER_DOWN`` - A flaunt, indicating that an achievement was released.
    * ``GE_CHANG_ZU_GUO`` - "Ode to the Motherland", a Chinese local song
    * ``DONG_FANG_HONG`` - "Oriental Red", a Chinese local song
    * ``CAI_YUN_ZHUI_YUE`` - "Rainbow, cloud and Moon), a Chinese local song
    * ``ZOU_JIN_XIN_SHI_DAI`` - "Into A New Era", a Chinese local song
    * ``MO_LI_HUA`` - "Jasmine Flower", a Chinese local song
    * ``YI_MENG_SHAN_XIAO_DIAO`` - "Yimeng Mountain", a Chinese local song

Example::

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
