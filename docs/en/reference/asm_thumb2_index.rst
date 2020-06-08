.. _asm_thumb2_index:

Inline assembler of Thumb2 architecture
=========================================

This document assumes that you are familiar with assembly language programming, so you should read this document after studying the tutorial（ :ref:`tutorial <pyboard_tutorial_assembler>`）.
For a detailed description of the instruction set, see《Architecture Reference Manual》. The inline assembler supports a subset of the ARM Thumb-2 instruction set described here.
This syntax tries to be as close as possible to the syntax defined in the above ARM manual for conversion to Python function calls.

Unless otherwise stated, the instruction operates on 32-bit signed integer data. Most supported instructions only run on registers  ``R0-R7`` ：
If it support ``R8-R15`` , then explain. Before returning from the function, the registers  ``R8-R12``  must be restored to their initial values. The registers  ``R13-R15`` constitute the link register, stack pointer and program counter respectively. 

File specification
--------------------

Where possible, the behavior of each instruction is introduced in Python, for example

* add(Rd, Rn, Rm) ``Rd = Rn + Rm``

This supports demonstration of the effect of instructions in Python. In some cases, this is not feasible because Python does not support concepts such as indirect methods. In the relevant page, the virtual program code used in this case is introduced.

Instruction classification
----------------------

The following section details the subset of the ARM Thumb-2 instruction set supported by MicroPython.

.. toctree::
   :maxdepth: 1
   :numbered:

   asm_thumb2_mov.rst
   asm_thumb2_ldr.rst
   asm_thumb2_str.rst
   asm_thumb2_logical_bit.rst
   asm_thumb2_arith.rst
   asm_thumb2_compare.rst
   asm_thumb2_label_branch.rst
   asm_thumb2_stack.rst
   asm_thumb2_misc.rst
   asm_thumb2_float.rst
   asm_thumb2_directives.rst

Examples
--------------

This section provides more code examples and tips for using the assembler.

.. toctree::
   :maxdepth: 1
   :numbered:

   asm_thumb2_hints_tips.rst

Reference list
----------

-  Assembler tutorial :ref:`Assembler Tutorial <pyboard_tutorial_assembler>`
-  `Wiki tips and tricks
   <http://wiki.micropython.org/platforms/boards/pyboard/assembler>`__
-  `uPy inline assembly source code，
   emitinlinethumb.c <https://github.com/micropython/micropython/blob/master/py/emitinlinethumb.c>`__
-  `ARM Thumb2 instruction set quick reference card <http://infocenter.arm.com/help/topic/com.arm.doc.qrc0001l/QRC0001_UAL.pdf>`__
-  `RM0090 Reference Guide <http://www.google.ae/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&sqi=2&ved=0CBoQFjAA&url=http%3A%2F%2Fwww.st.com%2Fst-web-ui%2Fstatic%2Factive%2Fen%2Fresource%2Ftechnical%2Fdocument%2Freference_manual%2FDM00031020.pdf&ei=G0rSU66xFeuW0QWYwoD4CQ&usg=AFQjCNFuW6TgzE4QpahO_U7g3f3wdwecAg&sig2=iET-R0y9on_Pbflzf9aYDw&bvm=bv.71778758,bs.1,d.bGQ>`__
-  ARM v7-M Construction Reference Manual (simple registration is available on the ARM website, and is also available on the academic website, please pay attention to the expired version)
