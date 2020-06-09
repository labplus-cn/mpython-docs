Push and pop
==================

File Specification
--------------------

The ``push()`` and ``pop()`` instructions will take a subset of the general registers R0-R12 and the link register (lr or R14) or all register sets as their parameters.
For any Python setting, the order in which the registers are specified does not matter. Therefore, in the following example, the pop() instruction will restore the contents of R1, R7, and R8 before push():

* push({r1, r8, r7}) Save 3 registers on the stack.
* pop({r7, r1, r8}) Reply R1、R7、R8。

 Stack operation
----------------

* push({regset}) Push a set of registers onto the stack
* pop({regset}) Reply a set of registers from the stack
