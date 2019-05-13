import numpy as np
#from pylab import *
import random
from tkinter import *
from get_map import get_distance
from PIL import Image, ImageTk
import re
from get_map import get_transport
from threading import Thread
import time

# def change_format(P, name_string,start):
#     #choose由一个个路线构成，每个路线都是由一个个字符串组成
#     choose = [[]]
#     lenth = len(P)
#     for i in range(length):
#         path = []
#         for j in range(i+1, length):
#             temp = P[i][j]

def get_handwork_name(temp_number1):
    f = open("handwork.txt")
    for i in range(temp_number1):
        str = f.readline()

    p = r'[\u4e00-\u9fa5]+\w+|[\u4e00-\u9fa5]+\s'
    pattern = re.compile(p)
    find = pattern.findall(str)
    #print(find[1])
    return find[1]

def get_room(temp_number1):
    f = open("address_array.txt")
    for i in range(temp_number1):
        str = f.readline()

    p = r'[\u4e00-\u9fa5]+\w+|[\u4e00-\u9fa5]+|\w+[\u4e00-\u9fa5]+\s'
    pattern = re.compile(p)
    find = pattern.findall(str)
    #print(find[0])
    return find[0]

class MyThread(Thread):
    def __init__(self, name,root,movie_name,route_new):
        super().__init__()
        self.name = name
        print("in show_movie")
        self.movie_name = movie_name
        self.route_new = route_new
        # frame = frame
        # frame.destroy()
        # canvas = canvas
        # canvas.pack_forget()
        self.root = root
        self.frame = Frame(root)
        self.frame.pack()

    def run(self):
        img = Image.open('5.jpg')  # 打开图片
        photo = ImageTk.PhotoImage(img)
        #photo.resize(900*400)
        #theLable = Label(root,text="选择你想看的电影",justify=LEFT,image=photo,compound=CENTER,font=("楷体",30),fg="blue")

        print("finish photo")
        x = 0
        width = 600

        dx = 10

        self.canvas = Canvas(self.root,width=900,height=600,bg="pink")
        self.canvas.pack()

        self.canvas.create_text(x, 700, text="点击你想的电影，和你的TA",font=("楷体",20),tag="text")

        self.canvas.create_image(100,100,anchor=NW,image=photo)

        first_time = time.time()

        while True:
            self.canvas.after(100)
            if time.time()-first_time>5:
                break;

            self.canvas.move("text",dx,0)

            self.canvas.update()

            if x<width:
                x += dx

            else:
                x=0
                self.canvas.delete("text")
                self.canvas.create_text(x,700,"点击你想的电影，和你的TA",font=("楷体",20),tag="text")

        print("finish show")

        BButton = []
        for i in range(10):
            BButton.append(" ")
            BButton[i] = Button(self.frame,text=str(self.movie_name[i]),command=lambda:self.play)
            #print(i)
            BButton[i].pack()

        Button11 = Button(self.frame,text="确定",command=self.change)
        Button11.pack()
        #mainloop()

    def change(self,):
        print("in change")
        self.frame.destroy()
        self.canvas.pack_forget()
        face(self.root,self.route_new)

    def play(self,):
        print("in self")
        return


class face():
    def __init__(self,master,route_new):
        print("in face")
        self.master = master
        self.route_new = route_new
        frame = Frame(self.master)
        frame.pack()
        img = Image.open('6.jpg')  # 打开图片
        photo = ImageTk.PhotoImage(img)
        theLable = Label(frame,text=self.route_new,justify=LEFT,image=photo,compound=CENTER,font=("楷体",23),fg="blue")
        theLable.pack()
        mainloop()

