:mod:`uio` -- I/O Stream
==================================

.. module:: uio
   :synopsis: I/O stream

This module implements the corresponding :term:`CPython` a subset of modules, as follows. Refers to CPython document for details: `io <https://docs.python.org/3.5/library/io.html#module-io>`_

This module contains other types of stream (class file) objects and helping functions.

Conceptual level
--------------------

.. admonition:: differences with CPython
   :class: attention

   As described in this section, the conceptual hierarchy of stream base classes is simplified in MicroPython.

（摘要）基本流类作为所有具体类行为的基础，在CPython中遵循少量二分法（成对分类）。
在MicroPython中，它们稍微简化并隐含以实现更高的效率并节省资源。

n important dichotomy in CPython is unbuffered flow and buffered flow. In MicroPython, all streams are currently unbuffered.
This is because all modern operating systems, even many RTOS and file system drivers, are already performing buffering around them.
Adding another layer of buffer is counterproductive（a problem called “bufferbloat”）and takes up valuable memory.
Note that there are still situations where buffering can be useful, so we may introduce optional buffering support later.

But in CPython, another important dichotomy is related to "buffering" - whether a stream can cause short reads / writes.
Short reads are when a user requests, for example, 10 bytes from a stream, but similar for writes. In CPython, unbuffered streams are automatically sensitive to short operations, and buffering is their guarantee.
No short read / write is an important feature because it allows for simpler and more efficient development of programs - something MicroPython really needs.
Therefore, although MicroPython does not support buffering streams, it still provides non short operation streams.
Whether there will be short-term operations depends on the needs of each specific category, but it is highly recommended that developers support non short-term operations for the reasons described above.
For example, MicroPython sockets guarantee against short reads / writes. In fact, at this point, there is no example of a short operation flow class in the core, and one is a port specific class, where this requirement is determined by the hardware characteristics.

In the case of non blocking flow, non short operation behavior becomes tricky. Blocking and non blocking behavior is another CPython dichotomy, which is fully supported by MicroPython.
Nonblocking streams never wait for data to arrive or be written - they may read / write, or indicate a lack of data (or the ability to write to data).
Obviously, this conflicts with the "non short operation" policy. In fact, in CPython, the situation of non blocking buffer (and this non short operation) flow is puzzling - in some places, this combination is forbidden, in some cases, it is undefined or just not recorded, in some cases, it will cause lengthy exceptions. This problem is much simpler in micropython: non blocking flows are important for efficient asynchronous operations, so this attribute has an advantage over "no short ops.".

So the final dichotomy is binary to text flow. MicroPython certainly supports these, but in CPython, text streams themselves are buffered, they are not in micropython.

(in fact, this is one of the cases where we might introduce buffer support.)

Note that for efficiency, MicroPython does not provide an abstract base class corresponding to the above hierarchy, and it is not possible to implement or subclass stream classes in pure python.

Function
---------

.. function:: open(name, mode='r', **kwargs)

   Open a file. The built-in ``open()`` function is an alias for this function.
Class
-------

.. class:: FileIO(...)

    This is the type of file opened in binary mode, such as using ``open(name, "rb")`` 
    You should not instantiate this class directly.

.. class:: TextIOWrapper(...)

    This is the type of file opened in text mode, such as using ``open(name, "rt")`` 。
    Not to instantiate this class directly.

.. class:: StringIO([string])

.. class:: BytesIO([string])


    Memory file class object for I/O. ``StringIO`` For text mode I/O（Similar to a normal file opened with the “t” modifier）。``BytesIO`` for binary modeI ​​/ O（Similar to a normal file opened with the “b” modifier）. To use the string parameter to specify the initial contents of the class file object (expected to be a normal string stringIO or a byte object BytesIO).
    All common methods of documentation, such as ``read()`` ， ``write()`` ， ``seek()`` ， ``flush()`` ， ``close()``  The following methods are available on these objects:


    .. method:: getvalue()

       Gets the current contents of the underlying buffer that holds the data. 


.. class:: StringIO(alloc_size)
.. class:: BytesIO(alloc_size)

    Create an empty `StringIO`/ `BytesIO` object, Pre-allocated to accommodate *alloc_size* bytes. This means that writing the number of bytes does not cause the buffer to be reallocated, so there will be no out of memory or memory fragmentation.
    These constructors are MicroPython extensions and are recommended only for special cases and system level libraries, not end-user applications.

    .. admonition:: Difference to CPython
        :class: attention

        These constructors are MicroPython extensions.
