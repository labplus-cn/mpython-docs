Parsing JSON
==============

JSON (JavaScript Object Notation, JS Object Notation) is a lightweight data exchange format. It uses a text format that is completely independent of the programming language to store and represent data, which is easy for humans to read and write, and also easy for machine analysis and generation, so it is widely used in the Internet.

In python, json and dict are very similar, both are in the form of key-value, and json and dict can also be easily converted between each other through the: :mod:`json` module.

* json：Is a data format, is a pure string, is essentially a file organization, such as your familiarntxt、csv、doc、docx、xls、xlsx files, etc.

* dict：is a data structure, such as list, set, string str, array。

Network access to parse JSON
------------------------------

The http protocol uses a request / response model, the browser or client sends a request, and the server responds。

For example, if you want to obtain the IP address and other information from the open interface http://ip-api.com/json/ , we enter the address directly in the browser, you can see：

.. image:: /../images/tutorials/httpjson.png
    :align: center
    :scale: 100 %

This is a JSON array containing information such as IP address. By accessing this URL, we can get the information and return the string TEXT, and use ujson.loads(str) to give the string to the generated DICT dictionary type, we can directly read the key （key）to obtain the corresponding value（value）.


.. literalinclude:: /../../examples/network/ip_parsing_json.py
    :caption: Display part of the information on the website on the OLED display
    :linenos:


.. image:: /../images/tutorials/json.jpg
    :align: center
    :scale: 70 %


We analyze it step by step in the interactive programming environment of REPL and can view the results more intuitively.

First, import mpython、json、urequests modules::

    >>> from mpython import*
    >>> import json
    >>> import urequests

Connect to WiFi network, then set up your WiFi ID and Password::

    >>> mywifi=wifi()
    >>> mywifi.connectWiFi('yourESSID', 'yourpassword')
    Connecting to network...
    Connecting to network...
    Connecting to network...
    WiFi Connection Successful,Network Config:('','','','')

Add request address, send GET request, get data returned by third-party interface of webpage::

    >>> url_ip ="http://ip-api.com/json/"
    >>> rsp=urequests.get(url_ip)

The obtained data is returned in JSON data text format, print out, we can see the returned data::

    >>> ipJson=rsp.text
    >>> print(jpJson)
    {"as":"AS56040 China Mobile Communications Corporation","city":"Guangzhou","country":"China","countryCode":"CN","isp":"China Mobile communications corporation","lat":23.1292,"lon":113.264,"org":"China Mobile","query":"120.234.223.173","region":"GD","regionName":"Guangdong","status":"success","timezone":"Asia/Shanghai","zip":""}

.. Note::

    rsp.text is returned as JSON data text format.

Convert the obtained data to DICT dictionary type, print out, we can see the returned data::

    >>> ipDict=json.loads(ipJson)
    >>> print(ipDict)
    {'countryCode': 'CN', 'lon': 113.264, 'regionName': 'Guangdong', 'query': '120.234.223.173', 'city': 'Guangzhou', 'status': 'success', 'org': 'China Mobile', 'timezone': 'Asia/Shanghai', 'region': 'GD', 'lat': 23.1292, 'isp': 'China Mobile communications corporation', 'as': 'AS56040 China Mobile Communications Corporation', 'zip': '', 'country': 'China'}

.. Note::

    json.loads(str) parse JSON string and return object。

To type the key（key）in the DICT dictionary to get the corresponding information value（value），such as city, IP address::

    >>> ipDict['city']
    'Guangzhou'
    >>> ipDict['query']
    '120.234.223.173'

