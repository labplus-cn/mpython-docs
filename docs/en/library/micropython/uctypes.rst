:mod:`uctypes` --  Access binary data in a structured way
========================================================

.. module:: uctypes
   :synopsis:  Access binary data in a structured way

This module implements the “external data interface” for MicroPython. The idea behind it is similar to CPython's ``ctypes`` module, but the actual API is different, streamlined and small-scale optimization.
The basic idea of this module is to define a data structure layout with approximately the same power as that allowed by C language, and then access it to reference subfields using familiar point syntax.

.. warning::

  ``uctypes`` The module allows access to any memory address of the machine (including I/O and control registers). Using it carelessly may cause crashes, data loss, and even hardware failure.

.. seealso::

    :mod:`ustruct` module: Standard Python methods for accessing binary data structures (not well extended to large and complex structures).


For examples::

    import uctypes

    # Example 1: Subset of ELF file header
    # https://wikipedia.org/wiki/Executable_and_Linkable_Format#File_header
    ELF_HEADER = {
        "EI_MAG": (0x0 | uctypes.ARRAY, 4 | uctypes.UINT8),
        "EI_DATA": 0x5 | uctypes.UINT8,
        "e_machine": 0x12 | uctypes.UINT16,
    }

    # "f" is an ELF file opened in binary mode
    buf = f.read(uctypes.sizeof(ELF_HEADER, uctypes.LITTLE_ENDIAN))
    header = uctypes.struct(uctypes.addressof(buf), ELF_HEADER, uctypes.LITTLE_ENDIAN)
    assert header.EI_MAG == b"\x7fELF"
    assert header.EI_DATA == 1, "Oops, wrong endianness. Could retry with uctypes.BIG_ENDIAN."
    print("machine:", hex(header.e_machine))


    # Example 2: In-memory data structure, with pointers
    COORD = {
        "x": 0 | uctypes.FLOAT32,
        "y": 4 | uctypes.FLOAT32,
    }

    STRUCT1 = {
        "data1": 0 | uctypes.UINT8,
        "data2": 4 | uctypes.UINT32,
        "ptr": (8 | uctypes.PTR, COORD),
    }

    # Suppose you have address of a structure of type STRUCT1 in "addr"
    # uctypes.NATIVE is optional (used by default)
    struct1 = uctypes.struct(addr, STRUCT1, uctypes.NATIVE)
    print("x:", struct1.ptr[0].x)


    # Example 3: Access to CPU registers. Subset of STM32F4xx WWDG block
    WWDG_LAYOUT = {
        "WWDG_CR": (0, {
            # BFUINT32 here means size of the WWDG_CR register
            "WDGA": 7 << uctypes.BF_POS | 1 << uctypes.BF_LEN | uctypes.BFUINT32,
            "T": 0 << uctypes.BF_POS | 7 << uctypes.BF_LEN | uctypes.BFUINT32,
        }),
        "WWDG_CFR": (4, {
            "EWI": 9 << uctypes.BF_POS | 1 << uctypes.BF_LEN | uctypes.BFUINT32,
            "WDGTB": 7 << uctypes.BF_POS | 2 << uctypes.BF_LEN | uctypes.BFUINT32,
            "W": 0 << uctypes.BF_POS | 7 << uctypes.BF_LEN | uctypes.BFUINT32,
        }),
    }

    WWDG = uctypes.struct(0x40002c00, WWDG_LAYOUT)

    WWDG.WWDG_CFR.WDGTB = 0b10
    WWDG.WWDG_CR.WDGA = 1
    print("Current counter:", WWDG.WWDG_CR.T)

Define structure layout
-------------------------

The structure layout is defined by “descriptors” - a python dictionary that encodes field names as keys and uses them as associated values to access other properties they need::

    {
        "field1": <properties>,
        "field2": <properties>,
        ...
    }

Currently，``uctypes`` need to specify the offset of each field. The offset unit in bytes at the beginning of the structure.

