Various instructions
==========================

* nop() ``pass`` no operation.
* wfi() Suspend execution in a low-power state until an interruption occurs.
* cpsid(flags) Set priority mask register-disable interrupt.
* cpsie(flags) Clear priority mask register-enable interrupt.
* mrs(Rd, special_reg) ``Rd = special_reg`` Copy special registers to general registers. Special registers may be IPSR (Interrupt Status Register) or BASEPRI (Basic Priority Register). IPSR provides a way to determine the exception number of the interrupt being processed. If there is no interrupt being processed, it contains 0.

Currently, the ``cpsie()`` and ``cpsid()`` functions have been partially implemented. These functions require but ignore marker parameters and serve as a way to enable or disable interrupts.
