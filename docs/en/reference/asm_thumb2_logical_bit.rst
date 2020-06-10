Logic & Bit Operation Instructions
==============================

File Specification
--------------------

Symbol：Except for the special instructions using R0-R15, ``Rd, Rn`` means ARM registers R0-R7.  ``Rn<a-b>`` means the ARM register whose content is in the range of ``a <= contents <= b`` .
For instructions with two register parameters, both are allowed to be the same. For example, regardless of the initial content, the following instruction will reset R0 to zero (Python  ``R0 ^= R0`` ).

* eor(r0, r0)

Unless otherwise specified, these instructions affect condition flags。

Logic instruction
--------------------

* and\_(Rd, Rn) ``Rd &= Rn``
* orr(Rd, Rn) ``Rd |= Rn``
* eor(Rd, Rn) ``Rd ^= Rn``
* mvn(Rd, Rn) ``Rd = Rn ^ 0xffffffff`` i.e.  Rd = 1's complement of Rn
* bic(Rd, Rn) ``Rd &= ~Rn``  bit use the mask in Rn to clear Rd

Note: Use "and\_" instead of "and" because "and" is a reserved keyword in Python. 

Conversion and rotation instructions
-------------------------------

* lsl(Rd, Rn<0-31>) ``Rd <<= Rn``
* lsr(Rd, Rn<1-32>) ``Rd = (Rd & 0xffffffff) >> Rn`` Logical shift right
* asr(Rd, Rn<1-32>) ``Rd >>= Rn`` Arithmetic shift right
* ror(Rd, Rn<1-31>) ``Rd = rotate_right(Rd, Rn)`` Rd turn right Rn bit.

The three-position rotation operation is as follows. If Rd initially contains bits ``b31 b30..b0`` , then it will contain ``b2 b1 b0 b31 b30..b3`` after rotation.

Special instructions
--------------------

Condition codes are not affected by these instructions.

* clz(Rd, Rn) ``Rd = count_leading_zeros(Rn)``

count_leading_zeros(Rn) Returns the number of binary zero digits before the first binary digit in Rn.

* rbit(Rd, Rn) ``Rd = bit_reverse(Rn)``

bit_reverse(Rn) Returns the bit-reversed content of Rn. If Rn contains bits ``b31 b30..b0`` , then Rd will be set to ``b0 b1 b2..b31`` 。

Before executing clz, the null point can be calculated by performing a bit reversal.
