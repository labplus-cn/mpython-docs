:mod:`micropython` -- Access and control of MicroPython internal
=============================================================

.. module:: micropython
   :synopsis: Access and control of MicroPython from internal


Function
---------

.. function:: const(expr)

  Used to declare that an expression is a constant so that compilation can optimize it. The use of this function shall be as follows::

    from micropython import const

    CONST_X = const(123)
    CONST_Y = const(2 * CONST_X + 1)
    print(CONST_X)
    print(CONST_Y)

  Operation result::

    >>>123
    >>>247



  Constants declared in this way can still be accessed as global variables from outside the modules they declare. On the other hand, if a constant begins with an underscore, it is hidden.
  It is not available as a global variable and does not take up any memory during execution. 

  This ``const`` function is directly recognized by the MicroPython parser and provided as part of the  :mod:`micropython`  module, It is mainly used to write scripts running under CPython and MicroPython by following the above patterns.



.. function:: opt_level([level])

  If the level is given, this function sets the script and returns the subsequent compilation optimization level ``None`` . Otherwise, return to the current optimization level.

  The optimization level controls the following compilation functions:

    * Assertion: Assertion statement is enabled and compiled into bytecode at level 0; Assertions at level 1 and higher are not compiled. 
    * Built-in ``__debug__`` variables: At level 0, this variable expands to ``True``; At level 1 and higher, it extends to ``False``.
    
    * Source code line number: Source line numbers are stored with bytecode at levels 0, 1 and 2 so that exceptions can report their occurrence; line numbers at levels 3 and higher are not stored. 

  The default optimization level is usually 0. 

.. function:: alloc_emergency_exception_buf(size)

  Set the safe RAM allocation in case of emergency (stack overflow, general RAM shortage, etc.) so that RAM is still available in case of emergency. 

    - ``size``: The safe size of the remaining ram is generally 100.


  A good way to use this function is at the beginning of the main script（such as ``boot.py`` or ``main.py`` ），
  The emergency exception buffer will then take effect for all subsequent code. 


.. function:: mem_info([verbose])

  Function description： Print current memory usage (including stack and heap usage). 

  .. Note::

      If the parameter level (any data type) is given, more detailed information will be printed, which will print the entire heap, indicating which memory blocks are used and which are free. 

  Parameter not given::

    >>>micropython.mem_info()
    stack: 736 out of 15360
    GC: total: 48000, used: 7984, free: 40016
    No. of 1-blocks: 72, 2-blocks: 31, max blk sz: 264, max free sz: 2492
    >>>

  Given parameter::

      >>>micropython.mem_info("level")
    stack: 752 out of 15360
    GC: total: 48000, used: 8400, free: 39600
    No. of 1-blocks: 82, 2-blocks: 36, max blk sz: 264, max free sz: 2466
    GC memory layout; from 3ffc4930:
    00000: h=ShhBMh=DhBhDBBBBhAh===h===Ahh==h==============================
    00400: ================================================================
    00800: ================================================================
    00c00: ================================================================
    01000: =========================================hBh==Ah=ShShhThhAh=BhBh
    01400: hhBhTShh=h==h=hh=Bh=BDhhh=hh=Bh=hh=Bh=BhBh=hh=hh=h===h=Bhh=h=BhB
    01800: h=hh=h=Bh=hBh=h=hBh=h=hBh=h=h=hh=======h========================
    01c00: ============================================Bh=hBhTh==hh=hh=Sh=h
    02000: h==Bh=B..h...h==....h=..........................................
          (37 lines all free)
    0b800: ........................................................
    >>>

.. function:: qstr_info([verbose])

  Print the number of strings currently used in memory, occupied memory size and other information. 

  .. Note::

    If the parameter is given, the specific string information will be printed out. The printed information depends on the actual situation, including the number of strings entered and the amount of ram they use.
    In verbose mode, it prints out the names of all strings. 

  Parameter not given::

    >>>micropython.qstr_info()  
    qstr pool: n_pool=1, n_qstr=4, n_str_data_bytes=31, n_total_bytes=1135
    >>>
    
  Given parameter::

    >>>micropython.qstr_info("level")  
    qstr pool: n_pool=1, n_qstr=4, n_str_data_bytes=31, n_total_bytes=1135
    Q(b)
    Q(2)
    Q(asdfa222)
    Q(level)
    >>>

.. function:: stack_use()

  Returns an integer representing the number of stacks currently in use. This absolute value is not particularly useful, but should be used to calculate stack usage differences at different points.

  Examples::

    >>>micropython.stack_use()
    720

.. function:: heap_lock()

  Lock the heap. When the heap is locked, no operation will allocate memory. If a memory allocation operation is attempted, a memoryerror error will be generated. 

  

.. function:: heap_unlock()

  Unlock heap

.. function:: kbd_intr(chr)

  Set the character that will throw the keyboardinterrupt exception. By default, it is set to 3 during script execution, corresponding to Ctrl-C.
  Passing - 1 to this function disables capture of Ctrl-C, and passing 3 restores it.

  If the stream is used for other purposes, this function can be used to prevent capture of Ctrl-C on the incoming character stream that is commonly used for REPL.

.. function:: schedule(func, arg)

  Schedule function func to execute “quickly”. The function passes the value arg as its single parameter. “Quickly” means that the MicroPython runtime will do its best to perform this function as early as possible.
  Because it also tries to improve efficiency, and the following conditions are true：

  - The scheduled function will never preempt another scheduled function. 
  - Planning functions are always executed “between opcodes”, which means that all basic Python operations, such as attaching to a list, are guaranteed to be origin.
  - A given port can define a "critical area" within which the scheduling function will never be executed. Could schedule functions in a critical area, but they will not be performed until you exit the area. An example of a critical area is preemption interrupt handler (IRQ).

  The purpose of this function is to schedule callbacks from preemptive IRQ. Such IRQ limits the code that runs in IRQ (for example, heap may be locked), and schedules functions that are called later will relieve these restrictions.

  Note：If ``schedule()`` is called from preemptive IRQ, if memory allocation is not allowed and the callback ``schedule()`` to transmit directly by binding method,  it will fail.
  This is discussed in detail in the reference documentation under “creating Python objects”. 

  There is a limited stack to hold the scheduled functions. If the stack is full, ``schedule()`` ,  ``RuntimeError`` will be raised.

