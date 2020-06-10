:mod:`sys` -- Specific System Functions
=======================================

.. module:: sys
   :synopsis: Specific System Functions


The system module provides functions and variables related to the MicroPython operating environment.

This module implements the corresponding :term:`CPython` a subset of modules, as follows. See the CPython document for details: `sys <https://docs.python.org/3.5/library/sys.html#module-sys>`_

Functions
---------

.. function:: exit(retval=0)

   Terminate the current program with the given exit code. On this basis, this function is upgraded to ``SystemExit`` . If a parameter is given, its value is given as a parameter  ``SystemExit``  .

.. function:: print_exception(exc, file=sys.stdout)


    By tracing back to class object file（or ``sys.stdout`` by defauit）to print exceptions. 

.. admonition:: differences with CPython
    :class: attention

    This ``traceback``  simplified versions of functions that appear in CPython modules. 。The difference with  ``traceback.print_exception()`` , This function only uses exception values instead of exception types, exception values and backtracking objects; the file parameter should be positional; other parameters are not supported.
    ``traceback``  CPython compatible modules can be found ``micropython-lib`` 。

Constant
---------

.. data:: argv

    Variable parameter list of current program launch.

.. data:: byteorder

    Byte order of the system（ ``little`` or ``big`` ）。

.. data:: implementation

    Objects that contain information about the current Python implementation. For MicroPython，it has the following attributes：

    * *name* - string "micropython"
    * *version* - Tuple (primary, secondary, micro), e.g. (1, 7, 0)

    This method is recommended to identify MicroPython on different platforms.


    Example::

        >>> print(sys.implementation)
        (name='micropython', version=(1, 9, 1))

.. data:: maxsize

    The maximum integer type value that can be saved on the current platform，If it is less than the platform maximum.
    （For MicroPython ports without INT support）。

    This attribute is useful for detecting the "bits" (32-bit, 64 bit, etc.) of the platform. It is not recommended to directly compare this property with a value, but to calculate the number of digits in it ::::

        bits = 0
        v = sys.maxsize
        while v:
            bits += 1
            v >>= 1
        if bits > 32:
            # 64-bit (or more) platform
            ...
        else:
            # 32-bit (or less) platform
            # Note that on 32-bit platform, value of bits may be less than 32
            # (e.g. 31) due to peculiarities described above, so use "> 16",
            # "> 32", "> 64" style of comparisons.

.. data:: modules

    Loaded module dictionary. In some migration versions, it may not be included in built-in modules.

.. data:: path

    List of variable directories to search for import modules.

.. data:: platform

   Gets the MicroPython operating platform.

.. data:: stderr

  Standard error ``stream``

.. data:: stdin

   Standard input ``stream``

.. data:: stdout

   Standard output ``stream``

.. data:: version

    returns MicroPython language version, string

.. data:: version_info

   returns MicroPython language version, restructured tuple
