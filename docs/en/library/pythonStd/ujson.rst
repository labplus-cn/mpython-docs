:mod:`ujson` -- JSON Encoding and Decoding
==========================================

.. module:: ujson
   :synopsis: JSON encoding and decoding

This module implements the corresponding :term:`CPython` A subset of modules, as described below. Refers to CPython documents for details: `json <https://docs.python.org/3.5/library/json.html#module-json>`_

This module allows conversion between Python objects and JSON data formats.

Function
---------

.. function:: dump(obj, stream)

   Take *obj* serialize to *JSON* string, Write it to the given *stream* .

.. function:: dumps(obj)

  Convert dict type data to str，This function is required when writing data of type dict directly to JSON file, because an error will be reported.
  - ``obj`` Objects to convert

Example::

  >>> obj = {1:2, 3:4, "a":6}
  >>> print(type(obj), obj) #Originally of dict type
  <class 'dict'> {3: 4, 1: 2, 'a': 6}
  >>> jsObj = ujson.dumps(obj) #Convert dict type to str
  >>> print(type(jsObj), jsObj)
  <class 'str'> {3: 4, 1: 2, "a": 6}


.. function:: load(stream)

  Parsing given *stream*, interpret it as a JSON string and deserialize the data into Python objects. Returns the result object. 

  Parsing continues until the end of the file. If the data in the stream is not properly formed, then raise :exc:`ValueError`


.. function:: loads(str)

   Parse the JSON string and return the object. A valueerror exception will be thrown if the string is malformed.
   
Example::

  >>> obj = {1:2, 3:4, "a":6}
  >>> jsDumps = ujson.dumps(obj)
  >>> jsLoads = ujson.loads(jsDumps)
  >>> print(type(obj), obj)
  <class 'dict'> {3: 4, 1: 2, 'a': 6}
  >>> print(type(jsDumps), jsDumps)
  <class 'str'> {3: 4, 1: 2, "a": 6}
  >>> print(type(jsLoads), jsLoads)
  <class 'dict'> {'a': 6, 1: 2, 3: 4}
