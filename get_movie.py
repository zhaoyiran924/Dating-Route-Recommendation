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
    #frame.destroy()
    #theLable.pack_forget()
    choose =  i

# def show_movie(master,movie_name):
#     print("in show_movie")
#     root = master
#     # frame = frame
#     # frame.destroy()
#     # canvas = canvas
#     # canvas.pack_forget()
#
#     frame = Frame(root)
#     frame.pack()
#
#     img = Image.open('/Users/macbook/Desktop/5.jpg')  # 打开图片
#     photo = ImageTk.PhotoImage(img)
#     #photo.resize(900*400)
#     #theLable = Label(root,text="选择你想看的电影",justify=LEFT,image=photo,compound=CENTER,font=("楷体",30),fg="blue")
#
#     print("finish photo")
#     x = 0
#     width = 600
#
#     dx = 10
#
#     canvas = Canvas(root,width=900,height=600,bg="white")
#     canvas.pack()
#
#     canvas.create_text(x, 100, text="点击你想的电影，和你的TA",font=("楷体",30),tag="text")
#
#     canvas.create_image(200,200,anchor=NW,image=photo)
#
#     first_time = time.time()
#
#     while True:
#         if time.time()-first_time>5:
#             break;
#         canvas.after(100)
#
#         canvas.move("text",dx,0)
#
#         canvas.update()
#
#         if x<width:
#             x += dx
#
#         else:
#             x=0
#             canvas.delete("text")
#             canvas.create_text(x,100,"点击你想的电影，和你的TA",font=("楷体",30),tag="text")
#
#     print("finish show")


    # BButton = []
    # for i in range(10):
    #     BButton.append(" ")
    #     BButton[i] = Button(frame,text=str(movie_name[i]),command=lambda:next(i))
    #     #print(i)
    #     BButton[i].pack()
    #
    # root.mainloop()

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

    # t = Thread(target=show_movie,args=(master,movie_name))
    # t.start()
    # time.sleep(20)

    print("back")
    #time.sleep(15)
    #mainloop()
    #print(id[int(sequence)])
    print("back to follow")
    movie = []
    for i in range(10):
        movie.append(movie_name[i])
    print(movie)

    return choose,id,movie
    # for i in range(len(movie_name)):
    #     print(str(i+1)+"  "+movie_name[i])

    # BButton.append(" ")
    # BButton[10] = Button(frame,text=str(movie_name[i]),command=lambda:next(frame,theLable))
    # BButton[i].pack()
    #theLable.pack()



# if __name__=='__main__':
#     print(get_movie())
