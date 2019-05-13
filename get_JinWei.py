#This code is used to get the longitude and latitude of a giving address

# -*- coding: utf-8 -*-
import requests
import json
from retrying import retry

def return_JW(address):
    from urllib import parse
    query = {
     'key' : 'f247cdb592eb43ebac6ccd27f796e2d2',
     'address': address,
     'output':'json',
      }
    base = 'http://api.map.baidu.com/geocoder?'
    url = base+parse.urlencode(query)
    import urllib.request
    doc = urllib.request.urlopen(url)
    s = doc.read().decode('utf-8')
    import json
    jsonData = json.loads(s)
    lat=jsonData['result']['location']['lat']
    lng =jsonData['result']['location']['lng']
    return lat,lng
