:mod:`uzlib` -- zlib unzip
==================================

.. module:: uzlib
   :synopsis: zlib decompression

This module implements the corresponding :term:`CPython` A subset of modules, as described below. Refers to CPython document for details: `zlib <https://docs.python.org/3.5/library/zlib.html#module-zlib>`_

his module allows the extraction of binary data compressed with the deflate algorithm (commonly used in zlib libraries and gzip compressors). Compression is not yet implemented.

Function
---------

.. function:: decompress(data, wbits=0, bufsize=0)

   Returns the extracted data as bytes. *wbits* is the size of the deflate dictionary window used for compression (8-15, the size of the dictionary is the power of 2 of this value).
   In addition, if the value is positive, *data* is assumed to be a zlib stream with zlib headers. Otherwise, if the value is negative,
   The original deflate flow is assumed. *bufsize* parameter is compatible with Cpython, ignored here.
 

.. class:: DecompIO(stream, wbits=0)

   Create a flow decorator that allows transparent decompression of compressed data in another flow.
   This allows compressed streams to be processed with data larger than the available heap size. In addition to the values described in `decompress()` , *wbits* possible values 24..31 (16 + 8..15), This means that the input stream has a gzip header.

   .. admonition:: differences with CPython
      :class: attention

      This class is an extension of MicroPython. Temporarily use this class, it may be modified or deleted in a later version.
