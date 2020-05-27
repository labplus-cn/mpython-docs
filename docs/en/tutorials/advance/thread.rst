Thread 
=======

.. admonition:: What is Thread?

    A thread is a single sequential control flow in a program. A relatively independent and schedulable execution unit in the process, which is the basic unit of system independent scheduling and dispatching CPU refers to the scheduling unit of the running program. 
    Run multiple threads simultaneously in a single program to complete different tasks, called multi-threading.

  

Create Thread
---------

First to import the ``_thread`` module, which will provide the functions needed. Please note that the module name is  ``_thread`` (the underscore here is not wrong).
We will also import the  ``time`` module, so we can use the ``sleep`` function to introduce some delay in our program. 

::

    import _thread
    import time


Next, we will define the function executed in the thread. Simply loop iteratively 5 times the current running time of printing, each loop will have a certain delay.
We will use the ``sleep`` aspect of the ``time`` module mentioned above to introduce the delay, and the ``time`` module receives the delay in seconds as input. The pararmeter of ``delay`` is the delay in seconds for a single iteration loop.

::

    def print_time( threadName, delay):  
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print ("%s: %s sec" % ( threadName, time.localtime()[5] ))

        print("%s:End" %threadName)
        # exit thread
        _thread.exit()

To start our thread, we simply call the start_new_thread function of the _thread module, specify the first parameter as the _thread module, specify the first parameter as the ``print_time`` function we defined earlier, and specify it as a 2-tuple corresponding to the thread function parameters. 

::

    _thread.start_new_thread( print_time, ("Thread-1", 2, ) ) 
    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )  

Finally, use the ``while`` conditional judgment to make the program in an infinite loop without executing any instructions::

    while True:
        pass


.. literalinclude:: /../../examples/thread/thread_creat.py
    :caption: The complete code is as follows, start two threads and iterate through the printout:
    :linenos: 


The program execution will produce the following results::

    Thread-1: 4 sec
    Thread-1: 6 sec
    Thread-2: 6 sec
    Thread-1: 8 sec
    Thread-1: 10 sec
    Thread-2: 10 sec
    Thread-1: 12 sec
    Thread-1:End
    Thread-2: 14 sec
    Thread-2: 18 sec
    Thread-2: 22 sec
    Thread-2:End

.. Note:: 

    * Multi-threading seems to run in parallel at the same time. In fact, at a certain moment, a CPU core can only perform the tasks of one process.

    * The current multi-process / multi-tasking of computers is actually achieved by accelerating the execution speed of the CPU. Because a CPU can execute hundreds of millions of calculations per second and can switch processes many times, so it can be perceived by humans. In time, it seems that it is actually executing at the same time. 


Thread Lock
---------

In multithreading, all variables are shared by all threads, so any variable can be modified by any thread. Therefore, the biggest danger of sharing data between threads is that multiple threads change a variable at the same time, and the content is messed up.
Lets learn the control to access shared resources. Control is necessary to prevent data corruption. In other words, in order to prevent simultaneous access to the object, we need to use the Lock object.

Thread lock has two states: `Lock` and `Unlock` . It was created in the state of `Unlock` . It has two basic methods，``acquire()`` and ``release()`` .

When the state of the thread is  `Unlock` , ``acquire()`` changes the state to `Lock` and returns immediately.
When the state is `Lock` , ``acquire()`` blocks until the call to ``release()`` in another thread changes it to `Unlock` ，and then the ``acquire()`` call changes it Reset to `Lock` and return. 

.. Attention:: The ``release()`` method should only be called in the `Lock` state; It changes the state to `Unlocked` and returns immediately. If you try to release an unlocked lock, it will raise  `RuntimeError` .


.. literalinclude:: /../../examples/thread/thread_lock.py
    :caption: We changed the above example to a thread lock, as follows. Only one thread can successfully acquire the lock, and then continue to execute the code, the other threads continue to wait until the lock is acquired:
    :linenos: 

Operation result:

    Thread-1: 2 sec
    Thread-1: 4 sec
    Thread-1: 6 sec
    Thread-1: 8 sec
    Thread-1: 10 sec
    Thread-1:End
    Thread-2: 14 sec
    Thread-2: 18 sec
    Thread-2: 22 sec
    Thread-2: 26 sec
    Thread-2: 30 sec
    Thread-2:End


The advantage of locks is to ensure that a certain piece of critical code can only be executed completely by one thread from beginning to end. Of course, there are many disadvantages. First, it prevents multiple threads from executing concurrently. A piece of code that contains a lock can only be used in single-threaded mode Implementation, efficiency is greatly reduced.
