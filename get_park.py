#This code is a crawler to get park on www.meituan.com

# -*- coding: utf-8 -*-
import requests
import json
import io
import os
import re
import random
import codecs

def get_park():
    url = "https://i.meituan.com/notel/proxy?requestUrl=http%3A%2F%2Fapimobile.vip.sankuai.com%2Fgroup%2Fv2%2Farea%2Flist%3Fuuid%3D618C49BDF412F34E95C59B7AD8E819474772EAE2E66CBA65F99446E128F32FB5%26cityId%3D10"
    headers = {
    "Accept": "application/json",
    "X-Requested-With" : "XMLHttpRequest",
    "Referer": "https://i.meituan.com/trip/lvyou/triplist/poi/?stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F195",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    }
    query_string = {
    "requestUrl" : "http://apimobile.vip.sankuai.com/group/v2/area/list?uuid=618C49BDF412F34E95C59B7AD8E819474772EAE2E66CBA65F99446E128F32FB5&cityId=10"
    }
    response = requests.get(url,data=query_string,headers=headers)
    json_str = response.content.decode()
    ret1 = json.loads(json_str)['data']['landmarks']
    park_all = []
    for element in ret1:
        if element['type']==3:
            element_s = "上海市" + element['name']
            park = json.dumps(element_s,ensure_ascii=False,indent=2)
            park_all.append(park)
    all = len(park_all)
    number = random.sample(range(0,all-1),10)
    park = []
    with open("park_select.txt","w",encoding="utf-8") as f:
        for i in number:
            park.append(park_all[i])
            f.write(park_all[i])
            f.write("\n")
    print("\n")
    print("开始寻找公园")
    print(park)
    price_park = []
    for i in range(10):
        price_park.append('0')
    return park, price_park
