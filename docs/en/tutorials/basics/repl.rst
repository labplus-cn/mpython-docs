REPL
=====

One of the main advantages of using MicroPython is the interactive REPL. REPL (read-eval-print loop) stands for read-evaluation-output loop.
REPL is very helpful for learning a new programming language, because it can immediately respond to programs written by beginners, which means that you execute the code and can view the results immediately, avoiding the cumbersome steps to compile and upload. 
Install the cp2104 serial driver in order for REPL to operate on windows on this this mPython Board.


Serial connection
----------

To access via USB-serial, you need to use serial terminal software. On Windows such as kitty, xshell are good choices. Set the serial port baud rate to 115200, you can start playing MicroPython. To access via USB-serial, you need to use serial terminal software. 

After establishing the connection through the serial port, you can test whether it is working by pressing the Enter key a few times to test whether it is working properly. If it works, you can see the Python REPL prompt, which is expressed as ``>>>`` 。

Use REPL
----------

Once prompted, you can start trying! After pressing Enter, you can type anything at the prompt. 
MicroPython will run the code you entered and print the results (if any)；If the text entered is wrong, an error message will be printed.

Try typing the following at the prompt::

    >>> print('hello mPython')
    hello mPython


Please note that you do not need to type ``>>>`` arrows, they indicate that you should type text after this prompt, and the next line is the content of the response.

If you already know some python, you can try some basic commands now. E.g. ::

    >>> 1+2
    3
    >>> 1/2
    0.5
    >>> 12*34
    408


You can try to download mPython to display characters on the OLED display::

    >>> from mpython import *
    >>> oled.DispChar('hello,world!',0,0)
    >>> oled.show()
    >>> 

.. Note::

    ``oled.DispChar(str,x,y)``   ``str`` is the character string to be displayed， ``x`` 、``y`` are the x and y coordinates of the display starting point。
    Then use ``oled.show()`` to refresh the screen, the string can be displayed on the OLED display. You can try to display arbitrary strings in other locations.



Line Editor
~~~~~~~~~~~~

You can use the left and right arrow keys to move the cursor to edit the currently entered line；Press the Home key or ctrl-A to move the cursor to the beginning of the line, press End or ctrl-E to move to the end of the line; the Delete key or backspace key is used to delete.

Enter History
~~~~~~~~~~~~~

REPL will remember a certain amount of the first few lines of text you entered (up to 8 lines on ESP32). 
To call the previous line, use the up and down arrow keys.

Tab Key
~~~~~~~~~~~~~~

Tab key to view the list of all members in the module. This is very useful for finding out the functions and methods that a module or object has.
Suppose you imported the machine in the above example and then typed  ``.`` and then press the Tab key to view the list of all members of the machine module::

    >>> machine.
    __class__       __name__        ADC             DAC
    DEEPSLEEP       DEEPSLEEP_RESET                 EXT0_WAKE
    EXT1_WAKE       HARD_RESET      I2C             PIN_WAKE
    PWM             PWRON_RESET     Pin             RTC
    SLEEP           SOFT_RESET      SPI             Signal
    TIMER_WAKE      TOUCHPAD_WAKE   Timer           TouchPad
    UART            ULP_WAKE        WDT             WDT_RESET
    deepsleep       disable_irq     enable_irq      freq
    idle            mem16           mem32           mem8
    reset           reset_cause     sleep           time_pulse_us
    unique_id       wake_reason
    >>> machine.


Line continue and auto indent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Something you type will need to “continue”, that is, more lines of text are needed to generate the correct Python statement. under these circumstances,
The prompt will change to ``...`` and the cursor will automatically be indented by the correct amount so that you can immediately start typing the next line.
Try this by defining the following function::


    >>> def toggle(p):
    ...    p.value(not p.value())
    ...    
    ...    
    ...    
    >>>

In the above, you need to press the Enter key three times in a row to complete the compound statement (that is, there are only dots on the three lines). Another way to complete the compound statement is to press the backspace key to reach the beginning of the line, and then press Enter. (If you make a mistake and want to quit, then press ctrl-C, all lines will be ignored.)

You just defined the function function to flip the pin level. The pin object you created earlier should still exist.
(If not, you need to recreate it), you can use the following command to flip the LED::

    >>> toggle(pin)

Now let's flip the LEDs in a loop (if you don't have LEDs, then you can print some text instead of calling toggle to see the effect)：

    >>> import time
    >>> while True:
    ...     toggle(pin)
    ...     time.sleep_ms(500)
    ...    
    ...    
    ...    
    >>>

This will flip the LED at 1 Hz (on half a second, off half a second). To stop switching press ``ctrl-C`` , this will cause keyboard interrupt exception and exit the loop.


Paste mode
~~~~~~~~~~

Press ``ctrl-E`` to enter the special paste mode, you can copy and paste a large block of text into the REPL. If you press ctrl-E, you will see the paste mode prompt::

    paste mode; Ctrl-C to cancel, Ctrl-D to finish
    === 

You can then paste (or type) your text. Please note that there are no special keys or commands that work in paste mode (eg Tab or Backspace),
they are just accepted as they are. Press``ctrl-D`` to finish entering text and execute.

Other control commands
~~~~~~~~~~~~~~~~~~~~~~

There are four other control commands：

* Ctrl-A on the blank line will enter the original REPL mode. This is similar to permanent paste mode, except that characters are not echoed.

* Ctrl-B in the blank space goes to normal REPL mode.

* ``Ctrl-C`` cancels any input or interrupts the currently running code.

*  ``Ctrl-D`` on the blank line will perform a soft restart.


