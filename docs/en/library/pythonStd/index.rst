.. _pythonStd:

Python Standard library
===========

"micropython Standard Library", the miniaturization of "Python Standard Library". Only provide the core functions of the module. Those modules that don't use the standard Python name. was labeled with a "U", for example, "U JSON" instead of "JSON". Which is the micropython standard library could only realize portion of the module functions.。
For better compatibility, users could choose to write the Python module module extension function by the change of name. (Note: mentioned in "term:`micropython-lib"）。

On the embedded platform, python Encapsulation Library can be added to achieve compatibility naming with Cpython.
The path of "non-u-name" packaged files was rewritable.

For example: for ”import json“，First, to search and load the “JSON. Py” file or “JSON” directory.
If not, then go back to load the built-in “ujson” module.


 .. toctree::
      :maxdepth: 1

      builtins.rst
      array.rst
      gc.rst
      math.rst
      sys.rst
      ubinascii.rst
      ucollections.rst
      uerrno.rst
      uhashlib.rst
      uheapq.rst
      uio.rst
      ujson.rst
      uos.rst
      ure.rst
      uselect.rst
      usocket.rst
      ussl.rst
      ustruct.rst
      utime.rst
      uzlib.rst


      


