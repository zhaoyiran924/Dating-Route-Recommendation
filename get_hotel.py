#This code use Baidu_Map and addresses we searched to get the route of date and store in Baidu_Map.txt

# -*- coding: utf-8 -*-
import requests
import json
import io
import os
import re
import codecs
import sys
import importlib
importlib.reload(sys)

global null
false = False
true = True
null=''

def get_page(url,headers):
    try:
        response = requests.get(url,headers=headers)
        #print(response)
        response.encoding = response.apparent_encoding
        return response.text
    except Exception as e:
        print(e)

def get_hotel():
    basic_url = "http://m.ctrip.com/webapp/hotel/shanghai2/p1"
    headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36",
    "Cookie": "supportwebp=true; _abtest_userid=9154e050-8f93-42e0-9c4f-d8e6691396d4; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; ibu_wws_c=1554792766656%7Czh-cn; _ga=GA1.2.860010712.1552200767; _RSG=IgaAfwI4MKFTE0lsIylXt9; _RDG=289a56a4fb5def20b70d9d5f73af5bcdba; _RGUID=f516112e-a92a-4a92-9de1-bfc4b6bc039d; __zpspc=9.1.1552200772.1552200772.1%234%7C%7C%7C%7C%7C%23; _jzqco=%7C%7C%7C%7C1552200772384%7C1.1178580234.1552200772179.1552200772179.1552200772180.1552200772179.1552200772180.0.0.0.1.1; _bfi=p1%3D100101991%26p2%3D0%26v1%3D2%26v2%3D0; MKT_Pagesource=H5; _fpacid=09031153211979529009; GUID=09031153211979529009; ASP.NET_SessionSvc=MTAuMjguMTEyLjE5fDkwOTB8amlucWlhb3xkZWZhdWx0fDE1NTE5NTQ1NTEzMjg; hotelist=d%3DW5kMZWZjpbmkVkMDkTwMzExNTMyMTE5Nzk1MjkwMDk%3D; hotelpst=undefined; _HGUID=%06UQVQQR%05M%01YR%01MT%01YRMY%04%05QM%02%06%03T%02V%02%03PSY%04; fcerror=1790918599; _zQdjfing=1336fa3165bb65b02e4ea08465b02e1336fa3a923ad5c08665b02e65b02e; Union=OUID=&AllianceID=66672&SID=508670&SourceID=&AppID=&OpenID=&Expires=1553950359128; _RF1=58.247.22.163; hotelust=1553345576990; _bfa=1.1552200763451.49v9ae.1.1552200763451.1553345588535.6.50.212093; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1552975949894%7D%2C%7B%22aid%22%3A%2266672%22%2C%22timestamp%22%3A1553345588763%7D%5D"
    }
    for i in range(1):
        url = basic_url
        page = get_page(url,headers)
        f = codecs.open('unicode.txt', 'wb+', 'utf-8')
        f.write(page)
        
    #get the array of address
    f = open("unicode.txt","r")
    str = f.read()
    f.close()
    p = r"[\u4e00-\u9fa5]+路\d+号"
    pattern = re.compile(p)
    find = pattern.findall(str)
    address = []
    for i in range(10):
        address.append(find[i])

    #get the dict of address which contains ten elements
    p = r'hotelAddress.+hotelid'
    pattern = re.compile(p)
    find = pattern.findall(str,10)
    f = codecs.open('after_change.txt', 'w', 'utf-8')
    total = 10
    count = 0
    for element in find:
        if count<total:
            f.write(element)
            f.write("\n")
            count = count + 1
            
    #get the array of price
    f = open("after_change.txt")
    str = f.read()
    p = r'(priceAfterAllReturn\".\d+)'
    pattern = re.compile(p)
    find = pattern.findall(str,10)
    fp = codecs.open('price.txt','w','utf-8')
    for i in range(10):
        fp.write(find[i])
        fp.write('\n')
    fp.close()
    price = []
    f = open("price.txt")
    str = f.read()
    p = r"(\d+)"
    pattern = re.compile(p)
    find = pattern.findall(str)
    price_hotel = []
    for i in range(10):
        # fp = codecs.open('address_array.txt','a','utf-8')
        # fp.write(find[i])
        # fp.write('\n')
        price.append(find[i])
        price_hotel.append(find[i])

    #get the array of shortname
    f = open("after_change.txt")
    str = f.read()
    p = r'(shortName(.+?)tag)'
    pattern = re.compile(p)
    find = pattern.findall(str)
    fp = codecs.open('name_array.txt','w','utf-8')
    for i in range(10):
        fp.write(find[i][1])
        fp.write('\n')
    fp.close()

    name = []
    f = open("name_array.txt")
    p = r"(\w+[\u4e00-\u9fa5]+|[\u4e00-\u9fa5]+|\w+)"
    pattern = re.compile(p)
    for i in range(10):
        str = f.readline()
        find = pattern.findall(str)
        name.append(find[0])
    address_ten = []
    fp = codecs.open('address_array.txt','w','utf-8')
    for i in range(10):
        fp.write(name[i]+"  "+price[i]+"  "+address[i])
        address_ten.append("上海市"+address[i])
        fp.write("\n")
    print("\n")
    print("开始打印找到的酒店")
    print(name)
    return address_ten,price_hotel
