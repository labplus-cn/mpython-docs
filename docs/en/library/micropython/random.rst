.. _random:
:mod:`random` --- Generate random numbers
=========================================

This module is based on the ``random`` module in the Python standard library. It contains functions for generating random numbers.

Function
---------

.. method:: random.randint(start, end)

Randomly generate an integer between start and end.

  - ``start``: Start value in the specified range, included in the range.
  - ``stop``：End value within the specified range, included in the range.

Example::

  >>> import random
  >>> print(random.randint(1, 4))
  4
  >>> print(random.randint(1, 4))
  2

.. method:: random.random()

Randomly generate a floating point number between 0 and 1。 

Example::

  >>> print(random.random())
  0.7111824
  >>> print(random.random())
  0.3168149


.. method:: random.unifrom(start, end)

Randomly generate floating point numbers from start to end.

  - ``start``：Start value in the specified range, included in the range.
  - ``stop``：End value within the specified range, included in the range.

Example::

  >>> print(random.uniform(2, 4))
  2.021441
  >>> print(random.uniform(2, 4))
  3.998012


.. method:: random.getrandbits(size)

Randomly generate positive integers in the range of 0 to size binary digits. 

  - ``size`` : Bit size. Example，size = 4，then it is a random positive integer from 0 to 0b1111；size = 8，then it is a random positive integer from 0 to 0b11111111.

Example::

  >>> print( random.getrandbits(1))  #1 binary bit, the range is0~1（Decimal：0~1）
  1
  >>> print(random.getrandbits(1))
  0
  >>> print(random.getrandbits(8))  #8 binary digits, the range is 0000 0000~1111 11111（decimal：0~255）
  224
  >>> print(random.getrandbits(8))
  155

.. method:: random.randrange(start, end, step)

Randomly generate start to end and increment to a positive integer in the range of step. Example，in randrange(0, 8, 2), the randomly generated number is any of 0、2、4、6.

  - ``start``：Start value in the specified range, included in the range
  - ``stop``：End value within the specified range, included in the range
  - ``step``：Increasing cardinality

Example::

  >>> print(random.randrange(2, 8, 2))
  4
  >>> print(random.randrange(2, 8, 2))
  6
  >>> print(random.randrange(2, 8, 2))
  2

.. method:: random.seed(sed)

Specify a random number seed, usually used in conjunction with other random number generation functions.

.. Note::

   The random number in MicroPython is actually a stable result sequence obtained by a stable algorithm, not a random sequence.
   SEED is the first value that this algorithm starts to calculate. So it will appear that as long as the seed is the same, then all subsequent "random" results and order are exactly the same.

Example::

  import random

  for j in range(0, 2):
    random.seed(13)  #Specify random number seed
    for i in range(0, 10):  #Generate random sequences in the range 0 to 10
      print(random.randint(1, 10))
    print("end")

Operation result:

  5
  2
  3
  2
  3
  4
  2
  5
  8
  2
  end
  5
  2
  3
  2
  3
  4
  2
  5
  8
  2
  end

From the above, you can see that the two random number lists are the same. You can also generate a few more random number lists.
In addition, when we do not use the seed (sed) function, it is equivalent to not specifying a random seed, which is randomly generated.

.. method:: random.choice(obj)

Function description：Randomly generate the arity in the object obj.

  - ``obj``：List of arity

Example::

  >>> print(random.choice("mPython"))
  m
  >>> print(random.choice("mPython"))
  n
  >>> print(random.choice([0, 2, 4, 3]))
  3
  >>> print(random.choice([0, 2, 4, 3]))
  3
  >>> print(random.choice([0, 2, 4, 3]))
  2
