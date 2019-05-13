# -*- coding: utf-8 -*-
import requests
import json
from retrying import retry


# address = '上海市长宁区延安西路1882号'
# url= 'http://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak=ClmC68V8M22O6lxjZSwdkW0kUYg1F7z3'
# url_use = url.format(address)
#
# print(url_use)
#
# headers = {
# "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"
# }
#
# response = requests.get(url,headers=headers)
# json_str = response.content.decode()
# answer = json.loads(json_str)
# print(answer)

def return_JW(address):

    from urllib import parse

    #address = input("输入起点：")

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

# if __name__ == '__main__':
#     print(return_JW())
#     # print(__name__)
