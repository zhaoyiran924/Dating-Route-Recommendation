import requests
import json
import random
import re


def get_Dazhong():
    url = "https://mapi.dianping.com/searchshop.json?start={}&categoryId=10&parentCategoryId=10&locateCityid=0&limit=20&sortId=0&cityId=1&regionId=0&maptype=0&sortid=2"
    headers = {
        "Referer": "https://m.dianping.com/shanghai/ch10/",
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"
         }
    total = 200
    num = 0

    all_name = []

    f = open("Temp_DaZhong.txt","w",encoding="utf-8")
    #f = open("dadoubi.txt","w",encoding="utf-8")
    while num<total:
        temp_url = url.format(num)
        response = requests.get(url, headers=headers)
        json_str = response.content.decode()

        # print(json_str)

        ret1 = json.loads(json_str)['list']
        #f.write(json.dumps(ret1,ensure_ascii=False))

        for content in ret1:
            content_in ="上海市"+content['regionName'] + content['name']+"饭店" +"  "+ content['categoryName'] + "  " + content['priceText']
            #f.write(json.dumps(content_in,ensure_ascii=False))
            f.write(json.dumps(content_in,ensure_ascii=False))
            all_name.append(json.dumps(content_in,ensure_ascii=False))
            # f.write("\n")
            # f.write(json.dumps(content['dishtags'],ensure_ascii=False))
            # f.write("\n")
            f.write("\n")

        print("已经找到"+str(20+num)+"店面符合要求")
        num += 20
    return total, all_name

def get_Dazhong_ten(total, all_name):
    get_Dazhong = []
    price_Dazhong = []
    number = random.sample(range(0,total-1),10)
    #print(number)
    for i in range(10):
        need_insert = all_name[number[i]]
        p = r'[\u4e00-\u9fa5]+\w+|[\u4e00-\u9fa5]+\s'
        pp = r'\d+'
        pattern = re.compile(p)
        ppattern = re.compile(pp)
        insert = pattern.findall(need_insert)
        insertt = ppattern.findall(need_insert)
        get_Dazhong.append(insert[0]+insert[1])
        try:
            price_Dazhong.append(insertt[0])
        except:
            price_Dazhong.append('302')
    f = open("DaZhong.txt","w",encoding="utf-8")
    for element in get_Dazhong:
        f.write(str(element))
        f.write("\n")

    #print(get_Dazhong)
    return get_Dazhong, price_Dazhong


def get_resturant():
    total, all_name = get_Dazhong()
    Ten_Dazhong, price_Dazhong = get_Dazhong_ten(total, all_name)
    return Ten_Dazhong, price_Dazhong
