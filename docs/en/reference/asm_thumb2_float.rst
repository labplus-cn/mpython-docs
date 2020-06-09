Floating-point instruction
==============================

These instructions support the use of ARM floating-point coprocessors (on platforms such as Python, this platform is equipped with this processor). The FPU has 32 registers called  ``s0-s31`` ,
Each register can hold a precision floating point. Data can be transferred between FPU register and ARM core register by ``vmov`` instruction.

Note: MicroPython does not support the transfer of floating point to assembly functions, nor can you put floating point in ``r0`` and expect reasonable values. There are two solutions.
One is to use arrays, the other is to transfer and/or return integers and convert them to floating-point numbers in the code.

File Specification
--------------------

Symbols： ``Sd, Sm, Sn`` means FPU register,  ``Rd, Rm, Rn`` means ARM core register. The latter can be any ARM core register, although the registers  ``R13-R15`` are not applicable in this case.

Algorithm
----------

* vadd(Sd, Sn, Sm) ``Sd = Sn + Sm``
* vsub(Sd, Sn, Sm) ``Sd = Sn - Sm``
* vneg(Sd, Sm) ``Sd = -Sm``
* vmul(Sd, Sn, Sm) ``Sd = Sn * Sm``
* vdiv(Sd, Sn, Sm) ``Sd = Sn / Sm``
* vsqrt(Sd, Sm) ``Sd = sqrt(Sm)``

Registers may be the same： ``vmul(S0, S0, S0)`` will execute ``S0 = S0*S0``

Move between ARM and FPU registers
---------------------------------------

* vmov(Sd, Rm) ``Sd = Rm``
* vmov(Rd, Sm) ``Rd = Sm``

The FPU has a register called FPSCR, which is similar to ARM's core APSR and stores condition codes and other data. The following instructions provide access to it.

* vmrs(APSR\_nzcv, FPSCR)

Move floating point N、Z、C、V  flags to APSR N、Z、C、V flags.

This is done after instructions such as FPU comparison, so that the condition code can be tested by assembly code. The following is the general form of the instruction.

* vmrs(Rd, FPSCR) ``Rd = FPSCR``

Move between FPU register and memory
------------------------------------

* vldr(Sd, [Rn, offset]) ``Sd = [Rn + offset]``
* vstr(Sd, [Rn, offset]) ``[Rn + offset] = Sd``

Where ``[Rn + offset]`` represents the memory address obtained by adding Rn to the offset. The unit is byte. Since each floating-point value occupies a 32-bit word, when accessing a floating-point array, the offset must always be a multiple of 4 bytes.

Data comparison
---------------

* vcmp(Sd, Sm)

Compare the values in Sd and Sm, and set the FPU N、C、Z、V flags. After this, there is usually  ``vmrs(APSR_nzcv, FPSCR)`` to enable the results to be detected.

Conversion between integer and floating point
---------------------------------

* vcvt\_f32\_s32(Sd, Sm) ``Sd = float(Sm)``
* vcvt\_s32\_f32(Sd, Sm) ``Sd = int(Sm)``
