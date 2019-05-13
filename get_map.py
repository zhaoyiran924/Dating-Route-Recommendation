#-*- coding:utf-8 -*-
import requests
import json
from get_JinWei import return_JW


def get_distance(origin,destination):
    temp_url = "http://api.map.baidu.com/direction/v2/transit?origin={},{}&destination={},{}&ak=ClmC68V8M22O6lxjZSwdkW0kUYg1F7z3"

    # origin = input("输入起点: ")
    # destination = input("输入终点: ")


    lat_s,lng_s = return_JW(origin)
    lat_d,lng_d = return_JW(destination)

    url = temp_url.format(lat_s,lng_s,lat_d,lng_d)

    headers = {
    "Upgrade-Insecure-Requests" : "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"
    }


    response = requests.get(url, headers = headers)
    json_str = response.content.decode()


    distance = int(json.loads(json_str)['result']['routes'][0]['distance'])/ 1000


    return distance


def get_transport(origin,destination):
    temp_url = "http://api.map.baidu.com/direction/v2/transit?origin={},{}&destination={},{}&ak=ClmC68V8M22O6lxjZSwdkW0kUYg1F7z3"

    # origin = input("输入起点: ")
    # destination = input("输入终点: ")


    lat_s,lng_s = return_JW(origin)
    lat_d,lng_d = return_JW(destination)

    url = temp_url.format(lat_s,lng_s,lat_d,lng_d)

    headers = {
    "Upgrade-Insecure-Requests" : "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"
    }


    response = requests.get(url, headers = headers)
    json_str = response.content.decode()

    try:
        distance = int(json.loads(json_str)['result']['routes'][0]['distance'])/ 1000
    except:
        distance = 30

    print(distance)

    with open("Baidu_Map.txt","a",encoding="utf-8") as f:
        f.write("公交车乘车方案")
        f.write("\n")

    ret_arrive = json.loads(json_str)['result']['routes'][0]['arrive_time']
    with open("Baidu_Map.txt","a",encoding="utf-8") as f:
        f.write("到达时间："+str(ret_arrive))
        f.write("\n")

    ret_price = json.loads(json_str)['result']['routes'][0]['price']
    with open("Baidu_Map.txt","a",encoding="utf-8") as f:
        f.write("票价："+str(ret_price))
        f.write("\n")

    ret_step = json.loads(json_str)['result']['routes'][0]['steps']
    # print(type(ret_step))
    for i in range(len(ret_step)):
        ret_wri = ret_step[i][0]['instructions']
        with open("Baidu_Map.txt","a",encoding="utf-8") as f:
            f.write(str(ret_wri))
            f.write("\n")


    with open("Baidu_Map.txt","a",encoding="utf-8") as f:
        f.write("\n")
        f.write("出租车出行方案")
        f.write("\n")

    ret1 = json.loads(json_str)['result']['taxi']['detail']
    for i in range(len(ret1)):
        rett = ret1[i]
        with open("Baidu_Map.txt","a",encoding="utf-8") as f:
            print("success")
            for key,value in rett.items():
                # f.write(json.dumps(content,ensure_ascii=False))】

                f.write(str('{key}:{value}'.format(key=key, value=value)))

                f.write("\n")



if __name__ == '__main__':
    get_transport()
