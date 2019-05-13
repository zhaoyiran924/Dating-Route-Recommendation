#This code is a crawler to get manual shop on www.dianping.com

# -*- coding: utf-8 -*-
import requests
import json
import io
import os
import re
import codecs
from urllib.parse import urlencode
from selenium import webdriver

def get_page_index(use_url):
    url = use_url
    browser = webdriver.PhantomJS()
    browser.get(url)
    return browser.page_source

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')
    headers = {
    "Referer" : "https://m.dianping.com/shop/121859722",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    }

def main():
    #url = "https://m.dianping.com/isoapi/module"
    url = "https://baymax-api.dianping.com/midasmkt/ajax/shopAdsMob?cityId=1&userId=0&viewShopId=121859722&shopType=30&lat=0&lng=0&t=1553182399661&_=1553182399665&callback=Zepto1553182399658"
    html = get_page_index(url)
    for url in parse_page_index(html):
        print(url)

def do_what_need():
    headers = {
    "Referer" : "https://m.dianping.com/shop/121859722",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    }
    url = "https://baymax-api.dianping.com/midasmkt/ajax/shopAdsMob?cityId=1&userId=0&viewShopId=121859722&shopType=30&lat=0&lng=0&t=1553182399661&_=1553182399665&callback=Zepto1553182399658"
    response = requests.get(url,headers=headers)
    json_str = response.content.decode()
    ret = json.loads(json_str)
    with open("handwork.txt","w",encoding="utf-8") as f:
         f.write(json.dumps(ret,ensure_ascii=False,indent=2))

def get_write_hand():
    f = open("handwork.txt")
    hand_work  = []
    price_handwork = ['260','298','158','108','78','99','188','95','364','116']
    for i in range(10):
        str = f.readline()
        p = r'[\u4e00-\u9fa5]+\w+|[\u4e00-\u9fa5]+\s'
        pattern = re.compile(p)
        insert = pattern.findall(str)
        hand_work.append(insert[0])
    print("\n")
    print("打印找到的手工店")
    print(hand_work)
    return hand_work, price_handwork

def get_page(url):
    response = requests.get(url,data=query_string,headers=headers)
    response.encoding = response.apparent_encoding
    return response.text
    page = get_page(url)
    f = codecs.open('handwork_html.txt','w','utf-8')
    f.write(page)
 
