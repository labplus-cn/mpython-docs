
.. _urequests:

.. module:: urequests
   :synopsis: Relevant functional functions of the HTTP client, providing various HTTP request methods

:mod:`urequests` --- Related functions of HTTP client
================

Before we used the socket library, this tool as a primer is still good, for understanding the basic concepts of some crawlers, its helpful to master it.
After get started, we need to learn some more advanced content and tools to facilitate our crawling.
Then this section briefly introduces the basic usage of urequests library.

Response class
---------

.. class:: Response(s)

The Response class object contains the server's response to the HTTP request.

    - ``s``-ussl object

Method
~~~~~~~

.. method:: close()

Shutdown socket。

.. decorator:: content

Returns the content of the response, in bytes.

.. decorator:: text

Return the content of the response as text, encoded as unicode.

.. method:: json()

Return response json encoded content and convert to dict type.

Method
---------

.. method:: request(method, url, data=None, json=None, headers={},params=None,files=None)

Send an HTTP request to the server.

    - ``method`` - HTTP method to use
    - ``url`` - URL to send
    - ``data`` - To append to the body of the request. If a dictionary or tuple list is provided, the form will be encoded.
    - ``json`` - json is used to attach to the body of the request.
    - ``headers`` - Dictionary of headers to send.
    - ``params`` - URL parameters attached to the URL. If a dictionary or tuple list is provided, the form will be encoded.
    - ``files`` - Used for file upload, the type is 2-tuple, which defines the file name, file path and content type. As follows,{‘name’, (file directory,content-type)}


.. method:: head(url, **kw)

Send HEAD request and return Response object.

    - ``url`` - Request object URL
    - ``**kw`` - The parameters of the request method.

.. method:: get(url, **kw)

Send GET request and return Response object.

    - ``url`` - Request object URL
    - ``**kw`` - Parameters of request method.

.. method:: post(url, **kw)

Send POST request and return Response object.

    - ``url`` - Request object URL
    - ``**kw`` - Parameters of request method.
    

.. method:: put(url, **kw)

Send PUT request and return Response object.

    - ``url`` - RRequest object URL
    - ``**kw`` - Parameters of request method.
    
.. method:: patch(url, **kw)

Send PATCH request, return Response object.

    - ``url`` - Request object URL
    - ``**kw`` - Parameters of request method.


    
.. method:: delete(url, **kw)

Send a DELETE request. Return Response object。

    - ``url`` - Request object URL
    - ``**kw`` - Parameters of request method.



.. literalinclude:: /../../examples/network/example_requests.py
    :caption: requests example
    :linenos:
