Random Number
======================================

Sometimes we need to do random act or generate produce random numbers. Then you can use :ref:`random<random>` module.

For example, here is how to display random name on the OLED::

  from mpython import *
  import random

  names = ["Mary", "Yolanda", "Damien", "Alia", "Kushal", "Mei Xiu", "Zoltan" ]


  oled.DispChar(random.choice(names),40,20)
  oled.show()
  oled.fill(0)

The list (names) contains seven definitions to define as names string.

Could you modify the list to include your own name?

Random display of numbers
---------


Random numbers are very useful. They are very common in games. Why do we still have dice？

MicroPython comes with several useful random number generating methods. Here is how to make a simple dice::

  from mpython import *
  import random

  oled.DispChar(str(random.randint(1,6)),60,20)
  oled.show()
  oled.fill(0)

.. Note::

  Every time you restart the mPython Board, it will display a number between 1 and 6。``randint()`` returns an integer, we need to use ``str()`` to convert the integer to a string (such as, 6 -> "6")。
  ``oled.DispChar()`` write random number in OLED.

If you want to set a random range or increase the base, to use random.randrange()::
 
  from mpython import *
  import random

  oled.DispChar(str(random.randrange(0,10,2)),60,20)
  oled.show()
  oled.fill(0)

.. Note::

  random.randrange(start, end, step). ``start`` is the start value of the random number, ``end`` is the end value of the random number, and step is the increasing base.
  The above example is to randomly display even numbers in the range (0,10).

Sometimes you need a number with a decimal point. You can use the ``random.random`` method to generate random floating point numbers from 0.0 to 1.0. If you need the result of adding a larger random floating point number  ``random.uniform`` ::
  from mpython import *
  import random

  oled.DispChar(str(random.random()),30,10)
  oled.DispChar(str(random.uniform(1,20)),30,30)
  oled.show()
  oled.fill(0)

Random seed
-------

The random number in MicroPython is actually a stable result sequence obtained by a stable algorithm, not a random sequence. SEED is the first value calculated by this algorithm.
So it will appear that as long as the SEED is the same, then all subsequent "random" results and order are exactly the same.

Specify a random number SEED, usually used in conjunction with other random number generation functions.

Sometimes you want repeatable random behavior: a reproducible source of randomness. It's like saying you need the same five random values every time you roll the dice.

Example::

  import random
  from mpython import *


  for i in range(0,2):
    random.seed(8)

    for j in range(8):
      oled.DispChar(str(random.randint(1,10)),j*16,i*16)
      oled.show()
      print(random.randint(1,10))

  oled.fill(0)

Snowing effect
-------

Combined with the random number generation learned above, we can use the mPython Board OLED screen to create a snowing effect.

.. literalinclude:: /../../examples/display/snowing.py
    :linenos:

.. figure:: /../images/tutorials/snowing.gif
    :align: center

    Snowing