The following are examples of coding for various field types:

* Scalar type::

    "field_name": offset | uctypes.UINT32

  In other words, the value is a scalar type identifier that performs or operates on the field offset (in bytes) at the beginning of the structure. 

* Recursive structure::

    "sub": (offset, {
        "b0": 0 | uctypes.UINT8,
        "b1": 1 | uctypes.UINT8,
    })

  That is, the value is a 2-tuple, the first element is the offset, and the second is the structure descriptor Dictionary (Note: the offset in the recursive descriptor is related to the structure it defines). 
  Of course, recursive structures can be specified not only through a text dictionary, but also by referencing the structure descriptor dictionary by name (defined earlier). 

* Array of original type::

      "arr": (offset | uctypes.ARRAY, size | uctypes.UINT8),

  That is, value is a 2-tuple, the first element of which is the ARRAY flag ORed and offset, and the second is the element in the ORed array of scalar element type.

* Array of aggregate type::

    "arr2": (offset | uctypes.ARRAY, size, {"b": 0 | uctypes.UINT8}),

  That is, value is a 3-tuple, the first element of which is the ARRAY flag ORed and offset, the second is the number of elements in the array, and the third is the descriptor of the element type. 

* Pointer to primitive type::

    "ptr": (offset | uctypes.PTR, uctypes.UINT8),

  That is, value is a 2-tuple, the first element of which is the PTR flag, ORed with the offset, and the second element is the scalar element type.

* Pointer to aggregate type::

    "ptr2": (offset | uctypes.PTR, {"b": 0 | uctypes.UINT8}),

  The ie value is a 2-tuple, the first element of which is the PTR flag ORed with offset, and second is the descriptor of the type pointed to.

* Bit address::

    "bitf0": offset | uctypes.BFUINT16 | lsbit << uctypes.BF_POS | bitsize << uctypes.BF_LEN,

ie value is a scalar value that contains the positioning field (type name is similar to the scalar type, but with the prefix BF), ORed has an offset that contains the scalar value of the bit field, and is further related to the bit OR the value and the bit length in the bit field.
Scalar values are shifted by BF_POS and BF_LEN respectively. The bit field position is counted from the least significant bit of the scalar (position with 0), and is the number of the rightmost bit of the field (in other words, it is the number of bits that the scalar needs to be shifted to the right) to extract the bit field). 

In the above example, the UINT16 value is first extracted at offset 0 (when accessing hardware registers, this detail may be important and requires specific access size and alignment). 
Then the rightmost bit is the bit field of the lsbit bit of this UINT16, and the length is bitsize bits, which will be extracted. 
For example, if lsbit is 0 and bitsize is 8, then it will effectively access the least significant byte of UINT16. 

Note that bit field operations are independent of the target byte order, especially the above example will access the least significant byte of UINT16 in little-endian and big-endian structures.
But it depends on the least significant bit being numbered 0. Some targets may use different numbers in their native ABI, but uctypes always use the above standardized numbers. 

Module content
---------------

.. class:: struct(addr, descriptor, layout_type=NATIVE)

    Instantiate the “external data structure” object based on the address of the structure in memory, the descriptor (encoded as a dictionary) and the layout type (see below). 

.. data:: LITTLE_ENDIAN

    Layout type of little-endian compressed structure. (Packing means that each field occupies the number of bytes defined in the descriptor, that is the alignment is 1). 

.. data:: BIG_ENDIAN

    Layout type of big-endian compressed structure。

.. data:: NATIVE

    Layout type of native structure-data byte order and alignment conforms to ABI of systems running MicroPython. 

.. function:: sizeof(struct, layout_type=NATIVE)

    Returns the size of the data structure in bytes. The structure parameter can be a class structure or a specific instantiated structure object (or its aggregate field). 

.. function:: addressof(obj)

    Returns the address of the object. The parameter should be a byte, byte array or other object that supports the buffer protocol (the address of the buffer is actually returned). 

