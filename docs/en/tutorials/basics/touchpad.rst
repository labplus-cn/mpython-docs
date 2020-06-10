Touchpad
=======

The 6 goldfinger on the front of the mPython Board as touchpads for expansion, indicated as P、Y、T、H、O、N in sequence.


------------------------------------------------------------

.. literalinclude:: /../../examples/button/button_tp_ctl_rgb.py
    :caption: Example - Touch different buttons to light up RGB lights of different colors
    :linenos:
        

First, import the mPython module, Try to touch the P gold finger with your finger and use  ``read()``  to read the value. Observe the changes::

  >>> from mpython import *
  >>> touchPad_P.read()
  643
  >>> touchPad_P.read()
  8

.. Note::

  The control board has 6 touch pads on it, touchPad_P、touchPad_Y、touchPad_T、touchPad_H、touchPad_O、touchPad_N，from left to right, and other touch keys are used as above.

.. image:: /../images/mPython Board pins definition - Front Side.png
