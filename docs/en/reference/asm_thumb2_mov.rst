Register shift instruction
==========================

File specification
--------------------

Symbol： ``Rd, Rn`` means ARM registers R0-R15.  ``immN`` means instant value with width N. These instructions affect the condition flags.

Register shift
--------------

When using immediate value, it changes from zero padding to 32 bits. So  ``mov(R0, 0xff)`` set R0 to 255.

* mov(Rd, imm8) ``Rd = imm8``
* mov(Rd, Rn) ``Rd = Rn``
* movw(Rd, imm16) ``Rd = imm16``
* movt(Rd, imm16) ``Rd = (Rd & 0xffff) | (imm16 << 16)``

movt writes an immediate value to the first half-word of the target register, which does not affect the content of the second half-word.

* movwt(Rd, imm32) ``Rd = imm32``

movwt is a virtual instruction：The MicroPython assembler sends  ``movw`` and then ``movt`` to move the 32-bit value into Rd. Move a 32-bit value into Rd with a movt.