.. function:: bytes_at(addr, size)

    Capture memory as bytes object with given address and size. Because the bytes object is immutable, the memory is actually copied and copied into the bytes object, so if the memory content changes later, the created object will retain the original value.

.. function:: bytearray_at(addr, size)

    Capture memory of given address and size as bytearray object. Unlike the bytes_at（）function above, memory is captured by reference, so it can also be written to, and you will access the current value at the given memory address.

.. data:: UINT8
          INT8
          UINT16
          INT16
          UINT32
          INT32
          UINT64
          INT64

    Integer type of structure descriptor. Provides 8, 16, 32, and 64-bit constants, including signed and unsigned. 

.. data:: FLOAT32
          FLOAT64

    Floating point type of structure descriptor. 
    

.. data:: VOID

    ``VOID`` is an alias ``UINT8`` , Used to conveniently define the void pointer of C：( ``uctypes.PTR`` , ``uctypes.VOID`` )

.. data:: PTR
          ARRAY

    Input pointer and array constants. Note that the structure has no explicit constants, it is implicit: the aggregate type without the ``PTR`` or ``ARRAY`` flag is a structure. 

Structure descriptors and instantiated structure objects
---------------------------------------------------------

Given the structure descriptor dictionary and its layout type, you can use :class:`uctypes.struct()`  constructor instantiates a specific structure instance at a given memory address.
Memory addresses usually come from the following sources:


* Predefined addresses when accessing hardware registers on bare metal systems. Look up these addresses in the data sheet of a specific MCU / SoC.
* As a return value from calling some FFI (external function interface) functions.

* From `uctypes.addressof()`, when you want to pass parameters to the FFI function, or, in order to access some data of the I / O (for example, data read from a file or network socket).

Structural object
-----------------

Structural objects allow access to individual fields using standard dot notation：``my_struct.substruct1.field1`` 。
If the field is of scalar type, getting it will produce the original value (Python integer or float) corresponding to the value contained in the field.
Scalar fields can also be assigned to.

If the field is an array, you can use standard subscript operators to access its individual elements  ``[]`` - including reading and allocation.

If a field is a pointer, it can be used ``[0]`` Syntax dereference (corresponding to C  ``*`` operator, but also ``[0]``  applies to C). Also supports the use of other integer values (but 0) to subscribe to pointers, the semantics are the same as in C.

In summary, accessing structure fields usually follows the C syntax, except for pointer dereferencing, when you need to use the ``[0]`` operator instead of  ``*`` .

Limitation
-----------

1. Accessing non-scalar fields causes allocation of intermediate objects to represent them. This means that special attention should be paid to structures that the layout needs to access when memory allocation is disabled (for example, from interrupts). Suggestions as follows:

  * Avoid access to nested structures. For example, instead of  ``mcu_registers.peripheral_a.register1`` define a separate layout descriptor for each peripheral device to access ``peripheral_a.register1`` . Or only cache specific peripherals: If the register consists of multiple bit fields, you need to cache references to specific registers: ``peripheral_a = mcu_registers.peripheral_areg_a = mcu_registers.peripheral_a.reg_a``

  * Avoid using other non-scalar data, such as arrays. For example, instead of peripheral_a.register[0] use peripheral_a.register0. Similarly, another method is to cache intermediate values, for example ``register0 = peripheral_a.register[0]`` 

2. ``uctypes`` module supports a limited range of offsets. The exact range supported is considered to be an implementation detail, and the general recommendation is to split the structure definition into a maximum value from a few kilobytes to tens of kilobytes.
In most cases, this is a natural situation anyway. For example, it does not make sense to define all the registers of the MCU (expanded to the 32-bit address space) in a structure, but define peripheral modules through peripheral modules.
In some extreme cases, you may need to manually split the structure of several parts (for example, if you access a native data structure with a multi-megabyte array in the middle, although this will be a very synthetic situation). 
