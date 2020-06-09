Assembly Instruction
====================

Mark
------

* Mark (INNER1)

This defines a flag for the transfer instruction. Therefore, elsewhere in the code, ``b(INNER1)`` will cause the instruction to continue to execute after the instruction is marked.

Define inline data
--------------------

The following assembly instructions help embed data into assembly code.

* data(size, d0, d1 .. dn)

Data instructions create an array of data values in memory. The first parameter specifies the size of subsequent parameters (in bytes). Therefore, the first statement below will cause the assembler to convert three bytes
(Its value is 2, 3, 4) into a continuous storage unit, and the second statement will make it send two four-byte words.

::

    data(1, 2, 3, 4)
    data(4, 2, 100000)

Data values larger than one byte will be stored in memory in low-order first format.

* align(nBytes)

Align the following instructions with n-byte values. ARM Thumb-2 instructions must be two-byte aligned, so it is recommended to send   ``align(2)`` after the ``data`` instruction and before any subsequent code 
This will ensure that the code will run when any data array is any size.
