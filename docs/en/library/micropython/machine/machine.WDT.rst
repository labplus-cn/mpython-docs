.. currentmodule:: machine
.. _machine.WDT:

Class WDT -- Watchdog timer
===========================

When the program crashes and eventually enters an unrecoverable state, WDT is used to restart the system. Once started, it cannot be stopped or reconfigured in any way.
After activation, the program must periodically  ``feed`` to prevent it from expiring and reset the system.

Example::

    from machine import WDT
    wdt = WDT()        # enable it with a wdt
    wdt.feed()

Create Object
------------

.. class:: WDT()

  Create a WDT object and start it.

Method
-------

.. method:: wdt.feed()

  WDT feedto prevent it from resetting the system. The program should place this call in a reasonable location to ensure that the WDT feed after verifying that all operations are correct。
