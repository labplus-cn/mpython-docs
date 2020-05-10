:mod:`ubinascii` -- Binary / ASCII conversion
============================================

.. module:: ubinascii
   :synopsis: Binary / ASCII conversion

This module implements the corresponding :term:`CPython` A subset of modules, as follows. See CPython document for details: `binascii <https://docs.python.org/3.5/library/binascii.html#module-binascii>`_

This module realizes the conversion (bidirectional) between binary data and various ASCII codes.

Function
---------

.. function:: hexlify(data, [sep])

   Converts a string to a hexadecimal representation.

   .. admonition:: differences with CPython
      :class: attention

      If additional parameter SEP is provided, It will be used as a separator in-between these hexadecimal values.
   
   Without SEP parameter::

      >>> ubinascii.hexlify('\x11\x22123')
      b'1122313233'
      >>> ubinascii.hexlify('abcdfg')
      b'616263646667'
   
   If the second parameter SEP is specified, it will be used to separate two hexadecimal numbers::

      >>> ubinascii.hexlify('\x11\x22123', ' ')
      b'11 22 31 32 33'
      >>> ubinascii.hexlify('\x11\x22123', ',')
      b'11,22,31,32,33'



.. function:: unhexlify(data)

   Convert hexadecimal string to binary string, the function is opposite to hexlify.

   Example::

      >>> ubinascii.unhexlify('313233')
      b'123'



.. function:: a2b_base64(data)

   ecode Base64 encoded data, ignoring invalid characters in input. According with   `RFC 2045 s.6.8 <https://tools.ietf.org/html/rfc2045#section-6.8>`_ 。returns a ``bytes`` object。


.. function:: b2a_base64(data)

  Encoding binary data in Base64 format, as mentioned in  `RFC 3548 <https://tools.ietf.org/html/rfc3548.html>`_ . Returns the encoded data, followed by a line break, as the ``bytes`` object.

