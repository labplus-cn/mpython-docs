.. _array_lib:
:mod:`array` -- Array of Values
======================================

.. module:: array
   :synopsis: Efficient numerical array

This module implements the corresponding :term:`CPython` A subset of modules, as follows. For more details, refer to CPython document: `array <https://docs.python.org/3.5/library/array.html#module-array>`_

Code in supported formats： ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
``L``, ``q``, ``Q``, ``f``, ``d`` (The latter 2 depends on floating point support).

Classes
-------

.. class:: array.array(typecode, [iterable])

   Create an array with elements of the given type. The initial contents of the array are given by 'Iterable'. Empty array were created if not provided. 

    .. method:: append(val)

       Append the new element Val to the end of the array to grow it.

    .. method:: extend(iterable)

       Append the new element contained in the iteration to the end of the array and build on it.
