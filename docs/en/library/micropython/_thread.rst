
:mod:`_thread` --- Threads
==========================

This module provides low-level primitives for handling multiple threads (also known as lightweight processes or tasks)-multiple control threads share their global data space. 
For synchronization, a simple lock (also called a mutex or binary semaphore) is provided.

When a thread-specific error occurs, an exception will be raised by RuntimeError.

Quick use example::

    import _thread
    import time

    def th_func(delay, id):
        while True:
            time.sleep(delay)
            print('Running thread %d' % id)

    for i in range(2):
        _thread.start_new_thread(th_func, (i + 1, i))

Method
~~~~~~~

.. method:: _thread.start_new_thread（function，args [，kwargs]）

Start a new thread and return its identifier. The thread uses the parameter list args (must be a tuple) to execute the function. Optional kwargs parameter specifies a dictionary of keyword parameters. 
When the function returns, the thread will exit silently. When the function terminates with an unhandled exception, the stack trace is printed, and then the thread exits (but other threads continue to run). 

.. method:: _thread.exit()

SystemExit exception is triggered. If not captured, this will cause the thread to exit silently。

.. method:: _thread.allocate_lock()

Return a new locked object. The method of locking is as follows. The lock is initially unlocked.

.. method:: _thread.get_ident()

Returns the thread identifier of the current thread. This is a non-zero integer. Its value has no direct meaning; 
It is intended to be used as a magic cookie for indexing a dictionary of thread-specific data. When the thread exits and creates another thread, the thread identifier can be retrieve。

.. method:: _thread.stack_size([size])

Returns the thread stack size (in bytes) used when creating a new thread. The optional size parameter specifies the stack size of the thread used for subsequent creation and must be 0 (use the platform or configured default value) or a positive integer value of at least 4096 (4KiB).
4KiB is the minimum stack size value currently supported to ensure that the interpreter has enough stack space. 

Object
~~~~~~~

.. object:: _thread.LockType

Type of locked object. 



Lock class 
~~~~~~~

.. class:: Lock

The threading module provided by Python contains an easy-to-implement locking mechanism that enables synchronization between threads. Create a new lock by calling the Lock() method.
New lock object acquisition (blocking) method is used to force threads to run synchronously. Optional blocking parameter allows you to control whether the thread is waiting to acquire the lock.

Method
-----

The lock object has the following methods：

.. method::  lock.acquire(waitflag = 1，timeout = -1)

Without any optional parameters, this method acquires the lock unconditionally, and if necessary, waits for it to be released by another thread (only one thread can acquire the lock at a time-that's why they exist). 

If there is an integer  ``waitflag`` parameter, the operation depends on its value: if it is zero, the lock is only acquired when the lock is acquired immediately without waiting, and if it is non-zero, it is acquired unconditionally as described above locking. 

If the floating-point timeout parameter is present and positive, it specifies the maximum wait time (in seconds) before returning.     -ve timeout parameter specifies unlimited waiting. If ``waitflag`` is zero, you cannot specify a timeout.

``True`` returns the value if the lock is successfully acquired, otherwise the return value is ``False`` .

.. method::  lock.release()

Release the lock. The lock must be acquired first, but not necessarily the same thread. 

.. method::  lock.locked()

Returns the state of the lock：True means acquired by a thread, False means no.

In addition to these methods, you can also use locked objects through the with statement, for example::

    import _thread

    a_lock = _thread.allocate_lock()
    with a_lock:
        print("a_lock is locked while this executes")
