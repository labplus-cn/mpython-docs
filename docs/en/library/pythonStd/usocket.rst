*******************************
:mod:`usocket` -- Socket Module
*******************************

.. module:: usocket
   :synopsis: socket module

This module implements the corresponding :term:`CPython` a subset of modules, as follows, refers to CPython document for details: `socket <https://docs.python.org/3.5/library/socket.html#module-socket>`_

This module provides access to BSD socket interface. 

.. admonition:: differences with CPython
   :class: attention

    In order to improve efficiency and consistency, socket objects in MicroPython directly implement the `stream`(class file) interface. In CPython,
    To use ``makefile()`` method to convert the socket to a class file object. This method is still supported by micropython (but no operation),
    To use this method for CPython compatibility. 

Socket address format
------------------------

The following function uses the (ipv4_address, port) network address, ipv4_address Is a string of points and numbers, such as ``"8.8.8.8"`` ，
Port number of 1-65535. Be careful not to use domain names as ipv4_address，Domain name needs to be used first ``socket.getaddrinfo()`` for parsing.

The native socket address format of the ``usocket`` module is an opaque data type returned by the ``getaddrinfo`` function,
It must be used to resolve text addresses (including numeric addresses)::

    sockaddr = usocket.getaddrinfo('www.micropython.org', 80)[0][-1]
    # You must use getaddrinfo() even for numeric addresses 
    sockaddr = usocket.getaddrinfo('127.0.0.1', 80)[0][-1]
    # Now you can use that address 
    sock.connect(addr)

Using ``getaddrinfo`` is the most efficient and convenient way to process addresses (both in memory and processing power).


Function
---------

.. function:: socket(af=AF_INET, type=SOCK_STREAM, proto=IPPROTO_TCP)

  - ``af`` ：address

    - ``socket.AF_INET``:=2 — TCP/IP – IPv4
    - ``socket.AF_INET6`` :=10 — TCP/IP – IPv6

  - ``type`` ：socket type

    - ``socket.SOCK_STREAM``:=1 — TCP stream
    - ``socket.SOCK_DGRAM``:=2 — UDP Datagram
    - ``socket.SOCK_RAW`` :=3 — Raw Socket
    - ``socket.SO_REUSEADDR`` : =4 — socket reusable

  - ``proto`` ：protocol

    - ``socket.IPPROTO_TCP`` =6
    - ``socket.IPPROTO_UDP`` =17 


In general, proto parameters are not specified, because some MicroPython firmware provides default parameters::

  >>> s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  >>> print(s)
  <socket>

.. function:: getaddrinfo(host, port)

Converts the host domain name (host) and port (port) to a 5-tuple sequence used to create the socket. The tuple list is structured as follows::

  (family, type, proto, canonname, sockaddr)

Connection to a web address is shown below

  s = usocket.socket()
  s.connect(usocket.getaddrinfo('www.micropython.org', 80)[0][-1])

.. admonition:: differences with CPython
  :class: attention

    When an error occurs in this function, will trigger a ``socket.gaierror`` error（ ``OSError`` subclass）.  
    MicroPython does not have ``socket.gaierror`` , It will directly cause an OSError.  
    Note: The number of errors in ``getaddrinfo()`` constitutes a separate namespace,
    May not match the number of errors in the ``uerrno``  system error code module.
    To distinguish ``getaddrinfo()`` error, the error is marked with a negative number, The standard system error is a positive number (the number of errors can be accessed by using the e.args[0] attribute of the exception object).
    Use a negative number for the time being and it may change in the future.



socket class
============

Method
-------

.. method:: socket.close()

Mark socket closed and free all resources. Once this happens, all future operations on the socket object will be lost. If supported by the protocol, the remote terminal will receive EOF instructions.

The socket will automatically close when the memory fragment is recycled, but it is recommended to use close() to close when necessary

.. method:: socket.bind(address)

Bind the address and port number as a list or tuple. Socket must not be bound.

  - ``address`` ：A list or tuple of addresses and port numbers.

Example::

  addr = ("127.0.0.1",10000)
  s.bind(addr)




.. method:: socket.listen([backlog])

Listen to the socket so that the server can receive the connection. If ``backlog`` is specified, it must be at least 0 (if low, set it to 0); And specifies the number of unaccepted connections the system will allow before rejecting new connections. If not specified, the default reasonable value is selected.

  -  ``backlog`` ：The maximum number of accepted sockets, at least 0, or a reasonable value by default if not specified.

   
  
.. method:: socket.accept()


Receive connection requests. Socket needs to specify the address and listen for the connection. The return value is (conn, address)，
Where conn is the socket used to receive and send data, and address is the socket bound to the other end.
  
  - ``conn``：A new socket object that can be used to send and receive messages
  - ``address``：Client address to connect to the server

.. admonition::

  It can only be called after binding address port and monitoring, returning conn and address.


.. method:: socket.connect(address)

Connect to the remote socket at the specified address.

  - ``address``：Tuples or lists of addresses and port numbers

