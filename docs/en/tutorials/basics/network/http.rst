HTTP
=======

HTTP is based on the client / server (C / S) architectural model, exchanges information through a reliable link, and is a stateless request / response protocol.

A HTTP "Client" is an application (web browser or any other client) that connects to the server to send one or more HTTP requests to the server.

HTTP GET request
----------------

The following example shows how to download a webpage. HTTP uses port 80, you first need to send a “GET” request to download any content. As part of the request, you need to specify the page to retrieve.

.. literalinclude:: /../../examples/network/http_get.py
    :caption: socket implements HTTP get method:
    :linenos:

.. Hint::

    When using the socket module, please connect to wifi first and make sure you can access the Internet. For details of WiFi connection, see :ref:`配置wifi<network_base>` 。



``http_get('http://micropython.org/ks/test.html')`` , the mPython Board client sends a GET request of the range TEST path resource to the `micropython.org` server. After receiving the request, the server will return the data to the client.

 

urequest module
~~~~~~~~~~~~~

The above is to use the SOCKET to implement the HTTP GET request. Use :mod:`urequests` module, which encapsulates some common request methods of the HTTP protocol, is easier to use.


.. literalinclude:: /../../examples/network/http_get_request.py
    :caption: Use the urequest module to access the webpage
    :linenos:

More details :mod:`urequests` module usage, please refer to the module description.

HTTP Server
----------------

.. literalinclude:: /../../examples/network/http_server_simplistic.py
    :caption: In the following example, the mPython Board is used as the HTTP server, and the on-board light sensor can be accessed using a browser:
    :linenos:


Run MAIN in REPL::

    >>> main()

.. image:: /../images/tutorials/http_1.png


Connect the same WiFi to the mobile phone or laptop to make it in the same LAN. Press the print prompt or oled screen to display ip, use the browser to access the IP address of the control panel host.

.. image:: /../images/tutorials/http_2.png



