.. _radio:

.. module:: radio
   :synopsis: Radio-related functions

:mod:`radio` --- Radio-related functions
==========

The radio module provides wireless broadcast function, supports 13 Channel, and can receive broadcast messages sent by members in the same Channel, suitable for multi-board network communication within 10 meters.

Parameter
----------


.. py:method:: radio.on()

Turn ON wireless function

.. py:method:: radio.off()

Turn OFF wireless function


.. py:method:: radio.config(channel)


Configure wireless parameters

- ``channel`` (int): Wireless channel, range 1~13



.. py:method:: radio.receive()

Receive a wireless broadcast message, the message is returned as a string. Can receive up to 250 bytes of data. If no message is received, it returns ``None`` . When the internal parameter of ``receive`` is  ``True`` , that is  ``receive(True)`` , the (msg,mac) binary is returned. The default is ``receive(False)`` , which only returns msg.


.. py:method:: radio.receive_bytes()

Receive wireless broadcast message, the message is returned in bytes. Others are the same as ``radio.receive()`` .

.. py:method:: radio.send()

Send wireless broadcast message, data type as string. Return True after successful transmission, otherwise return False.

.. py:method:: radio.send_bytes()

Send wireless broadcast message, byte data type. Return True after successful transmission, otherwise return False.



.. literalinclude:: /../../examples/radio/radio.py
    :caption: Radio broadcasting example
    :linenos:
