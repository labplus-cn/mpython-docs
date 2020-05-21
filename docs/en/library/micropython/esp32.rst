:mod:`esp32` --- ESP32 specific features
====================================================

.. module:: esp32
    :synopsis: ESP32 specific features

``esp32`` The module contains functions and classes specifically for controlling the ESP32 module.

Function
---------

.. function:: wake_on_touch(wake)

    Configure whether the touch wakes the device from sleep. Wake should be a boolean

.. function:: wake_on_ext0(pin, level)

    Configure `EXT0`  how to wake the device from sleep.  

    - ``pin`` :None or a valid Pin object。 
    - ``level`` : ``esp32.WAKEUP_ALL_LOW`` or ``esp32.WAKEUP_ANY_HIGH`` 。

.. function:: wake_on_ext1(pins, level)

    Configure `EXT1` how to wake the device from sleep.  

    - ``pin`` :None or a tuple / list of valid Pin objects.  
    - ``level`` : ``esp32.WAKEUP_ALL_LOW`` or ``esp32.WAKEUP_ANY_HIGH`` 。

.. function:: raw_temperature()

    Read the original value of the internal temperature sensor and return an integer.

.. function:: hall_sensor()

    Read the original value of the internal Hall sensor and return an integer. 


Ultra low power coprocessor
--------------------------------

.. class:: ULP()

    This class provides access to ultra-low power coprocessors. 

.. method:: ULP.set_wakeup_period(period_index, period_us)

    Set wake up time. 

.. method:: ULP.load_binary(load_addr, program_binary)

    Load program_binary into ULP in the given load_addr.

.. method:: ULP.run(entry_point)

    Start ULP running at the given entry_point .


Constants
---------

.. data:: esp32.WAKEUP_ALL_LOW
          esp32.WAKEUP_ANY_HIGH

   Select the wake-up level of the pin. 
