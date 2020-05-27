:mod:`ussl` -- SSL/TLS module
=============================

.. module:: ussl
   :synopsis: TLS/SSL wrapper for socket objects

This module implements the corresponding :term: A subset of the `CPython` module, as described below. For details, refers to CPython document: `ssl <https://docs.python.org/3.5/library/ssl.html#module-ssl>`_

This module provides access to transport layer security (formerly known as “secure socket layer”) encryption and peer authentication tools for client and server-side network socket.

Functions
---------

.. function:: ssl.wrap_socket(sock, server_side=False, keyfile=None, certfile=None, cert_reqs=CERT_NONE, ca_certs=None)


Use sock (usually a usocket.socket instance of type SOCK_STREAM), And return an instance of ssl.SSLSocket, which wraps the basic stream in an SSL context.
The returned object has the usual stream interface methods, such as ``read()`` ，``write()`` etc.
In MicroPython, the returned objects do not expose socket interfaces and methods, such as recv()，send().
In particular, server-side SSL sockets should be created from ordinary sockets returned on ``accept()`` non-SSL listening server sockets。




.. warning::

    Some implementations of the module do not verify the server certificate, which makes the established SSL connection prone to middleman attacks.

EXception
----------

.. data:: ssl.SSLError

   This exception does not exist. Instead, use its base class OSError. 

Constant
---------

.. data:: ssl.CERT_NONE
          ssl.CERT_OPTIONAL
          ssl.CERT_REQUIRED

    Supported values for cert_reqs parameter.
