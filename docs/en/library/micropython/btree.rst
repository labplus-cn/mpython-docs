:mod:`btree` -- Simple BTree Database
=====================================

.. module:: btree
   :synopsis: Simple BTree Database

 ``btree`` The module uses external storage (disk file or random access stream in general) to realize simple key value database.
 Key sorting is stored in the database. In addition to the effective retrieval of a single key value, the database also supports efficient ordered range scanning (using keys within a given range to retrieve values). 
 In terms of application program interface, the B-tree database should be operated in a way similar to the standard 'dict' type as much as possible. One obvious difference is that both the key and the value must be.
 As a `bytes` object（Therefore, if you want to store other types of objects, you need to first serialize them to `bytes` ）。

This module is based on the BerkelyDB library 1.xx edition.

Examples::

    import btree

    # First, we need to open a stream which holds a database 
    # This is usually a file, but can be in-memory database 
    # using uio.BytesIO, a raw flash partition, etc. used of uio.BytesIO，
    # Oftentimes, you want to create a database file if it doesn't
    # exist and open if it exists. Idiom below takes care of this.
    # In general, if there is no database file, you need to create one; if there is already one, just open it. The following idioms take this into account. 
    # DO NOT open database with "a+b" access mode. 

    try:
        f = open("mydb", "r+b")
    except OSError:
        f = open("mydb", "w+b")

    # Now open a database
    db = btree.open(f)

    # The keys you add will be sorted internally in the database 您
    db[b"3"] = b"three"
    db[b"1"] = b"one"
    db[b"2"] = b"two"

    # Assume that any changes are cached in memory unless
    # explicitly flushed (or database closed). Flush database
    # at the end of each "transaction". 
    # Any changes are assumed to be cached in memory unless explicitly refreshed (or the database is shut down). Refresh the database at the end of each process. 
    db.flush()

    # Prints b'two'
    print(db[b"2"])

    # Iterate over sorted keys in the database, starting from b"2"
    # until the end of the database, returning only values. 
    # Iterate over the sorted keys in the database, starting from B "2" to the end of the database, and only return values. 
    # Mind that arguments passed to values() method are *key* values. 
    # Prints:
    #   b'two'
    #   b'three'
    for word in db.values(b"2"):
        print(word)

    del db[b"2"]

    # No longer true, prints False 不正确，打印False
    print(b"2" in db)

    # Prints:
    #  b"1"
    #  b"3"
    for key in db:
        print(key)

    db.close()

    # Don't forget to close the underlying stream! 
    f.close()


Function
---------

.. function:: open(stream, \*, flags=0, cachesize=0, pagesize=0, minkeypage=0)

   Open a database from a random access ``stream``(similar to an open file). All other parameters are optional, are only keywords, and allow adjustment of advanced parameters of database operation (most users do not need this):

   * *flags* - currently unused
   * *cachesize* - Recommended maximum memory cache size in bytes. For a board with sufficient memory, using a larger value may improve performance. This value is only the recommended value. If the value is set too low, the module may occupy more memory.
   * *pagesize* - The page size used for the node in the BTree. The acceptable range is 512-65536. If 0, the size of the underlying I/O block is used (best coordination between memory usage and performance). 
   * *minkeypage* - The minimum number of keys stored per page. The default is 0 equals to 2. 

   Returns a BTree object that implements a dictionary protocol (method set) and the following additional methods. 

Method
-------

.. method:: btree.close()

   Close the database. Closing the database at the end of processing is mandatory because some unwritten data may remain in the cache. Note: This does not close the underlying flow that is opened with the database, which should be closed separately (this is also mandatory to ensure that data flushed from the buffer goes into the underlying storage). 

.. method:: btree.flush()

   Refresh any data in the cache to the underlying stream. 

.. method:: btree.__getitem__(key)
            btree.get(key, default=None)
            btree.__setitem__(key, val)
            btree.__detitem__(key)
            btree.__contains__(key)

   Standard dictionary method. 

.. method:: btree.__iter__()

   B-tree objects can be iterated directly (similar to dictionaries) to access all keys orderly.

.. method:: btree.keys([start_key, [end_key, [flags]]])
            btree.values([start_key, [end_key, [flags]]])
            btree.items([start_key, [end_key, [flags]]])

   These methods are similar to the standard dictionary methods, but you can also use optional parameters to iterate over the key subscope instead of the entire database. 
   Note：This is the third method这, *start_key* and *end_key* parameters all represent key values. For example, the ``values()`` method iterates over the values corresponding to a given key range.
   No *start_key* value means “from the first key”, No “*end_key* value or none means “until the end of the database”. 
   By default, the range includes *start_key* ，excluding *end_key* , you can pass `btree.INCL` to set *end_key* to include in the iteration.
   Can pass `btree.DESC` tag to iterate in the direction of the down key. Tag value can be the same as ORed. 

Constant
---------

.. data:: INCL

    `keys()`, `values()`, `items()` methods, specifies that the scan should include the end key.

.. data:: DESC

    `keys()`, `values()`, `items()` The tags method specifies that the scan should be performed in the downward direction of the key.
