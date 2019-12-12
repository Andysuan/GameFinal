#抽奖 面向对象版本
import tkinter
from tkinter import *
import time
import threading
import numpy as np
import matplotlib.pyplot as plt

# 1.圓半徑
r = 200.0
# 2.圓心座標
a, b = (350., 350.)
# 參數方程

x1 = a + r * np.cos(np.pi/6)
y1 = b + r * np.sin(np.pi/6)
x2 = a + r * np.cos(np.pi/6*2)
y2 = b + r * np.sin(np.pi/6*2)
x3 = a + r * np.cos(np.pi/6*3)
y3 = b + r * np.sin(np.pi/6*3)
x4 = a + r * np.cos(np.pi/6*4)
y4 = b + r * np.sin(np.pi/6*4)
x5 = a + r * np.cos(np.pi/6*5)
y5 = b + r * np.sin(np.pi/6*5)
x6 = a + r * np.cos(np.pi/6*6)
y6 = b + r * np.sin(np.pi/6*6)
x7 = a + r * np.cos(np.pi/6*7)
y7 = b + r * np.sin(np.pi/6*7)
x8 = a + r * np.cos(np.pi/6*8)
y8 = b + r * np.sin(np.pi/6*8)
x9 = a + r * np.cos(np.pi/6*9)
y9 = b + r * np.sin(np.pi/6*9)
x10 = a + r * np.cos(np.pi/6*10)
y10 = b + r * np.sin(np.pi/6*10)
x11 = a + r * np.cos(np.pi/6*11)
y11 = b + r * np.sin(np.pi/6*11)
x12 = a + r * np.cos(np.pi/6*12)
y12 = b + r * np.sin(np.pi/6*12)


class choujiang:
    #初始化魔术方法
    def __init__(self):
        #准备好界面
        self.root = tkinter.Tk()
        self.root.title('lowB版转盘')
        #self.root.configure(background="black")
        self.root.minsize(100, 100)
        canvas_width = 10000
        canvas_height = 10000
        cvs = Canvas(self.root,
                    width=canvas_width,
                    height=canvas_height)
        cvs.pack()
        img = PhotoImage(file="C:\\Users\\user\\Desktop\\HI.gif")
        cvs.create_image(0.1,0.1, image=img)
        #x1, y1, x2, y2=140, 500, 590, 290
        #cvs.create_arc(x1, y1, x2, y2,fill='green')
        # 声明一个是否按下开始的变量
        self.isloop = False
        self.newloop = False
        #调用设置界面的方法
        self.setwindow()
        self.root.mainloop()



  #界面布局方法
    def setwindow(self):
        #开始停止按钮
        a = 45
        self.btn_start = tkinter.Button(self.root, text = 'start/stop',command = self.newtask)
        self.btn_start.place(x=350, y=350, width=a, height=a)

        self.btn1 = tkinter.Button(self.root, text='1', bg='red')
        self.btn1.place(x=x1, y=y1, width=a, height=a)

        self.btn2 = tkinter.Button(self.root, text='2', bg='white')
        self.btn2.place(x=x2, y=y2, width=a, height=a)

        self.btn3 = tkinter.Button(self.root, text='3', bg='white')
        self.btn3.place(x=x3, y=y3, width=a, height=a)

        self.btn4 = tkinter.Button(self.root, text='4', bg='white')
        self.btn4.place(x=x4, y=y4, width=a, height=a)

        self.btn5 = tkinter.Button(self.root, text='5', bg='white')
        self.btn5.place(x=x5, y=y5, width=a, height=a)

        self.btn6 = tkinter.Button(self.root, text='6', bg='white')
        self.btn6.place(x=x6, y=y6, width=a, height=a)

        self.btn7 = tkinter.Button(self.root, text='7', bg='white')
        self.btn7.place(x=x7, y=y7, width=a, height=a)

        self.btn8 = tkinter.Button(self.root, text='8', bg='white')
        self.btn8.place(x=x8, y=y8, width=a, height=a)

        self.btn9 = tkinter.Button(self.root, text='9', bg='white')
        self.btn9.place(x=x9, y=y9, width=a, height=a)

        self.btn10 = tkinter.Button(self.root, text='10', bg='white')
        self.btn10.place(x=x10, y=y10, width=a, height=a)

        self.btn11 = tkinter.Button(self.root, text='11', bg='white')
        self.btn11.place(x=x11, y=y11, width=a, height=a)

        self.btn12 = tkinter.Button(self.root, text='12', bg='white')
        self.btn12.place(x=x12, y=y12, width=a, height=a)

        # 将所有选项组成列表
        self.girlfrends = [self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,self.btn11,self.btn12]

    def rounds(self):
        # 判断是否开始循环
        if self.isloop == True:
            return

        # 初始化计数 变量
        i = 0
        # 死循环
        while True:
            if self.newloop == True:
                self.newloop = False
                return

            # 延时操作
            time.sleep(0.007)
            # 将所有的组件背景变为白色
            for x in self.girlfrends:
                x['bg'] = 'white'

            # 将当前数值对应的组件变色
            self.girlfrends[i]['bg'] = 'red'
            # 变量+1
            i += 1
            # 如果i大于最大索引直接归零
            if i >= len(self.girlfrends):
                i = 0

    # 建立一个新线程的函数
    def newtask(self):
        if self.isloop == False:
            # 建立线程
            t = threading.Thread(target = self.rounds)
            # 开启线程运行
            t.start()
            # 设置循环开始标志
            self.isloop = True
        elif self.isloop == True:
            self.isloop = False
            self.newloop = True

c = choujiang()