Musical Box
==========

Built-in Songs in the music module, use user button A & B (on the mPython Board) for selection (up, down)！

::

    from mpython import *
    import music

    aStatus=1
    bStatus=1
    index=0

    song=[music.DADADADUM,music.ENTERTAINER,music.PRELUDE,music.ODE,music.NYAN,music.RINGTONE,
        music.BLUES,music.BIRTHDAY,music.WEDDING,music.FUNERAL,music.PUNCHLINE,music.PYTHON,music.BADDY
        ]
    def displaySong():
        oled.fill(0)
        oled.DispChar("歌曲:%d" %(index+1),45,25)
        oled.show()
        

    while True:
        if button_b.value()==0 and aStatus==1:
                music.play(song[index],wait=False)
                oled.show()
                displaySong()
                index+=1
                aStatus=0
                if index>=len(song):
                    index=0
        elif button_b.value()==1:
            aStatus=1
        
            oled.show()
        if button_a.value()==0 and bStatus==1:
                music.play(song[index],wait=False)
                displaySong()
                index-=1
                bStatus=0
                if index<0:
                    index=len(song)-1
        elif button_a.value()==1:
            bStatus=1


Other than playing music built-in music, you also can compose your own！
