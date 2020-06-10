Compare instructions
=======================

These instructions perform arithmetic or logical instructions on two parameters, discarding the result but setting the condition flag. Generally, these instructions are used to test the data value without changing the data value before executing the conditional branch.

File specification
--------------------

Symbol： ``Rd, Rm, Rn`` means ARM registers R0-R7.  ``imm8`` represents an instant value with 8-bit width.

Application Status Register (APSR)
----------------------------------------------

This contains four bits tested by conditional branch instructions. Normally, the conditional branch will test multiple bits, such as  ``bge(LABEL)`` .
The meaning of the condition code depends on whether the operand of the arithmetic instruction is regarded as a signed or unsigned integer. Therefore, ``bhi(LABEL)`` is assumed to handle unsigned numbers, and ``bgt(LABEL)`` is assumed to handle signed numbers.

APSR bit
---------

* Z (zero)

If the result of the operation is 0 or the compared operands are equal, set to 0.

* N (negative)

If the result is negative, set to N.

* C (carry)

If the result overflows the MSB, add the carry flag, for example, add 0x80000000 and 0x80000000. Due to the nature of two's complement arithmetic,
This behavior reverses during subtraction, clearing borrows indicated by carry. So 0x10 - 0x01 executes as 0x10 + 0xffffffff, it will set the carry bit.

* V (overflow)

If the result (considered as the complement of the binary number) has an "error" sign related to the operand, an overflow flag will be set. For example, adding 0x7fffffff will set the overflow bit，
Because the result（0x8000000）(which is regarded as a two's complement integer) is negative. Please note: In this case, the carry is not set.

Compare instructions
-----------------------

These instructions set the APSR (application status register), N (negative), Z (zero), C (carry), and V (overflow) flags.

* cmp(Rn, imm8) ``Rn - imm8``
* cmp(Rn, Rm) ``Rn - Rm``
* cmn(Rn, Rm) ``Rn + Rm``
* tst(Rn, Rm) ``Rn & Rm``

Conditional Execution
---------------------

The ``It`` and ``ite`` instructions provide a way to conditionally execute one to four subsequent instructions without marking.

* it(<condition>) If then

If <condition> is True, execute the next instruction:

::

    cmp(r0, r1)
    it(eq)
    mov(r0, 100) # runs if r0 == r1
    # execution continues here 

* ite(<condition>) If then else

If <condtion> is TRUE, execute the next instruction, otherwise execute subsequent instructions, so:

::

    cmp(r0, r1)
    ite(eq)
    mov(r0, 100) # runs if r0 == r1
    mov(r0, 200) # runs if r0 != r1
    # execution continues here 

This may be expanded to control the execution of up to four subsequent instructions：it[x[y[z]]] where x,y,z=t/e; e.g. itt, itee, itete, ittte, itttt, iteee, etc.
