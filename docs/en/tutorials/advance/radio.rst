.. _tutorials_radio:

Radio Broadcast
===============

The mPython Board provides 13 channeks of 2.4G wireless RF communication. Can realize simple networking communication in a certain area. Under the same channel, members can receive broadcast messages. It's similar, like walkie talkie. Under the same channel, realize the call.

.. figure:: /../images/tutorials/radio/radio.png
    :align: center
    :width: 200

    Walkie Talkie

radio
--------

.. literalinclude:: /../../examples/radio/radio.py
    :caption: You can use two mPython Board to upload the program, under REPL, send and receive broadcast messages
    :linenos:

|

.. raw:: html

    <iframe width="700" height="400" src="https://showmore.com/zh/embed/j9xqz8v"  frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

|

First of all we need  ``import radio`` to import the wireless module. Then ``radio.on()`` , turn on the wireless function. Configure wireless channel ``radio.config(channel)`` , channel parameter can set 1 ~ 13 channels.
Use ``radio.send()`` to send a broadcast message, the message type is a string. On the receiving end, on the same channel, use ``radio.receive()`` to receive broadcast data. ``receive(True)`` The return data type is (msg, mac).
mac is the MAC address of the network device, and the addresses are unique. For example, if you want to be a unicast application, you can filter messages sent by other MAC devices. By default, ``receive()`` , the returned data type is msg, without MAC address.


Telegraph
-------

Based on the above radio learning, we can use the mPython Board to make an unique telegraph! The two mPython Board are spread by radio and Morse code, is there a sense of spy war film? Try it now！

.. figure:: /../images/tutorials/radio/telegraph.jpg
    :align: center
    :width: 400

    Telegraph


.. literalinclude:: /../../examples/radio/telegraph.py
    :caption: Telegraph example
    :linenos:

|
.. raw:: html

    <iframe width="700" height="400" src="https://showmore.com/zh/embed/ra3i9uw"  frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

|

The above telegraph example, A B button to select the wireless channel, touch T, send telegram. When receiving the telegram, the RGB of the mPython Board will have an indication.
