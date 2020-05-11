:mod:`uheapq` -- Heap Queue Algorithm
=====================================

.. module:: uheapq
   :synopsis: heap queue algorithm

This module implements the corresponding :term:`CPython` A subset of modules, as described below. Refers to CPython document for details: `heapq <https://docs.python.org/3.5/library/heapq.html#module-heapq>`_

This T module implements the heap queue algorithm.

A heap queue is a way to store a list of its elements.

Function
---------

.. function:: heappush(heap, item)

   Push the ``item`` onto the ``heap``.

.. function:: heappop(heap)

   Pop the first item from the ``heap``, and return it.  Raises IndexError if
   heap is empty.

.. function:: heapify(x)

   Convert the list ``x`` into a heap.  This is an in-place operation.
