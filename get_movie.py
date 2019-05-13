#This code is a crawler to get movies on www.maoyan.com

# -*- coding: utf-8 -*-
import requests
import json
import sys
import io
import codecs
import random
from urllib import request
from get_time import get_time
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import time
from threading import Thread
import time

id = []
choose = 0

def next(i):
    choose =  i

def get_movie(master):
    #get movieid and movies on the line
    url = "http://m.maoyan.com/ajax/movieOnInfoList?token="
    headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    json_str = response.content.decode()
    ret = json.loads(json_str)["movieIds"]
    number = []
    for element in ret:
        number.append(element)
    new_url = "http://m.maoyan.com/ajax/movie?forceUpdate=1553052387129"
    new_headers = {
    "Referer": "http://m.maoyan.com/cinema/movie/1216383?$from=imeituan",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"
    }
    query_string = {"forceUpdate":"1553052387129"}
    new_response = requests.get(new_url,data=query_string,headers=new_headers)
    html_str = response.content.decode()
    dict_ret = json.loads(html_str)['movieList']
    movie_name = []
    with io.open("movie.txt","w",encoding="utf-8") as f:
        for element in dict_ret:
            movie_name.append(element['nm'])
            element = element['nm']+"   "+str(element['sc'])+"   "+ element['star']+ "   "+element['showInfo']
            f.write(u'{}\n'.format(json.dumps(element,ensure_ascii=False)))
    master = master
    for element in dict_ret:
        id.append(element['id'])
    print("\n")
    print("打印找到的电影：")
    print("back")
    print("back to follow")
    movie = []
    for i in range(10):
        movie.append(movie_name[i])
    print(movie)
    return choose,id,movie
