.. mPython Board documentation master file, created by
   sphinx-quickstart on Tue Aug 28 17:25:35 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

mPython help documentation
======================================

Welcome to use mPython!

mPython board is a teaching and learning tool jointly put forward by the maker education expert committee, maoyouhui and the majority of front-line teachers and participated in the research and development with the representatives of excellent enterprises in the maker education industry. It is an open source hardware for education and a public welfare project.

|
.. image:: /../images/掌控-动态.gif
|

| **mPython Board Official Website**: https://www.mpython.cn
| **GitHub Open Source**: https://github.com/labplus-cn/mPython
| **mPython Board Documentation**: https://mPython.readthedocs.io
| **mPython IDE Software Programming Documentation**: https://mpythonsoftware.readthedocs.io/
| **Awesome-mPython(Resources)** : https://labplus-cn.github.io/awesome-mpython/


*We open the software and hardware resources of the mPython Board project to GitHub to share with mPython Board user to learn and Apply*

.. Attention::

     The project is under active development. Since ESP32 is still for developers, not all peripheral devices can be used perfectly, there may still be some bugs, we will continue to fix and update in time.

---------

mPython Board materials
---------

.. toctree::
   :maxdepth: 2

   board/index.rst


---------

.. toctree::
   :maxdepth: 2
   :caption: mPython Board Tutorial

   tutorials/basics/index.rst
   tutorials/advance/index.rst

---------

Classic Examples
++++++

.. toctree::
    :maxdepth: 2


    classic/index.rst

---------

MicroPython Library
----------------

.. toctree::
   :maxdepth: 1
   :caption: MicroPython Library
   :hidden:

   library/pythonStd/index.rst
   library/micropython/index.rst


============================================   =============================================================================
 :ref:`Python Standard Library<pythonStd>`       CPython compatible, contain Python built-in functions、commonly used module
 :ref:`MicroPython Library<microPythonModu>`     MicroPython ESP32 hardware control module
============================================   =============================================================================


You can find the available built-in libraries through ``help()`` , import the following content in REPL to import::

    >>> help('modules')


In addition to the built-in libraries described in this document, the :term:`micropython-lib`  You can also find more modules from the Python standard library and further microPython extensions to it.

---------

mPython Library
-------------

.. toctree::
   :maxdepth: 1
   :caption: mPython Library
   :hidden:

   library/mPython/index.rst
   ext_lib/index.rst

- ``built-in``

   - :mod:`mpython`  --------- mPython Board related built-in functions                                
   - :mod:`music` --------- Music related function, micro:bit module compatible
   - :mod:`urequests` --------- Related function of HTTP Client
   - :mod:`umqtt.simple` --------- MQTT Client function
   - :mod:`gui` --------- GUI type drawing elements
   - :mod:`audio` --------- Audio playback recording
   - :mod:`radio` --------- Radio broadcasting
   - :mod:`sdcard` --------- Mount SD Card
   - :mod:`bluebit` --------- blue:bit driver
   - :mod:`parrot` --------- mPython Expansion Board driver
   - :mod:`ds18x20` --------- ds18b20 Temperature Sensor driver

- ``extend``

   - `mython_ble <https://mpython-ble.readthedocs.io/>`_ --------- buletooth BLE Higher


---------

.. toctree::
   :maxdepth: 1
   :caption: MicroPython Syntax

   reference/index.rst

References for specific language features of micropython


.. toctree::
   :hidden:
   
   license.rst


.. toctree::
   :hidden:

   release <https://github.com/labplus-cn/mpython/releases>


mPython Series
----------

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: mPython Series

   extboard/index.rst
   mpython_classroom_kit/index.rst

.. image:: /../images/extboard/extboard_250.png
  :scale: 80 %
  :target: extboard/index.html

.. image:: /../images/mpython_classroom_kit/mpython_classroom_kit_250.png
  :scale: 80 %
  :target: mpython_classroom_kit/index.html


------------------

Index
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
