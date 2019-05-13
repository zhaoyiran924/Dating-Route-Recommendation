import numpy as np
from get_Dazhong import get_resturant
from get_movie import get_movie
from get_park import get_park
from get_hotel import get_hotel
from get_handwork import get_write_hand
import requests
import json
import re
from get_time import get_time
from calculate import floyd
import time
import random
import io

# from get_JinWei import return_JW
# from get_map import get_distance

#设置不可以连通的矩阵距离
distant = 100
all_level = 5

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

def xjbchu():
    movie = []
    price = []
    for i in range(10):
        movie.append("不选")
        price.append('0')
    return movie, price

def follow(choose,master,id):
    if choose!=0:
        sequence = choose
    else:
        sequence = 1

    temp_url = "http://m.maoyan.com/ajax/filterCinemas?movieId={}&day={}"
    headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"
    }
    now_time = get_time()
    url = temp_url.format(id[int(sequence)-1],now_time)

    # query_string = {
    # "movieId": str(id[sequence]),
    # "day": "2019-03-21"
    # }

    price_movie = []
    for i in range(10):
        price = int(random.uniform(40,60))
        price_movie.append(price)


    new_response = requests.get(url,headers=headers)
    json_str = new_response.content.decode()

    ret = json.loads(json_str)['brand']['subItems']

    cinema = []
    total = 0

    with io.open("movie.txt","a",encoding="utf-8") as f:
        for element in ret:
            element_s = "上海"+element['name'] +  "  " + str(element['count'])
            f.write(u'{}\n'.format(json.dumps(element_s,ensure_ascii=False)))
            if(total<10):
                element_in = "上海"+element['name']
                cinema.append(json.dumps(element_in,ensure_ascii=False))
                total = total + 1

    print("finish follow")


    return cinema,price_movie,master



#这里根据所有得到的距离生成需要的矩阵以及距离保存为.mat文件
#保存的顺序为[get_Dazhong,get_movie,get_park,get_handwork,get_hotel]
def get_allmatrix(order,master):
    Dazhong, price_Dazhong = get_resturant()
    flag = False
    for element in order:
        if int(element)==1:
            flag = True
    if flag:
        choose, id, movie_we = get_movie(master)
        movie, price_movie,master = follow(choose,master,id)
        print("back flag")
    else:
        movie,price_movie = xjbchu()
    print(movie)
    park,price_park = get_park()
    handwork, price_handwork = get_write_hand()
    hotel, price_hotel  = get_hotel()

    Dazhong_JW = []
    movie_JW = []
    park_JW = []
    handwork_JW = []
    hotel_JW = []
    all_matrix = np.zeros((all_level*10,all_level*10))
    price_raw = price_Dazhong+price_movie+price_park+price_handwork+price_hotel
    for i in range(10):
        #print(Dazhong[i])
        Dazhong_JW.append(return_JW(Dazhong[i]))
        try:
            movie_JW.append(return_JW(movie[i]))
        except:
            print("no movie")
        #print(park[i])
        park_JW.append(return_JW(park[i]))
        handwork_JW.append(return_JW(handwork[i]))
        hotel_JW.append(return_JW(hotel[i]))
        #print(Dazhong[i]+movie[i]+park[i]+handwork[i]+hotel[i]+'finish')

    raw = []
    column = []
    raw_JW = []
    column_JW = []
    raw = Dazhong+movie+park+handwork+hotel
    column = Dazhong+movie+park+handwork+hotel
    raw_JW = Dazhong_JW + movie_JW + park_JW + handwork_JW + hotel_JW
    column_JW = Dazhong_JW + movie_JW + park_JW + handwork_JW + hotel_JW
    #print(len(raw_JW))
    #print(raw)
    for i in range(len(raw)):
        for j in range(len(column)):
            all_matrix[i][j] = 100

    # for i in range(len(raw)):
    #     for j in range(len(column)):
    #         #print(i,j)
    #         if(i != j and raw[i]!=raw[j]):
    #             #print(raw[i],column[j])
    #             try:
    #                 all_matrix[i][j] = get_distance(raw[i],raw[j])
    #             #print(all_matrix[i][j])
    #             except:
    #                 all_matrix[i][j] = 100
    #                 print("fail")
    #     print(raw[i]+"finish")
    #
    # print(all_matrix)
    # fp = open("metrix.txt","w+")
    # for item in all_matrix:
    #     fp.write(str(item)+"\n")
    # fp.close()
    return all_matrix,raw,price_raw,movie,movie_we



#这里根据生成的所有矩阵和提出的需求自动生成计算矩阵
#matrix是60*60，order是数组，保存了用户选择的顺序
#metrix的保存顺序行为起点，列为终点
def get_matrix(all_matrix,order):
    size = len(order)
    matrix = np.zeros((all_level*10, all_level*10))
    #print(size)
    for i in range(all_level*10):
        for j in range(all_level*10):
            matrix[i][j] = distant
    #matrix也是全size的
    for k in range(size-1):
        source = int(order[k])*10
        destination = int(order[k+1])*10
        #print(source,destination)
        for number in range(10):
            i = source + number
            for number_next in range(10):
                j = destination + number_next
                matrix[i][j] = all_matrix[i][j]
                #print(i,j,matrix[i][j])


    fp = open("choose_metrix.txt","w+")
    for item in matrix:
        fp.write(str(item)+"\n")
    fp.close()

    return matrix



'''
上一阶段导入的矩阵是所有的距离，在规定了顺序之后自动生成可以到的和不可到的之间的不同方式
这里首先根据选择，自动生成矩阵
'''

def all_in_all(order,root):
    print("约会项目")
    print("0-吃饭  1-电影  2-公园  3-手工DIY 4-酒店")
    #input_order = input("请输入想要的约会项目顺序")
    #input_xjb = input("请输入约会预算")
    #input_xjb2 = input("请输入约会区域，比如(徐汇区)")
    # p = r'\d'
    # pattern = re.compile(p)
    # order = pattern.findall(input_order)
    root = root

    metrix,raw,price_raw,movie,movie_we = get_allmatrix(order,root)
    f = open("metrix.txt")
    all_matrix = f.read()
    p = r'(\d+)(\.\d+)?'
    pattern = re.compile(p)
    all_matrix = pattern.findall(all_matrix)
    after_metrix = []
    for element in all_matrix:
        after_metrix.append(float(element[0]+element[1]))
    after_metrix = np.array(after_metrix)
    after_metrix = after_metrix.reshape((50,50))
    #至上一步已经得到一个50*50的矩阵
    metrix = get_matrix(after_metrix,order)
    floyd(metrix,order,raw,price_raw,root,movie,movie_we)
