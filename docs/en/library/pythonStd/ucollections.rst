:mod:`ucollections` -- Container Data Type
=====================================================

.. module:: ucollections
   :synopsis: Container Data Type

This module implements the corresponding :term:`CPython` a subset of modules, as follows. Refers to CPython document for details. : `collections <https://docs.python.org/3.5/library/collections.html#module-collections>`_

This module implements advanced collection and container types to hold / accumulate various objects。

Type
-------

.. function:: deque(iterable, maxlen[, flags])

    Deques（Dual terminal queue）is a list type container, Support 0 (1) append and pop-up from either side of the dual end queue. Create a new deques with the following parameters：

    * iterable must be an empty tuple and the newly created deque must be empty. 
    * Maxlen must be specified and double ended queues limited to this maximum length. Once the two terminal queue is full, any new items added will discard as the other party's items.
    When adding item, the optional flag can be 1 to check for overflows.

    In addition to supporting ``bool`` and ``len`` deque object also has the following methods：

     .. method:: deque.append(x)

    Add x to the right of deque. If overflow checking is enabled and there is no space left, an index error is raised.

     .. method:: deque.popleft()

     Remove and return an item from the left side of deque. If no entry appears, an index error will be caused.


.. function:: namedtuple(name, fields)

    THis is factory function, Used to create a new namedtuple type with a specific name and a set of fields.
    A namedtuple is a subclass of a tuple, which allows access to its fields not only through numeric indexes, but also using the attribute access syntax of the symbolic field name.
    A field is a string sequence of specified field names. For compatibility with CPython, it can also be a string called a space delimited field (but less efficient).
    Example::

        from ucollections import namedtuple

        MyTuple = namedtuple("MyTuple", ("id", "name"))
        t1 = MyTuple(1, "foo")
        t2 = MyTuple(2, "bar")  
        print(t1.name)
        assert t2.name == t2[1]

.. function:: OrderedDict(...)

    ``dict`` type subclass，It memorizes and preserves the order in which keys are added. When traversing an ordered dictionary, keys / items return in the order they were added::

        from ucollections import OrderedDict

        # To make benefit of ordered keys, OrderedDict should be initialized
        # from sequence of (key, value) pairs.
        d = OrderedDict([("z", 1), ("a", 2)])
        # More items can be added as usual
        d["w"] = 5
        d["b"] = 3
        for k, v in d.items():
            print(k, v)

    Output::

        z 1
        a 2
        w 5
        b 3
