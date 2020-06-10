:mod:`uerrno` -- System Error Code
===================================

.. module:: uerrno
   :synopsis: System Error Code

This module implements the corresponding :term:`CPython` A subset of modules, as follows. Refers to CPython document for details: `errno <https://docs.python.org/3.5/library/errno.html#module-errno>`_

This module provides access symbol error codes for :ref:`OSError <OSError>` . Specific code listings depend on :term:`MicroPython port`.


Constant
---------

.. data:: EEXIST, EAGAIN, etc.

    Error Code，based on ANSI C/POSIX standard. All error codes start with “E”. Errors can usually be accessed as ``exc.args[0]`` ，amongst ``exc`` is ``OSError`` as an example.

    Example::

        try:
            uos.mkdir("my_dir")
        except OSError as exc:
            if exc.args[0] == uerrno.EEXIST:
                print("Directory already exists")

.. data:: errorcode

    Dictionary maps numeric error codes to strings with symbolic error codes (see above)::

        >>> print(uerrno.errorcode[uerrno.EEXIST])
        EEXIST


===================================  ================  ====================================
Error                                Value             Description
``uerrno.EPERM``                      1                Operation not permitted
``uerrno.ENOENT``                     2                No such file or directory
``uerrno.ESRCH``                      3                No such process
``uerrno.EINTR``                      4                Interrupted system call
``uerrno.EIO``                        5                I/O error
``uerrno.ENXIO``                      6                No such device or address
``uerrno.E2BIG``                      7                Argument list too long
``uerrno.ENOEXEC``                    8                Exec format error
``uerrno.EBADF``                      9                Bad file number
``uerrno.ECHILD``                     10               No child processes
``uerrno.EAGAIN``                     11               Try again
``uerrno.ENOMEM``                     12               Out of memory
``uerrno.EACCES``                     13               Permission denied
``uerrno.EFAULT``                     14               Bad address
``uerrno.ENOTBLK``                    15               Block device required
``uerrno.EBUSY``                      16               Device or resource busy
``uerrno.EEXIST``                     17               File exists
``uerrno.EXDEV``                      18               Cross-device link
``uerrno.ENODEV``                     19               No such device
``uerrno.ENOTDIR``                    20               Not a directory
``uerrno.EISDIR``                     21               Is a directory
``uerrno.EINVAL``                     22               Invalid argument
``uerrno.ENFILE``                     23               File table overflow
``uerrno.EMFILE``                     24               Too many open files
``uerrno.ENOTTY``                     25               Not a typewriter
``uerrno.ETXTBSY``                    26               Text file busy
``uerrno.EFBIG``                      27               File too large
``uerrno.ENOSPC``                     28               No space left on device
``uerrno.ESPIPE``                     29               Illegal seek
``uerrno.EROFS``                      30               Read-only file system
``uerrno.EMLINK``                     31               Too many links
``uerrno.EPIPE``                      32               Broken pipe
``uerrno.EDOM``                       33               Math argument out of domain of func
``uerrno.ERANGE``                     34               Math result not representable
``uerrno.EWOULDBLOCK``                11               Operation would block
``uerrno.EOPNOTSUPP``                 95               Operation not supported on transport endpoint
``uerrno.EAFNOSUPPORT``               97               Address family not supported by protocol
``uerrno.EADDRINUSE``                 98               Address already in use
``uerrno.ECONNABORTED``               99               Software caused connection abort
``uerrno.ECONNRESET``                 104              Connection reset by peer
``uerrno.ENOBUFS``                    105              No buffer space available
``uerrno.EISCONN``                    106              Transport endpoint is already connected
``uerrno.ENOTCONN``                   107              Transport endpoint is not connected
``uerrno.ETIMEDOUT``                  110              Connection timed out
``uerrno.ECONNREFUSED``               111              Connection refused
``uerrno.EHOSTUNREACH``               113              No route to host
``uerrno.EALREADY``                   114              Operation already in progress
``uerrno.EINPROGRESS``                115              Operation now in progress
===================================  ================  ====================================
