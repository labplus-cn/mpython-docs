.. _extboard_introduce:

mPython Expansion Board Introduction
================

Overview
----

This mPython Expansion Board (or PARROT as named in Library) is a handy and portable, exquisitely designed as the extension for mPython Board. The 12x I/O interface and 2x I2C interface enable its' extension capability to supports unique functions: motor drive, audio playback, speech synthesis and others. unique functions. Expandable 12 channel IO interface and 2 channel I2C interface.
Thus, expand its' connectivity for the diversify IoT application and enhance programming experiences. It realize your ideas, stimulate your creativenesss and imagination.LET‘S CREATE.

.. image:: /../images/extboard/extboard.png


Technical Data
-------

Characteristics:

    - 2 ways DC Motor driver, 150mA single way.
    - Audio power amplifier and speaker output(mPython Board P8，P9 pin)
    - Speech Synthesis (Text To Speech)
    - Expansion interface of 12x I/O and 2x I2C
    - Exquisite, handy and portable
    - Built-in Lithium Battery or external power input via USB
    - Built-in rechargeable 330mAH lithium battery
    - Operating Voltage:3.3V
    - Current: `1A@3.3V` (Max)
    - Charging current: 170mA (Max) 
    



Interface denote
--------

.. figure:: /../images/extboard/parrot_description.png
    :width: 800
    :align: center


- Power indicator status: 

    - v1 version
        - Power output indicator: 3.3V supplied, indicator lights ON; if not, the indicator goes OFF.

    - v2 version
        - Power output indicator: 3.3V supplied, indicator lights ON; if not, the indicator goes OFF.
        - Battery charging indicator: light flashing to indicates the level of charging (total: 4 levels).

- Charging indicator status: 

    - v1 version 
        Note: the charging and discharging state would only be indicated when the power switch is on.

        - Charging indicator: during charging, the indicator light is on; when fully charged, the indicator light is off.
        - Discharge indicator function: the battery power is indicated the rate of the indicator flashes. Higher rate indicates the lower power. Lights ON without indicate it is fully charged.

    - v2 version
        - Charging indicator function: during charging, the indicator flashes; when it is full, the indicator goes OFF
        
- VCC: the differences with VCC supply and other 3.3V supply. To provide higher than 3.3V for application that require higher voltage and current. Power management, VCC supplied by built-in Lithium battery but when the USB is connected, it will override the VCC supply.

DIY assembly guide
-----------

Both the mPython Board and Expansion Board have identical three holes. Connect the two boards via the three copper hexagonal rod and fasten it with screws provided, thereafter fix the protective silicon rubber cover as shown in the assembly diagram below.

.. figure:: /../images/extboard/parrot_install.png
    :scale: 70 %
    :align: center

    Assembly diagram


User guide
----------

Features illustration
+++++++++


**Motor Drive**

   The 2x PWM motor drive (marked as M1 and M2 on the mPython Expansion Board), connect it directly to external DC Motor or LED stripe/array.


**I/O**

    Connect those input sensors modules or output hardware modules, for example: PIR, Ultrasonic, LED, Button, Motor, BUzzer......
    Expansion pins are: P0、P1、P2、P3、P5、P6、P7、P11、P13、P14、P15、P16、P19(SCL)、P20(SDA)

.. Important:: 
    - Be aware: Not to use the digital input P5 and P11 to avoid conflict as it was dedicated for USER A and B switch.
    - The built-in lithium battery provides only limited drive capability, if needed to drive more powerful devices or for long term stable applications. External USB is recommended for external power supply.
    
**Speaker-Audio Playback**

    Built-in speaker to support audio playback.


**Speech Synthesis (TTS)**

    Converts normal language text into speech. Enter the text contents and let the built-in speaker speak it out.


Python Library
+++++++++

- :mod:`parrot` module : for motor drive function
- :mod:`audio` module : for audio playback function

