:mod:`uhashlib` -- Hash Algorithm
=====================================

.. module:: uhashlib
   :synopsis: hash algorithm

This module implements the corresponding :term:`CPython` a subset of modules, as follows. Refers to CPython document for details: `hashlib <https://docs.python.org/3.5/library/hashlib.html#module-hashlib>`_

This module implements the binary data hash algorithm. The exact list of available algorithms depends on the board. In the algorithms that can be implemented.：

* SHA256 -  The current generation of modern hash algorithms (Sha2 Series). It is suitable for encryption security purposes. Unless there is a specific code size limit, it is recommended to use the MicroPython kernel and any board to provide this feature.

* SHA1 - Previous generation algorithm. It is not recommended for new application, but SHA1 is part of many Internet standards and existing applications, so circuitry boards for network connectivity and interoperability will try to provide this feature.

* MD5 -  legacy checksum algorithm, not considered as encrypted. Only the selected circuit board can achieve interoperability with traditional applications. 

Construct Object
------------

.. class:: uhashlib.sha256([data])

    create a SHA256 hash object，and option for ``data`` input.
    Create an SHA256 hasher object and optionally feed ``data`` into it.

.. class:: uhashlib.sha1([data])

     Create a SHA1 hash object，and option for  ``data`` input.

.. class:: uhashlib.md5([data])

    Create MD5 hash object and option to select  ``data`` input.

Method
-------

.. method:: hash.update(data)

   Feed more binary data into hash

.. method:: hash.digest()

  Returns a hash of all data passed through as a byte object. When this method is called, no more data entry.

.. method:: hash.hexdigest()

  If this method is not workable. Then use ``ubinascii.hexlify(hash.digest())`` to achieve a similar effect. 


