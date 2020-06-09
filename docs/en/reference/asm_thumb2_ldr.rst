Load registers from memory
=========================

File Specification
--------------------

Symbol: Except for special notes, ``Rt, Rn`` means ARM registers R0-R7. ``immN`` means instant value with width N, so the range of ``imm5`` is limited to 0-31. ``[Rn + immN]`` is passed
Add the content of the memory address obtained by Rn and the error  ``immN`` . Error unit is byte. These instructions affect the condition flags.

Register loading
-------------

* ldr(Rt, [Rn, imm7]) ``Rt = [Rn + imm7]`` Load a 32-bit word
* ldrb(Rt, [Rn, imm5]) ``Rt = [Rn + imm5]`` Load a byte
* ldrh(Rt, [Rn, imm6]) ``Rt = [Rn + imm6]`` Load a 16-bit halfword

When a byte or a halfword is loaded, it changes from zero padding to 32 bits.

Specify the immediate error unit as bytes. Therefore, in the case of ``ldr`` , the 7-bit value makes it possible to access the 32-bit word alignment value with the maximum offset of 31 words.
In the case of ``ldrh`` , the 6-bit value makes it possible to access the 16-bit halfword alignment value with the maximum offset value of 31 halfwords.
