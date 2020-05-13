:mod:`ustruct` -- Pack and decompressing raw data types
======================================================

.. module:: ustruct
   :synopsis: Pack and decompressing raw data types

This module implements the corresponding :term:`CPython` a subset of modules, as follows. Refers to CPython document for details: `struct <https://docs.python.org/3.5/library/struct.html#module-struct>`_


Format string
--------------

Format strings are a mechanism to specify the expected layout when pack and unpack data. In addition, there are special characters for controlling byte order, size, and alignment.

Byte order, size, and alignment
^^^^^^^^^^^^^^^^^^^

By default, type C is represented in the native format and byte order of the machine，And if necessary, correct alignment by skipping padding bytes (according to the rules used by the C compiler).
Or, depending on the table below, the first character of the format string can be used to indicate the byte order, size, and alignment of the packed data：

+-----------+------------------------+----------+-----------+
| Character | Byte order             | Size     | Alignment |
+===========+========================+==========+===========+
| ``@``     | native                 | native   | native    |
+-----------+------------------------+----------+-----------+
| ``=``     | native                 | standard | none      |
+-----------+------------------------+----------+-----------+
| ``<``     | little-endian          | standard | none      |
+-----------+------------------------+----------+-----------+
| ``>``     | big-endian             | standard | none      |
+-----------+------------------------+----------+-----------+
| ``!``     | network (= big-endian) | standard | none      |
+-----------+------------------------+----------+-----------+

Format character
^^^^^^^^

Format characters have the following implication; Depending on the type, the conversion between C and Python values should be obvious. "Standard size" column refers to the size (in bytes) of the packed value when the standard size is used;
That is, when one of the format strings starts'<'，'>'，'!' or  '='. When using native size, the size of the packaging value depends on the platform.

+--------+--------------------------+--------------------+----------------+
| Format | C Type                   | Python type        | Standard size  |
+========+==========================+====================+================+
| ``x``  | pad byte                 | no value           |                |
+--------+--------------------------+--------------------+----------------+
| ``c``  | :c:type:`char`           | bytes of length 1  | 1              |  
+--------+--------------------------+--------------------+----------------+
| ``b``  | :c:type:`signed char`    | integer            | 1              |
+--------+--------------------------+--------------------+----------------+
| ``B``  | :c:type:`unsigned char`  | integer            | 1              |
+--------+--------------------------+--------------------+----------------+
| ``?``  | :c:type:`_Bool`          | bool               | 1              |
+--------+--------------------------+--------------------+----------------+
| ``h``  | :c:type:`short`          | integer            | 2              |
+--------+--------------------------+--------------------+----------------+
| ``H``  | :c:type:`unsigned short` | integer            | 2              |
+--------+--------------------------+--------------------+----------------+
| ``i``  | :c:type:`int`            | integer            | 4              |
+--------+--------------------------+--------------------+----------------+
| ``I``  | :c:type:`unsigned int`   | integer            | 4              |
+--------+--------------------------+--------------------+----------------+
| ``l``  | :c:type:`long`           | integer            | 4              |
+--------+--------------------------+--------------------+----------------+
| ``L``  | :c:type:`unsigned long`  | integer            | 4              |
+--------+--------------------------+--------------------+----------------+
| ``q``  | :c:type:`long long`      | integer            | 8              |
+--------+--------------------------+--------------------+----------------+
| ``Q``  | :c:type:`unsigned long   | integer            | 8              |
|        | long`                    |                    |                |
+--------+--------------------------+--------------------+----------------+
| ``n``  | :c:type:`ssize_t`        | integer            |                |
+--------+--------------------------+--------------------+----------------+
| ``N``  | :c:type:`size_t`         | integer            |                |
+--------+--------------------------+--------------------+----------------+
| ``e``  | \(7)                     | float              | 2              |
+--------+--------------------------+--------------------+----------------+
| ``f``  | :c:type:`float`          | float              | 4              |
+--------+--------------------------+--------------------+----------------+
| ``d``  | :c:type:`double`         | float              | 8              |
+--------+--------------------------+--------------------+----------------+
| ``s``  | :c:type:`char[]`         | bytes              |                |
+--------+--------------------------+--------------------+----------------+
| ``p``  | :c:type:`char[]`         | bytes              |                |
+--------+--------------------------+--------------------+----------------+
| ``P``  | :c:type:`void \*`        | integer            |                |
+--------+--------------------------+--------------------+----------------+

Function
---------

.. function:: calcsize(fmt)

   Return to the given *fmt* number of bytes.

   - ``fmt`` - Format character type, see format character table above


    >>> struct.calcsize("i")
    4
    >>> struct.calcsize("B")
    1


.. function:: pack(fmt, v1, v2, ...)

   According to the format string FMT, pack *v1, v2, ...* value. The return value is a byte object that decodes the value.

    >>> struct.pack("ii", 3, 2)
    b'\x03\x00\x00\x00\x02\x00\x00\x00'

.. function:: pack_into(fmt, buffer, offset, v1, v2, ...)
   
   According to the format string FMT. Take *v1, v2, ...* Values are packed into a buffer starting with *offset*. Count from the end of the buffer, *offset* may be negative.


.. function:: unpack(fmt, data)

   Decompress the data according to the format string *fmt*. The return value is a tuple of decompressed values.

    >>> buf = struct.pack("bb", 1, 2)
    >>> print(buf)
    b'\x01\x02'
    >>> print(struct.unpack("bb", buf))
    (1, 2)

.. function:: unpack_from(fmt, data, offset=0)

   Unpack data starting at ``offset`` according to format string ``fmt`` . The offset to count from the end of the buffer may be negative. The return value is a tuple of the decompressed value.

    >>> buf = struct.pack("bb", 1, 2)
    >>> print(struct.unpack("bb", buf))
    (1, 2)
    >>> print(struct.unpack_from("b", buf, 1))
    (2,)