class floyd():
    def __init__(self,adjust_matrix,order,raw,price_raw,root,movie,movie_we):
        self.adjust_matrix = adjust_matrix
        self.order = order
        self.raw = raw
        self.price_raw = price_raw
        self.master = root
        self.movie =movie
        self.movie_we = movie_we
        self.ffloyd()


    def ffloyd(self,):
        movie_name = self.movie_we
        print("开始寻找最短路径")
        d = np.array(self.adjust_matrix)
        inf = int(1e9)
        n = len(self.adjust_matrix)
        for i in range(0, n):
            for j in range(0,n):
                d[i][j] = inf if d[i][j] == 0 else d[i][j]
        for i in range(0,n): d[i][i] = 0

        for k in range(0,n):
            for i in range(0,n):
                for j in range(0,n):
                    d[i][j] = min(d[i][j],d[i][k]+d[k][j])

        size = len(self.order)

        route = []
        name = []
        price = []
        addr = []
        #price分别在"Temp_Dazhong.txt" "movie.txt" "free" "handwork.txt" "address_array.txt"
        for i in range(size-1):
            temp_number1 = int(random.uniform(1,9))
            temp_number2 = int(random.uniform(1,9))
            first = int(self.order[i])*10 + temp_number1
            second = int(self.order[i+1])*10 + temp_number2
            try:
                addr.append(self.raw[first])
                if int(self.order[i])==3:
                    distance = get_distance(self.raw[first],self.raw[second])
                    name = get_handwork_name(temp_number1)
                    route.append(name)
                    price.append(price_self.raw[first])
                else :
                    if int(self.order[i]==4):
                        distance = get_distance(self.raw[first],self.raw[second])
                        name = get_room(temp_number1)
                        route.append(name)
                        price.append(self.price_raw[first])
                    else:
                        distance = get_distance(self.raw[first],self.raw[second])
                        route.append(self.raw[first])
                        price.append(self.price_raw[first])

            except:
                addr.append(self.raw[first+1])
                if int(self.order[i])==3:
                    name = get_handwork_name(temp_number1+1)
                    route.append(name)
                    price.append(self.price_raw[first+1])
                else:
                    if int(self.order[i])==4:
                        name = get_rom(temp_number1+1)
                        route.append(name)
                        price.append(self.price_raw[first+1])
                    else:
                        route.append(self.raw[first+1])
                        price.append(self.price_raw[first+1])

        addr.append(self.raw[second])
        if int(self.order[i+1])==3:
            name = get_handwork_name(temp_number2)
            route.append(name)
            price.append(self.price_raw[second])
        elif int(self.order[i+1])==4:
            name = get_room(temp_number2)
            route.append(name)
            price.append(self.price_raw[second])

        else:
            route.append(self.raw[second])
            price.append(self.price_raw[second])

        print("打印找到的约会路线")
        print(route)

        route_new = ""

        for i in range(len(route)):
            if(i!=0):
                route_new = route_new +"->"+ str(route[i])
            else:
                route_new = route_new + str(route[i])
        print("打印各项目花费")
        print(price)

        for i in range(len(route)-1):
            print(route[i],route[i+1])
            try:
                get_transport(addr[i],addr[i+1])
            except:
                get_transport(addr[i],addr[i+1])

        flag = False
        for i in range(len(self.order)):
            if int(self.order[i]==1):
                flag = True

        if flag==True:
            t = MyThread('show_result',self.master,movie_name,route_new)
            print(route_new)
            print("进程创建完毕")
            t.start()
            #time.sleep(5)
        else:
            #self.route_new = route_new
            frame = Frame(self.master)
            frame.pack()
            img = Image.open('/Users/macbook/Desktop/6.jpg')  # 打开图片
            photo = ImageTk.PhotoImage(img)
            theLable = Label(frame,text=self.route_new,justify=LEFT,image=photo,compound=CENTER,font=("楷体",23),fg="pink")
            theLable.pack()
            mainloop()


        #return route, price



# if __name__=='__main__':
#     print(get_handwork_name(5))



#这里已经找到最好路径，直接打印出来。在选择中，权重的设置：距离，其他选择在爬虫中选择
#选择报价，并且将其排列在范围中。每个选择7-10个选择放入矩阵中

# def get_answer(metrix):
#     name_string = get_name()
#     #这里还要给一些接口用爬虫找到的地址填满name_string
#     floyd(data)
