.. currentmodule:: machine
.. _machine.ADC:

.. module:: ADC

Class ADC -- Analog-to-digital conversion
=========================================


Create object
------------

.. class:: ADC(Pin)

Create an ADC object associated with a set pin. So you can read the analog value on that pin。

 - ``Pin`` - ADC is available on dedicated pins, ESP32 available pins are：IO39、IO36、IO35、IO33、IO34、IO32. The ADC pins of the control board are P0、P1、P2、P3、P4、P10。

Detailed pin definitions  `ESP32 pins function list. <../../../_images/pinout_wroom_pinout.png>`_ and  :ref:` mPython Board pins definition<mpython_pinout>` chapter。


Example::

      from machine import ADC, Pin

      adc = ADC(Pin(33))      # create an ADC object


Method
-------

.. method:: ADC.read( )

   Read ADC and return read result.




.. method:: ADC.atten(db)

    This method allows setting the amount of attenuation of the ADC input. This allows a wider range of possible input voltages, but at the expense of accuracy (the same number of bits now means a wider range). When atten() is not set, the default is 0DB attenuation. Possible attenuation options include：
    
    - ``db``
 

        =================== =================== ======= ====================================  
        Macro definition    Attenuation          Value   Full-scale voltage
        =================== =================== ======= ==================================== 
        ``ADC.ATTN_0DB``     0dB attenuation       0      1V
        ``ADC.ATTN_2_5DB``   2.5dB attenuation     1      1.5V
        ``ADC.ATTN_6DB``     6dB attenuation       2      2V
        ``ADC.ATTN_11DB``    11dB attenuation      3      3.3V
        =================== ========== ======= ==================================== 

.. method:: ADC.width(bit)

    Set the data width (resolution). The resolution of the ADC refers to the precision that can convert the collected analog signal into a digital signal. Usually, we use the “bit”  to express, for example, 8 bit means that the ADC can correspond to the voltage signal within the specified range, respectively corresponding to - 2^8-1, that is, 256 digits of 0-255. The higher the resolution digits, the more accurate it can be expressed, and the less information is lost.
    
    - ``bit`` -  Width options are:

        =================== ========== =============
        Macro Definition     Value      Full Range  
        =================== ========== =============
        ``ADC.WIDTH_9BIT``    0         0x1ff(511)
        ``ADC.WIDTH_10BIT``   1         0x3ff(1023)
        ``ADC.WIDTH_11BIT``   2         0x7ff(2047)
        ``ADC.WIDTH_12BIT``   3         00xfff(4095)
        =================== ========== =============

Example::

      from machine import ADC, Pin

      adc = ADC(Pin(34))      # create an ADC object
      adc.atten(adc.ATTN_11DB)   # set 3.3V Range
      x = adc.read()
      print(x)

Constant
---------


Attenuation ratio
````````
.. data:: ADC.ATTN_0DB


.. data:: ADC.ATTN_2_5DB


.. data:: ADC.ATTN_6DB



.. data:: ADC.ATTN_11DB


Data width
````````
.. data:: ADC.WIDTH_9BIT



.. data:: ADC.WIDTH_10BIT



.. data:: ADC.WIDTH_11BIT



.. data:: ADC.WIDTH_12BIT







