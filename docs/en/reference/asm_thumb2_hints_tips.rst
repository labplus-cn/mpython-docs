 Tips and tricks
==============

The following are examples of using the inline assembler and information about solving its limitations. In this document, the term "assembler function" is.
Refers to the function declared with the  ``@micropython.asm_thumb`` decorator in Python, and "subroutine" refers to the assembler code called from the assembler function.

Code branches and subroutines
-----------------------------

It is important to know that the mark relative to the assembly function is local. It is not yet possible to call a subroutine defined in a function from another function.

Call the subroutine, then send the command  ``bl(LABEL)`` . This will transfer control to the instruction after the ``label(LABEL)`` instruction and store the return address in the link register（ ``lr`` or ``r14`` ）.
To return the instruction, send ``bx(lr)`` , which will continue the execution of the instruction after the subroutine call. This mechanism means that if a subroutine calls another subroutine, it must save the link register before the call and restore it before terminating.

The following example illustrates the function call. Note：At the beginning, all subroutine calls must be branched：The subroutine ends with ``bx(lr)`` , and the external function just ends with the Python function style "descent".

::

    @micropython.asm_thumb
    def quad(r0):
        b(START)
        label(DOUBLE)
        add(r0, r0, r0)
        bx(lr)
        label(START)
        bl(DOUBLE)
        bl(DOUBLE)

    print(quad(10))

The following code example demonstrates nested (recursive) calls: classic Fibonacci sequence. Here, before the recursive call, the link register is saved with other registers, and the program logic needs to save this register.

::

    @micropython.asm_thumb
    def fib(r0):
        b(START)
        label(DOFIB)
        push({r1, r2, lr})
        cmp(r0, 1)
        ble(FIBDONE)
        sub(r0, 1)
        mov(r2, r0) # r2 = n -1
        bl(DOFIB)
        mov(r1, r0) # r1 = fib(n -1)
        sub(r0, r2, 1)
        bl(DOFIB)   # r0 = fib(n -2)
        add(r0, r0, r1)
        label(FIBDONE)
        pop({r1, r2, lr})
        bx(lr)
        label(START)
        bl(DOFIB)

    for n in range(10):
        print(fib(n))

Transfer and return parameters
---------------------------

This tutorial details the feature that the assembler function can support 0 to 3 parameters. These three parameters must (if used) be named ``r0`` 、 ``r1`` and ``r2`` . When the code is executed, the register will be initialized to this value.

The data types that can be transferred in this way are integers and memory addresses. With the current firmware, all possible 32-bit values can be transmitted and returned. If the return value may set the most significant bit，
You should use the Python type hint to enable MicroPython to determine whether the value should be interpreted as a signed or unsigned integer：Type ``int`` or ``uint`` .

::

    @micropython.asm_thumb
    def uadd(r0, r1) -> uint:
        add(r0, r0, r1)

``hex(uadd(0x40000000,0x40000000))`` 0x80000000 will be returned, proving the transmission and return of different integers of 30 and 31 bits.

The limitation of the number of parameters and return values can be overcome by the ``array`` module method, which allows access to any number of values of any type.

Multiple parameters
~~~~~~~~~~~~~~~~~~

If a Python integer array is passed as an argument to the assembly function, the function will receive a continuous set of integer addresses. So multiple parameters can be passed as elements of a single array.
Similarly, a function can return multiple values by assigning multiple values to array elements. The assembly function cannot yet determine the length of the array: this needs to be transferred to the function.

This usage of arrays can be expanded to use more than three arrays. This is done indirectly： ``uctypes`` module support ``addressof()`` ,
It will return the array address passed as a parameter. Therefore, you can fill the integer array with the addresses of other arrays:

::

    from uctypes import addressof
    @micropython.asm_thumb
    def getindirect(r0):
        ldr(r0, [r0, 0]) # Address of array loaded from passed array 
        ldr(r0, [r0, 4]) # Return element 1 of indirect array (24) 
    def testindirect():
        a = array.array('i',[23, 24])
        b = array.array('i',[0,0])
        b[0] = addressof(a)
        print(getindirect(b))

Non-integer data type
~~~~~~~~~~~~~~~~~~~~~~

These can be handled by arrays of appropriate data types. For example, single-precision floating-point data can be processed as follows. This code example requires a floating-point array and replaces its contents with its square.

::

    from array import array

    @micropython.asm_thumb
    def square(r0, r1):
        label(LOOP)
        vldr(s0, [r0, 0])
        vmul(s0, s0, s0)
        vstr(s0, [r0, 0])
        add(r0, 4)
        sub(r1, 1)
        bgt(LOOP)

    a = array('f', (x for x in range(10)))
    square(a, len(a))
    print(a)

The uctypes module supports the use of data structures beyond the scope of simple arrays. It enables Python data structures to be mapped to byte array instances, which can then be transferred to assembler functions.

Named constant
---------------

By using named constants instead of randomly naming codes with numbers, assembly code can be made more readable and maintainable. Can be achieved by:

::

    MYDATA = const(33)

    @micropython.asm_thumb
    def foo():
        mov(r0, MYDATA)

The const() construction makes MicroPython replace the variable name with its value at compile time. If a constant is declared in an external Python scope, it can be shared among multiple assembly functions and Python code.

Assembly code as a class method
-------------------------------

MicroPython transfers the address of the object instance as the first parameter to the class method. Generally, this is not very useful for assembly functions. This can be avoided by declaring the function as a static class function:

::

    class foo:
      @staticmethod
      @micropython.asm_thumb
      def bar(r0):
        add(r0, r0, r0)

Use unsupported instructions
-------------------------------

These instructions can be encoded using data statements, as shown below. Although  ``push()`` and ``pop()`` are supported, the following example illustrates its principle. The necessary machine code can be found in the ARM v7-M Architecture Reference Manual. Please note: The first parameter of the data call is as follows

::

    data(2, 0xe92d, 0x0f00) # push r8,r9,r10,r11

Indicates that each subsequent parameter is a 2-byte value.

Overcoming MicroPython's integer limitation
--------------------------------------------

Pyboard chip contains a CRC generator. Its use raises a problem in MicroPython because the return value covers the full color gamut of 32 bits，
And small integers in MicroPython cannot have different values in bits 30 and 31. Use the following code to overcome this limitation：Use the assembler to put the results into arrays and Python code,
To cast the result to an unsigned integer of arbitrary precision.

::

    from array import array
    import stm

    def enable_crc():
        stm.mem32[stm.RCC + stm.RCC_AHB1ENR] |= 0x1000

    def reset_crc():
        stm.mem32[stm.CRC+stm.CRC_CR] = 1

    @micropython.asm_thumb
    def getval(r0, r1):
        movwt(r3, stm.CRC + stm.CRC_DR)
        str(r1, [r3, 0])
        ldr(r2, [r3, 0])
        str(r2, [r0, 0])

    def getcrc(value):
        a = array('i', [0])
        getval(a, value)
        return a[0] & 0xffffffff # coerce to arbitrary precision

    enable_crc()
    reset_crc()
    for x in range(20):
        print(hex(getcrc(0)))
