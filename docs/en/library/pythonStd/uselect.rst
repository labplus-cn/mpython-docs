:mod:`select` -- Waiting for I/O efficiently
========================================================================

.. module:: select
   :synopsis: wait for events on a set of streams

This module implements the corresponding :term:`CPython` a subset of modules, as follows, refers to CPython document for details: `select <https://docs.python.org/3.5/library/select.html#module-select>`_

This module provides the function of waiting for multiple events ``streams``（Ready to operate selection flow）.

Function
---------

.. function:: poll()

Create an instance of the Poll class.

.. function:: select(rlist, wlist, xlist[, timeout])

When the monitoring object is readable or writable, once the status of the monitored object changes, the result (blocking thread) is returned.
This function is for compatible but inefficient. It is recommended to use the poll function.

- ``rlist``：Array of file descriptors waiting to be read ready
- ``wlist``：Array of file descriptors waiting to be written
- ``xlist``：Array waiting for exception
- ``timeout``：Waiting time in seconds


.. _class: Poll

 Poll class
--------------

method
~~~~~~~

.. method:: poll.register(obj[, eventmask])

  Register an object for monitoring, `eventmask` is logic OR：stream

   - ``obj`` :Monitored objects


      - ``select.POLLIN``  - Read available data
      - ``select.POLLOUT`` - Write more data
      - ``select.POLLERR`` - Error occurred
      - ``select.POLLHUP`` - Flow end / connection end detection

      Attention to signs like ``uselect.POLLHUP`` and ``uselect. Is POLLERR`` valid for input `eventmask` (These are the unsolicited events from return poll(), whether they are requested or not）. 
      This semantics is based on POSIX.

   ``eventmask`` defaults to ``select.POLLIN | select.POLLOUT``.


   This function can be called multiple times for the same `obj` . Continuous call will update the value of `eventmask` to `eventmask` of OBJ（It will be shown as ``modify()`` ）. 

.. method:: poll.unregister(obj)

   Unregister OBJ from polling.

.. method:: poll.modify(obj, eventmask)

   Modify registered object ``obj`` , If OBJ is not registered, an ENOENT error occurs for OSErrorr.

.. method:: poll.poll([timeout])

   Optional timeout waiting for at least one registered object to be ready or with exception conditions（in milliseconds）（If timeout Arg or - 1 is not specified, there is no timeout）. 

   Returns a tuple ( ``obj``, ``event``, ...)of the list.  There may be other elements in the tuple, depending on the platform and version, so don't assume its size is 2.  

   The event element specifies the event that occurs in the flow, And it's ``uselect.POLL*`` a combination of the above constants. What needs to be noted is the logo ``uselect.POLLHUP`` , and ``uselect.POLLERR`` can be returned at any time (even if not required), Appropriate action must be taken (from investigating unregistered and potentially closed flows), Otherwise, all further calls to ``poll()`` can use these flag settings to immediately return to this stream again.
   
   If it times out, an empty list is returned.

   .. admonition:: Difference to CPython
      :class: attention

      The returned tuple may contain more than 2 elements, as described above.

.. method:: poll.ipoll([timeout])

   and :meth:`poll.poll` similar, but returns an iterator that produces all tuples of the called function. This function provides an efficient, non location polling method in the stream.


   .. admonition:: differences with CPython
      :class: attention

      This function is an extension of MicroPython.
