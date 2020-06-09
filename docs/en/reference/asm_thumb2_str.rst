Store registers in memory
========================

File Specification
--------------------

Symbol: Except for special notes， ``Rt, Rn`` means ARM registers R0-R7.  ``immN`` means an instant value with N-bit width, so the range of ``imm5`` is limited to 0-31. 
``[Rn + imm5]`` is the content of the memory address obtained by adding Rn and offset value  ``imm5`` . The unit of offset value is byte. These instructions will not affect the condition flags.

Register storage
--------------

* str(Rt, [Rn, imm7]) ``[Rn + imm7] = Rt`` Store a 32-bit word
* strb(Rt, [Rn, imm5]) ``[Rn + imm5] = Rt`` Store one byte (b0-b7)
* strh(Rt, [Rn, imm6]) ``[Rn + imm6] = Rt`` Store a 16-bit halfword (b0-b15)

Specify the unit of immediate deviation value in bytes. So in case of  ``str`` , the 7-bit value makes it possible to access the 32-bit word alignment value with the maximum deviation of 31 words.
In the case of ``strh`` , the 6-bit value makes it possible to access the 16-bit halfword alignment value with the maximum deviation of 31 halfwords.
