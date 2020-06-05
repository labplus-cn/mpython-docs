Piano
==========

Use the music module and the mPython Board touchpad to make a simple 7-scale touch piano.

::

    from mpython import *               # import mpython module
    import music                        # miport music module

    note=["C4:2","D4:2","E4:2","F4:2","G4:2","A4:2","B4:2"]     # Tuple defining 7 scales

    pStatus,yStatus,tStatus,hStatus,oStatus,nStatus,p0Status=[1]*7  # Key status flag variable
 
    p0 = TouchPad(Pin(33))              # As only 6 touchpads on the mPython Board, one more is required, expand pin P0, corresponding to IO33 of ESP32

    while True:
        if touchPad_P.read()<100 and pStatus==1:      # Detect key press and judge key mark
            music.play(note[0])                       # Play notes
            pStatus=0                                 # Button mark set to 0
        elif touchPad_P.read()>=100:
            pStatus=1
        if touchPad_Y.read()<100 and yStatus==1:
            music.play(note[1])
            yStatus=0
        elif touchPad_Y.read()>=100:
            yStatus=1
        if touchPad_T.read()<100 and tStatus==1:
            music.play(note[2])
            tStatus=0
        elif touchPad_T.read()>=100:
            tStatus=1
        if touchPad_H.read()<100 and hStatus==1:
            music.play(note[3])
            hStatus=0
        elif touchPad_H.read()>=100:
            hStatus=1
        if touchPad_O.read()<100 and oStatus==1:
            music.play(note[4])
            oStatus=0
        elif touchPad_O.read()>=100:
            oStatus=1
        if touchPad_N.read()<100 and nStatus==1:
            music.play(note[5])
            nStatus=0
        elif touchPad_N.read()>=100:
            nStatus=1
        if p0.read()<100 and p0Status==1:
            music.play(note[6])
            p0Status=0
        elif p0.read()>=100:
            p0Status=1

    
.. image:: /../images/classic/piano.gif
