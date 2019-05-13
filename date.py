# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image, ImageTk
from get_metrix import all_in_all
# from tkinter import ttk
# from tkinter import messagebox
import time


class basedesk():
    def __init__(self,master):
        self.root = master
        self.root.geometry('900x600')
        initface(self.root)


#frame1
class initface():
    def __init__(self,master):
        self.master = master
        self.frame1 = Frame(self.master)
        self.frame1.pack()
        print("in start")
        img = Image.open('1.jpg')  # 打开图片
        photo = ImageTk.PhotoImage(img)
        #photo = photo.resize((900,400),Image.ANTIALIAS)
        #theLable = Label(self.root,image=photo)
        # self.theLable = Label(self.master,text="陪你走遍上海每个角落",justify=LEFT,image=photo,compound=CENTER,font=("楷体",30),fg="white")
        # self.theLable.pack(side=LEFT)
        x = 0
        width = 600

        dx = 10

        self.canvas = Canvas(self.master,width=900,height=600,bg="pink")
        self.canvas.pack()

        self.canvas.create_text(x, 100, text="陪你走遍上海每个角落",font=("楷体",30),tag="text")

        self.canvas.create_image(100,200,anchor=NW,image=photo)

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
                self.canvas.create_text(x,50,"陪你走遍上海每个角落",tag="text")




        #frame1 实现开始界面
        #开始运行get_materix准备所有的数据但是需要准备
        theButton = Button(self.frame1,text="开始我的约会规划",command=self.change)
        theButton.pack()
        mainloop()


    def change(self,):
        self.frame1.destroy()
        self.canvas.pack_forget()
        face1(self.master)


#frame2
class face1():
    def __init__(self,master):
        self.order = []
        self.master = master
        self.frame2 = Frame(self.master)
        self.frame2.pack()
        print("开始进行项目选择")
        img = Image.open('2.jpg')  # 打开图片
        photo = ImageTk.PhotoImage(img)
        #photo.resize(900*400)
        #self.theLable = Label(self.master,text="选择你和TA最想做的事吧，注意顺序哦",justify=LEFT,image=photo,compound=CENTER,font=("楷体",30),fg="blue")

        x = 0
        width = 600

        dx = 10

        self.canvas = Canvas(self.master,width=900,height=600,bg="pink")
        self.canvas.pack()

        self.canvas.create_text(x, 100, text="选择你和TA最想做的事吧，注意顺序哦",font=("楷体",30),tag="text")

        self.canvas.create_image(0,200,anchor=NW,image=photo)

        first_time = time.time()

        while True:
            if time.time()-first_time>5:
                break;
            self.canvas.after(100)

            self.canvas.move("text",dx,0)

            self.canvas.update()

            if x<width:
                x += dx

            else:
                x=0
                self.canvas.delete("text")
                self.canvas.create_text(x,50,"选择你和TA最想做的事吧，注意顺序哦",tag="text")


        Button1 = Button(self.frame2,text="美食",command=lambda:self.count(0))
        Button1.pack()
        Button2 = Button(self.frame2,text="电影",command=lambda:self.count(1))
        Button2.pack()
        Button3 = Button(self.frame2,text="公园",command=lambda:self.count(2))
        Button3.pack()
        Button4 = Button(self.frame2,text="手工DIY",command=lambda:self.count(3))
        Button4.pack()
        Button5 = Button(self.frame2,text="酒店",command=lambda:self.count(4))
        Button5.pack()
        Button6 = Button(self.frame2,text="确定",command=self.show)
        Button6.pack()
        #self.theLable.pack()
        mainloop()

    def count(self,number):
        self.order.append(number)
        return

    def show(self,):
        print(self.order)
        self.frame2.destroy()
        self.canvas.pack_forget()
        print("destroy")
        all_in_all(self.order,self.master)



if __name__=='__main__':
    root = Tk()
    root.title = ("上海情侣约会推荐")
    basedesk(root)
    root.mainloop()
