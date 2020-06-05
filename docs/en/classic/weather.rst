Getting online weather
==========


Example：Obtain meteorological information through the network and feed the meteorological information back to the oled screen.
::
    from mpython import*
    import json
    import urequests                    #Module for network access
    from seniverse import *             #Weather icon module
    from machine import Timer           #Timer module

    API_KEY = 'yourkey'                 #Know the weather API key（key）

    url_now="https://api.seniverse.com/v3/weather/now.json"           #Get the address of the live weather request
    url_daily="https://api.seniverse.com/v3/weather/daily.json"       #Request address to get multi-day weather forecast

    oled.DispChar('Network...',40,25)     #OLED screen displays networking tips
    oled.show()

    mywifi=wifi()
    mywifi.connectWiFi('yourESSID','yourpassword')          #connect WiFi network

    def nowWeather(apikey,location='ip',language='zh-Hans',unit='c'):         #Set the data returned by the weather
        nowResult = urequests.get(url_now, params={
            'key': apikey,
            'location': location,
            'language': language,
            'unit': unit
        })
        json=nowResult.json()
        nowResult.close()
        return json

    def dailyWeather(apikey,location='ip',language='zh-Hans',unit='c',start='0',days='5'):        #Set multi-day weather, only return today's data
        dailyResult = urequests.get(url_daily, params={
            'key': apikey,
            'location': location,
            'language': language,
            'start': start,
            'days': days
        })
        json=dailyResult.json()
        dailyResult.close()
        return  json


    def refresh():
        nowRsp=nowWeather(API_KEY)                 #Get weather information via API key
        dailyRsp=dailyWeather(API_KEY)             #Get multi-day weather forecast by API key

        today=dailyRsp['results'][0]['daily'][0]['date'][-5:]         #Display the current date and display“month-day”
        todayHigh=dailyRsp['results'][0]['daily'][0]['high']          #Highest temperature
        todaylow=dailyRsp['results'][0]['daily'][0]['low']            #Lowest temperature

        nowText=nowRsp['results'][0]['now']['text']                   #Weather phenomenon text
        nowTemper=nowRsp['results'][0]['now']['temperature']          #Temperature
        todayIco=nowRsp['results'][0]['now']['code']                  #Weather phenomenon icon
        city=nowRsp['results'][0]['location']['name']                 #Geographic location

        oled.fill(0)
        oled.bitmap(10,23,ico[todayIco],38,38,1)                   #Display current weather phenomenon icon
        oled.DispChar("%s,live weather" %city,0,0)
        oled.DispChar(today,90,0)
        oled.DispChar("%s℃/%s" %(nowTemper,nowText),70,25)        #Display current temperature
        oled.DispChar("%s~%s℃" %(todaylow,todayHigh),70,45)       #Show today's lowest and highest temperature
        oled.show()

    refresh()          #Data update

    tim1 = Timer(1)
    tim1.init(period=1800000, mode=Timer.PERIODIC,callback=lambda _:refresh())      #Fixed Time, refreshed every half hour



.. image:: /../images/classic/weather.jpg
    :align: center
    :scale: 60 %

Before use, import mpython, json, urequests, Timer, and weather icon seniverse modules（:download:`seniverse module </../../examples/network/seniverse/seniverse.py>`，Import the Seniverse module file into the root directory of the mPython File file）::

    from mpython import*
    import json
    import urequests
    from seniverse import *
    from machine import Timer

To use seniverse free weather API, you must first register an account on the weather website. You will get an API key, which is a unique string used to verify the legitimacy of API requests , Passing in the key parameter in the API request::

    API_KEY = 'yourkey'

Add the address of the request for the live weather and multi-day weather forecast (for more requests, please refer to the weather data option provided by the official weather website)::

    url_now="https://api.seniverse.com/v3/weather/now.json"           #Get the address of the live weather request
    url_daily="https://api.seniverse.com/v3/weather/daily.json"       #Request address to get multi-day weather forecast

To connect to your WiFi network, you need to set your WiFi name and password::

    mywifi=wifi()
    mywifi.connectWiFi('yourESSID','yourpassword')

Define weather results and the results returned by multi-day weather forecast::

    def nowWeather(apikey,location='ip',language='zh-Hans',unit='c'): 
        nowResult = urequests.get(url_now, params={
            'key': apikey,
            'location': location,
            'language': language,
            'unit': unit
        }) 
        return nowResult.json()

    def dailyWeather(apikey,location='ip',language='zh-Hans',unit='c',start='0',days='5'): 
        dailyResult = urequests.get(url_daily, params={
            'key': apikey,
            'location': location,
            'language': language,
            'start': start,
            'days': days
        })
        return  dailyResult.json()

.. Note::

    Parameters：``unit`` is the temperature unit,  ``c``  is Celsius degree. ``start``  is the starting time, such as ``-2`` the day before yesterday, ``-1`` yesterday，``0`` today，``1`` tomorrow. ``days`` is the number of days and returns the result of days from start. For more parameters, please refer to seniverse Weather official website。
    https://www.seniverse.com/doc


Selective output of all returned results, tuples can use subscript indexes to access the values in the tuple::

    today=dailyRsp['results'][0]['daily'][0]['date'][-5:]         #Current date, display“month-day”
    todayHigh=dailyRsp['results'][0]['daily'][0]['high']          #Highest temperature
    todaylow=dailyRsp['results'][0]['daily'][0]['low']            #Lowest temperature

    nowText=nowRsp['results'][0]['now']['text']                   #Weather phenomenon text
    nowTemper=nowRsp['results'][0]['now']['temperature']          #Temperature
    todayIco=nowRsp['results'][0]['now']['code']                  #Weather phenomenon icon
    city=nowRsp['results'][0]['location']['name']                 #Geographic location


.. Note::

    For specific usage of tuples, please refer to Python's tuples.
