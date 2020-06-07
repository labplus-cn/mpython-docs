.. _repl:

MicroPython's interactive interpreter mode (also known as REPL)
=======================================================

This section introduces the features of MicroPython's interactive interpreter mode. Its common term is REPL (read-eval-print-loop) to refer to this interactive prompt。

Auto-indent
-----------

When typing a python statement ending in a colon（for example: if, for, while）, the prompt will change to three dots（...），and the cursor will be indented by 4 spaces.
When you click the back button, the next line will continue to be at the same level of normal indentation, or continue to add indentation level if appropriate. If you click the backspace button, an indent level will be withdrawn.

If your cursor stays at the beginning, click the back button to execute the code you entered. The following demonstrates what you will see after entering the for statement (the underline shows the position of the cursor):

    >>> for i in range(3):
    ...     _

If you enter an if statement, an additional level of indentation will be provided:

    >>> for i in range(30):
    ...     if i > 3:
    ...         _

Now type in ``break``, then hit enter, then hit backspace:

    >>> for i in range(30):
    ...     if i > 3:
    ...         break
    ...     _

Lastly, type ``print(i)`` , click Enter, Backspace and Enter:

    >>> for i in range(30):
    ...     if i > 3:
    ...         break
    ...     print(i)
    ...
    0
    1
    2
    3
    >>>

If the first two lines are spaces, no automatic indentation will be applied. This means that you can complete the compound statement input by clicking back twice, and then press the third key to end and execute.

Auto - completion
---------------

When entering an instruction in the REPL, if the input line corresponds to the beginning of the name of something, clicking the TAB key will display what you may enter.
For example, type  ``m`` and click TAB, it will expand to ``machine`` . Type a dot ``.`` and click TAB, you will see the following:

    >>> machine.
    __name__        info            unique_id       reset
    bootloader      freq            rng             idle
    sleep           deepsleep       disable_irq     enable_irq
    Pin

The word will be expanded as much as possible until there are multiple possibilities. For example: type ``machine.Pin.AF3`` and click the TAB key, then it will expand to ``machine.Pin.AF3_TIM`` . Long press TAB for one second, the possible expansions are displayed:

    >>> machine.Pin.AF3_TIM
    AF3_TIM10       AF3_TIM11       AF3_TIM8        AF3_TIM9
    >>> machine.Pin.AF3_TIM

Interrupt a running program
------------------------------

You can interrupt a running program by clicking Ctrl-C. This will trigger a keyboard interrupt and return you to the REPL, provided that your program does not block the keyboard interrupt failure.

For example:

    >>> for i in range(1000000):
    ...     print(i)
    ...
    0
    1
    2
    3
    ...
    6466
    6467
    6468
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
    KeyboardInterrupt:
    >>>

Paste mode
----------

If you want to paste some code into your terminal window, the auto-indent feature will become an obstacle. For example, if you have the following python code: ::

   def foo():
       print('This is a test to show paste mode')
       print('Here is a second line')
   foo()

You tried to paste this code into a regular REPL, then you will see the following:

    >>> def foo():
    ...         print('This is a test to show paste mode')
    ...             print('Here is a second line')
    ...             foo()
    ...
    Traceback (most recent call last):
      File "<stdin>", line 3
    IndentationError: unexpected indent

If you click Ctrl-E, you will enter the paste mode, that is, turn off the automatic indent feature, and change the prompt from ``>>>`` to  ``===`` . Example:

    >>>
    paste mode; Ctrl-C to cancel, Ctrl-D to finish
    === def foo():
    ===     print('This is a test to show paste mode')
    ===     print('Here is a second line')
    === foo()
    ===
    This is a test to show paste mode
    Here is a second line
    >>>

Paste mode allows pasting blank lines and compiling the pasted text as a file. Click Ctrl-D to exit paste mode and start compilation.

Soft reset
----------

A soft reset will reset the Python interpreter, but it will not reset the way you connect to the MicroPython board (USB-serial or WiFi). 

You can click Ctrl-D to perform a soft reset from the REPL, or execute it from your python code: ::

    raise SystemExit

Example：If you reset your MicroPython board and execute the dir() If you reset your MicroPython board and execute the:

    >>> dir()
    ['__name__', 'pyb']

Now create some variables and repeat the dir() instruction:

    >>> i = 1
    >>> j = 23
    >>> x = 'abc'
    >>> dir()
    ['j', 'x', '__name__', 'pyb', 'i']
    >>>

Now, if you click Ctrl-D and repeat the dir() command, you will find that the variable no longer exists:

.. code-block:: python

    PYB: sync filesystems
    PYB: soft reboot
    MicroPython v1.5-51-g6f70283-dirty on 2015-10-30; PYBv1.0 with STM32F405RG
    Type "help()" for more information.
    >>> dir()
    ['__name__', 'pyb']
    >>>

Special variable _ (underscope)
-----------------------------------

When using REPL, make calculations and get results. MicroPython stores the result of the previous statement in the variable _（underscore）. You can use underscores to store results in variables. Example:

    >>> 1 + 2 + 3 + 4 + 5
    15
    >>> x = _
    >>> x
    15
    >>>

Original mode
--------

The original mode is not for routine, but for programming. 

Click Ctrl-A to enter the original mode. Send your python code and click Ctrl-D. The Ctrl-D key will be recognized as "OK" , then compile and execute the python code.
All outputs (or faults) will be sent back. Clicking Ctrl-B will launch the original mode and return to the regular (also known as friendly) REPL.

``tools/pyboard.py`` 程序使用原始REPL来在MicroPython板上执行python文件。
