Algorithm Instructions
=======================

File specification
--------------------

Symbols:： ``Rd`` , ``Rm`` , ``Rn`` means ARM registers R0-R7。 ``immN`` means instant value with N-bit width, such as ``imm8`` 、 ``imm3``， etc.
``Carry`` indicates the carry condition flag.  ``not(carry)`` means its complement. For instructions with more than one register parameter, allow them to be the same.
For example, the following instruction will add the contents of R0 to itself, placing the result in R0:

* add(r0, r0, r0)

Unless otherwise specified, algorithmic instructions will affect condition flags.

Add
--------

* add(Rdn, imm8) ``Rdn = Rdn + imm8``
* add(Rd, Rn, imm3) ``Rd = Rn + imm3``
* add(Rd, Rn, Rm) ``Rd = Rn +Rm``
* adc(Rd, Rn) ``Rd = Rd + Rn + carry``

subtract
-----------

* sub(Rdn, imm8) ``Rdn = Rdn - imm8``
* sub(Rd, Rn, imm3) ``Rd = Rn - imm3``
* sub(Rd, Rn, Rm) ``Rd = Rn - Rm``
* sbc(Rd, Rn) ``Rd = Rd - Rn - not(carry)``

negate
--------

* neg(Rd, Rn) ``Rd = -Rn``

Multiplication and division
---------------------------

* mul(Rd, Rn) ``Rd = Rd * Rn``

This will produce a 32-bit result with an overflow lost. The result may be considered signed or unsigned according to the definition of the operand.

* sdiv(Rd, Rn, Rm) ``Rd = Rn / Rm``
* udiv(Rd, Rn, Rm) ``Rd = Rn / Rm``

These functions perform signed and unsigned divisions, respectively. Condition flags are not affected.