Example::

  host = "192.168.3.147"
  port = 100
  s.connect((host, port))

.. method:: socket.send(bytes)

Send data to the socket. The socket must be connected to a remote socket. Returns the number of bytes sent, which may be less than the data length ("short write"). 

  - ``bytes``：bytes type data

.. method:: socket.sendall(bytes)

Send all data to socket. Socket must be connected to a remote socket. Different from ``send()`` this method will try to send all data by continuously sending data blocks.

The behavior of this method on a non blocking socket is undefined. Therefore, it is recommended to use the ``write()`` method on MicroPython, It has the same no short write policy to block the socket and will return the number of bytes sent on the non blocking socket.

  - ``bytes``：bytes type data


.. method:: socket.recv(bufsize)

Receive data from socket. The return value is a byte object that represents the received data. The maximum amount of data received at one time is specified by `bufsize` .

  - ``bufsize``：Specify the maximum amount of data to receive at one time
  
Example::

  data = conn.recv(1024)


.. method:: socket.sendto(bytes, address)

Send data to the socket. Socket should not connect to remote socket because the destination socket is specified by address. Used for UDP communication to return the size of data sent.

  - ``bytes``：bytes type data
  - ``address``：Tuple of destination address and port number

.. method:: socket.recvfrom(bufsize)

Receive data from socket. The return value is a pair (bytes, address), where bytes is the byte object that receives the data and address is the address of the socket that sends the data. For UDP communication.

  - ``bufsize``：Specify the maximum amount of data to receive at one time

.. method:: socket.setsockopt(level, optname, value)

Sets the value of the given socket option. The required symbolic constants are defined in the socket module（SO_ * etc）. The value can be an integer or a byte like object that represents a buffer.

  - ``level``：Socket option level
  - ``optname``：socket option
  - ``value``：It can be an integer or a bytes class object that represents a buffer.
  
Example::

  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

.. method:: socket.settimeout(value)

Set the timeout in seconds.

Set timeout value` parameter can be a non-negative float number representing seconds, It can also be `None` . If a non-zero value is given, OSError if the timeout period value has been exceeded before the operation is completed, The subsequent socket operation will throw an exception.
If 0 is given, the socket is in non blocking mode. If 'none' is given, the socket is in blocking mode.

Example::

  s.settimeout(2)

.. method:: socket.setblocking(flag)

Set the blocking or non blocking mode ofsocket：If it is marked as false, the socket is set to non blocking mode instead of blocking mode.

his method is a shorthand for some settimeout() called:

   * ``sock.setblocking(True)`` amount to  ``sock.settimeout(None)``
   * ``sock.setblocking(False)`` amount to  ``sock.settimeout(0)``

  .. admonition:: Difference to CPython
    :class: attention

    CPython socket.timeout throws an exception in case of timeout, This is an OSError subclass. MicroPython directly causes the OSError。
    If you use it to catch exceptions, your code will work in both MicroPython and CPython.


.. method:: socket.makefile(mode='rb', buffering=0)

Returns a file object associated with a socket. The specific return type depends on the parameters of the given makefile(). This support is limited to binary mode（ 'rb' and 'wb' ）. 
The parameter of CPython：not supporting encoding 、 errors 、 newline 。

Socket must be blocking mode；Timeout is allowed, but if it occurs, internal buffer of the file object may end in an inconsistent state. 

.. admonition:: differences with CPython
  :class: attention

  * Since buffered streams are not supported by MicroPython, the value of the buffered parameter is ignored and will be processed when the value is 0 (unbuffered).
  * Closing all file objects returned by makefile() will also close the original socket.
.. method:: socket.read([size])

Read size bytes from socket. Returns a byte object. If not given ``size`` , according to similar :meth:`socket.readall()` mode operation. see below. 


.. method:: socket.readinto(buf[, nbytes])


Read bytes into buffer. If nbytes is specified, the maximum number of bytes can be read. Otherwise, the maximum number of bytes of  len(buf) is read. 
Just as ``read()`` ，This method follows the “no short reads” method.

Return value: the number of bytes read and stored in the buffer.


.. method:: socket.readline()

Receive a line of data, end with a line break, and return the object receiving the data.


.. method:: socket.write(buf)



Writes a byte buffer to the socket. This function will attempt to write all data to the socket (no short write).
However, for non blocking sockets, this may not be possible, and the return value will be less than the length of buf.

Return value: the number of bytes written.


.. exception:: usocket.error

   MicroPython does not have this exception.

   .. admonition:: Difference to CPython
        :class: attention

        CPython once had a socket.error had been deprecated, and it's an alias ``OSError`` 。In MicroPython中，``OSError`` is used directly.


Constant
------

.. data:: AF_INET
          AF_INET6

   Address cluster

.. data:: SOCK_STREAM
          SOCK_DGRAM

   Socket type

.. data:: IPPROTO_UDP
          IPPROTO_TCP

IP protocol 

.. data:: SOL_SOCKET

socket option level, default=4095
