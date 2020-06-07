.. _glossary:
Terminology
========

.. glossary::

    BareMetal
        Systems without (fully mature) OS, for example based on :term:`MCU` system.
        When running on bare metal systems, MicroPython effectively becomes a user-oriented operating system through a command interpreter (REPL).

    Board
        PCB board. Generally, this term is used to indicate :term:`MCU` system specific model. At times, actual application is  :term:`MicroPython port` reference to a specific board
        (may also mean :term:`Unix port <MicroPython Unix port>` boardless ports)。
   
    Callee-owned Tuple
        Tuples returned by some built-in functions/methods contain data that is valid for a limited time, usually until the next call to the same function (or set of related functions).
        After the next call, you can change the data in the tuple. This results in the following restrictions on the use of tuples owned by the callee-unable to store references to them.
        The only valid operation is to extract values from it (including making a copy). The tuples owned by Callee are MicroPython-specific constructs (not available in the general Python language) for memory allocation optimization.
        The idea is that the tuple owned by the callee is allocated once and stored in the callee. Subsequent calls do not require allocation, allowing multiple values to be returned when they cannot be allocated (for example, in an interrupt context) or undesirable (because allocation inherently causes memory fragmentation). Please note that the tuple owned by the callee is actually a variable tuple, which makes the exception to Python's rule that tuples are immutable. (It may be interesting why tuples are used for such purposes instead of mutable lists-the reason is that the list can also be changed from the user application side, so the user can perform operations on the list owned by the callee is not expected and possible Causes problems; tuples are protected.) Instead of a variable list-the reason is that the list can also be changed from the user application side, so the user can perform operations on the list owned by the callee, which the callee does not expect and may cause problems; a tuple is protected. (Instead of a mutable list-the reason is that the list can also be changed from the user application side, so the user can perform operations on the list owned by the callee, which the callee does not expect and may cause problems; a tuple is protected.)


    CPython
        CPython is the reference implementation of the Python programming language and the most famous programming language that most people used.
        However, it is one of many implementations (including Jython, IronPython, PyPy, etc., including MicroPython).
       Since there is no formal Python language specification, only CPython documentation, it is not always easy to draw a line between the Python language and a specific implementation of CPython.
        However, this leaves more freedom for other implementations. For example, MicroPython does many things different from CPython, while still eager to become a Python language implementation.

    GPIO
        Universal input/output. The easiest way to control electrical signals. Through GPIO, users can configure hardware signals as input or output，
        Aslo to set or get its digital signal value (logic "0" or "1"). Use of MicroPython :class:`machine.Pin`
        and :class:`machine.Signal` class extraction access to GPIO permissions。

    GPIO port
         A set of :term:`GPIO` pins, usually based on the hardware characteristics of the pins (for example: can be controlled by the same register).

    Interned String

        The string referenced by its (unique) identifier, not its address. Therefore, you can quickly compare internship strings by identifier, rather than by content.
        The disadvantage of the internship string is that the internship operation takes time (proportional to the number of existing internship strings, that is, it becomes slower and slower with time), and the space for the internship string is not recyclable.
        String training is done automatically by the MicroPython compiler and runtime, when the implementation needs it (for example, the function keyword parameter is represented by the training string id) or considered to be beneficial (for example, for short enough strings, there is a chance to repeat, So internship) They will save memory on the copy).
        由于上述缺点，大多数字符串和I / O操作不产生实际字符串。

    MCU

        Microcontroller. Compared with a complete computing system, microcontrollers usually have much fewer resources, but they are also smaller, less expensive, and consume less power.
        MicroPython is designed to be small and optimized to run on a generally recent microcontroller.

    micropython-lib
        MicroPython (usually) is distributed as a single executable/binary file with few built-in modules.
        Unlike the :term:`CPython` , MicroPython has no extended standard libraryMicroPython. But there is a related but independent project.
        `micropython-lib <https://github.com/micropython/micropython-lib>`_
        ，The project provides many implementations from modules in the standard library. However, a larger subset of these modules requires a POSIX-like environment
        (Partially supports Linux, MacOS, Windows), so it can only be run on the MicroPython Unix port.
        Some subsets of modules are also available on baremetal ports.

        Unlike the :term:`CPython` single-chip standard library, the micropython-lib module is designed to be copied manually or
        Use :term:`upip`to install separately.

    MicroPython port
        MicroPython supports different boards （ :term:`boards <board>`）, RTOS and OS can adapt to the new system relatively easily.
        MicroPython that supports a specific system is called the "port" of that system. The functional characteristics of different ports vary greatly. This document is intended for
        Common APIs available on different ports （"MicroPython core"）provide references. Note: Some ports may delete the API described here
        (Due to resource constraints). Such differences, as well as port-specific extensions beyond the core functionality of MicroPython, will be in separate,
        This is described in the port-specific files.

    MicroPython Unix port
        Unix端口是MicroPython（ :term:`MicroPython ports <MicroPython port>`）的主要端口之一。
        其设计为在与POSIX兼容的操作系统上运行，如Linux、MacOS、FreeBSD、Solaris等。
        该端口还可作为Windows端口的基础。端口的重要性在于在有许多不同板（ :term:`boards <board>`）时，
        任意两个用户不可能使用相同的板，几乎所有的现代操作系统都具有一定程度的POSIX兼容性，
        此时Unix端口可作为一种所有用户都可访问的"共同基础"。因此，Unix端口用于初始原型、不同种类
        的测试、开发独立于机器的特性等。我们建议所有MicroPython用户（甚至包括仅在 :term:`MCU` 系统中
        运行MicroPython的用户）都了解一下Unix（或Windows）端口，因为该端口可提高工作效率，且为MicroPython工作流的一部分。

    port
        :term:`MicroPython port` 或 :term:`GPIO port`。若您尚未理解上文，建议您使用如上述示例的完整规格。

    stream

        Also known as “file-like object"”. An object that provides sequential read and write access to the underlying data.
        A stream object implements the corresponding interface, which consists of similar methods  ``read()`` ， ``write()`` ，``readinto()`` ，``seek()`` ，``flush()`` ，``close()`` , etc. Streaming is an important concept in MicroPython,
        Many I/O objects implement the stream interface, so the context can be used consistently and interchangeably in different. More information about streams in MicroPython, see :mod:`uio` module。 
     

    upip
        (Literally meaning "micro pip"). MicroPython's package manager, inspired by  :term:`CPython` pip, but with smaller features and fewer features.
        upip can run on :term:`Unix port <MicroPython Unix port>` and :term:`baremetal` ports (providing file system and network support).
      
