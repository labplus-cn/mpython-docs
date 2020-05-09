:mod:`gc` --  Reclaim memory fragments
==========================================

.. module:: gc
   :synopsis:  Reclaim memory fragments

This module implements the corresponding :term:`CPython` A subset of modules, as described below. For more information, see the original CPython documentation:`array <https://docs.python.org/3.5/library/gc.html#module-gc>`_.

Functions
---------

.. function:: enable()

Enable automatic memory defragmentation

.. function:: disable()

  Disable auto recycle. Heap memory can still be allocated, but it can be allocated through :meth:`gc.collect` Function to manually reclaim memory fragments.


.. function:: collect()

  Reclaim memory fragmentation.

.. function:: mem_alloc()

  Returns the number of bytes of heap RAM allocated

   .. admonition::  differences with CPython
      :class: attention
      

      This function is an extension of micropython.

.. function:: mem_free()

   Returns the number of bytes of available heap ram, or - 1 if the number is unknown

   .. admonition:: differences with CPython
      :class: attention

       This function is an extension of micropython.

.. function:: isenabled()

  Determine whether to start automatic memory fragment collection.

.. function:: threshold([amount])

   Set or query other GC allocation thresholds. In general, collections are triggered only when a new allocation cannot be satisfied, that is, when there is not enough memory (OOM). 
   If this function is called, in addition to OOM, a collection is triggered every time a large number of bytes are allocated (in total, because so many bytes were allocated last time).
   Amount is usually specified to be less than the full heap size, with the intention of triggering the collection before the heap runs out, and the hope is that the early collection will prevent excessive memory fragmentation.
   This is a heuristic measure whose effect varies from application to application and the best value of the quantity parameter.
   Calling a function without parameters returns the current value of the threshold value. A value of - 1 indicates the disabled allocation threshold.
   .. admonition:: differences with CPython
      :class: attention

      The function is a MicroPython extension. Cpython has similar function - ``set_threshold()`` However, due to different GC implementations, its signature and semantics are different.
