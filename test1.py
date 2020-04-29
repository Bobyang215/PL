# # # #-*- coding: utf-8 -*-
# # #
# # # # L = [
# # # #     ['Apple', 'Google', 'Microsoft'],
# # # #     ['Java', 'Python', 'Ruby', 'PHP'],
# # # #     ['Adam', 'Bart', 'Lisa']
# # # # ]
# # # #
# # # # print (L[0][0],L[1][1],L[2][2])
# # #
# # # # age = int(input('birthday:'))
# # # # if age>2000:
# # # #     print('Age is ',age-2000)
# # # #     print('00后')
# # # # else:
# # # #     print('Age is ', 2019-age)
# # # #     print('00前')
# # #
# # # # heigh=float(input('Heigh:'))
# # # # weigh=float(input('Weigh:'))
# # # # IBM=weigh/(heigh*heigh)
# # # # if IBM<18.5:
# # # #     print('过轻  %0.2f'%IBM)
# # # # elif 18.5<= IBM <25:
# # #
# # # #     print('正常 %0.2f'%IBM)
# # # # elif 25<= IBM <28:
# # # #     print('超重 %0.2f'%IBM)
# # # # elif 28<= IBM <32:
# # # #     print('肥胖 %0.2f'%IBM)
# # # # else:
# # # #     print('过度肥胖 %0.2f'%IBM)
# # #
# # # # sum=0
# # # # n=99
# # # # while n>0:
# # # #     sum=sum+n
# # # #     n=n-2
# # # # print(sum)
# # #
# # # # sum=0
# # # # for n in list(range(101)):
# # # #     if n%2!=0:
# # # #         sum=sum+n
# # # # print(sum)
# # #
# # # # L = ['Bart', 'Lisa', 'Adam']
# # # #
# # # # for x in L:
# # # #     print("Hello: %s!\n" %x)
# # #
# # # # n1=255
# # # # n2=1000
# # # # print(hex(n1))
# # # # print(hex(n2))
# # # #
# # # #
# # #
# # # #
# # # # def my_abs(x):
# # # #     if x>=0:
# # # #         return x
# # # #     else:
# # # #         return -x
# # # # import math
# # # #
# # # # def quadratic(a, b, c,):
# # # #     if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
# # # #         raise TypeError('bad operand type')
# # # #     elif(b**2-4*a*c)<0:
# # # #         print('wujie')
# # # #     else:
# # # #         x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
# # # #         x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
# # # #         return x1,x2
# # # #
# # # # print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# # # # print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
# # # #
# # # # if quadratic(2, 3, 1) != (-0.5, -1.0):
# # # #     print('测试失败')
# # # # elif quadratic(1, 3, -4) != (1.0, -4.0):
# # # #     print('测试失败')
# # # # else:
# # # #     print('测试成功')
# # # #
# # # # s1=int(input('a= '))
# # # # s2=int(input('b= '))
# # # # s3=int(input('c= '))
# # # # print('quadratic(2, 3, 1) =', quadratic(s1, s2, s3))
# # #
# # # # def calc(*numbers):
# # # #     sum=0
# # # #     for n in numbers:
# # # #         sum=sum+n*n
# # # #     return sum
# # # # # print('calc()= ',calc([1,2,3]))
# # # # # print('calc()= ',calc((1,2,3)))
# # # # print('calc()= ',calc(1,2,3))
# # # # tuple1=[1,2,3]
# # # # list1=(1,2,3)
# # # # print('calc()= ',calc(*tuple1))
# # # # print('calc()= ',calc(*list1))
# # #
# # #
# # # def regestire(name,gender,age=6,city='chengdu'):
# # #     print('name:',name)
# # #     print('gender:',gender)
# # #     print('age:',age)
# # #     print('city:',city)
# # #
# # #
# # # def add_end(L=None):
# # #     if L is None:
# # #         L=[]
# # #     L.append('END')
# # #     return L
# # #
# # # def product(*numbers):
# # #     if numbers is None or len(numbers)<=0:
# # #         print('参数为空')
# # #     sum=1
# # #     for x in numbers:
# # #         sum=sum*x
# # #     return sum
# # #
# # #
# # # def move(n,a,b,c):
# # #     if n==1:
# # #         print(a,'-->',c)
# # #     else:
# # #         move(n-1,a,c,b)
# # #         move(1,a,b,c)
# # #         move(n-1,b,a,c)
# # #
# # #
# # # def trim(s):
# # #     while s[0:1]==' ':
# # #         s=s[1:]
# # #     while s[:-1]==' ':
# # #         s=s[:-2]
# # #     return s
# # #
# # #
# # # if trim('hello ')!='hello':
# # #     print('failed!')
# # # elif trim(' hello~!')!='hello~!':
# # #     print('failed!')
# # # elif trim(' hello ')!='hello':
# # #     print('failed!')
# # # elif trim('   hello  ')!='hello':
# # #     print('failed!')
# # # elif trim(' hello world ')!='hello world':
# # #     print('failed!')
# # # elif trim(' ')!='':
# # #     print('failed!')
# # # else:
# # #     print('successful!')
# # #
# # #
# # #
# # # def triangles():
# # #     L = [1]
# # #     while True:
# # #         yield L
# # #         L = [1] + [L[k] + L[k + 1] for k in range(len(L) - 1)] + [1]
# # #
# # # n = 0
# # # results = []
# # # for t in triangles():
# # #     print(t)
# # #     results.append(t)
# # #     n = n + 1
# # #     if n == 10:
# # #         break
# # # if results == [
# # #     [1],
# # #     [1, 1],
# # #     [1, 2, 1],
# # #     [1, 3, 3, 1],
# # #     [1, 4, 6, 4, 1],
# # #     [1, 5, 10, 10, 5, 1],
# # #     [1, 6, 15, 20, 15, 6, 1],
# # #     [1, 7, 21, 35, 35, 21, 7, 1],
# # #     [1, 8, 28, 56, 70, 56, 28, 8, 1],
# # #     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# # # ]:
# # #     print('测试通过!')
# # # else:
# # #     print('测试失败!')
# # #
# # #
# # # def _odd_iter():
# # #     n=1
# # #     while True:
# # #         n=n+2
# # #         yield n
# # #
# # # def _not_divisible(n):
# # #     return lambda x: x % n > 0
# # #
# # # def primes():
# # #     yield 2
# # #     it = _odd_iter()
# # #     while True:
# # #         n=next(it)
# # #         yield n
# # #         it =filter(_not_divisible(n),it)
# # #
# # #
# # # for n in primes():
# # #     if n<1000:
# # #         print(n)
# # #     else:
# # #         break
# # #
# # #
# # # def is_palindrome(n):
# # #     return str(n)==str(n)[::-1]
# # #
# # #
# # #
# # # def by_name(t):
# # #     return t[0]
# # #
# # #
# # # def by_score(t):
# # #     return -t[1]
# # #
# # # L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# # #
# # # L2 = sorted(L, key=by_name)
# # # L3 = sorted(L, key=by_score)
# # # print(L2)
# # # print(L3)
# #
# # from tkinter import *
# # import tkinter.messagebox as  messagebox
# #
# # class Application(Frame):
# #     def __init__(self,master=None):
# #         Frame.__init__(self,master)
# #         self.pack()
# #         self.createWidgets()
# #
# #     def createWidgets(self):
# #         self.nameInput = Entry(self)
# #         self.nameInput.pack()
# #         self.alertButton =Button(self,text='Hello', command=self.hello)
# #         self.alertButton.pack()
# #
# #     def hello(self):
# #         name=self.nameInput.get() or 'world'
# #         messagebox.showinfo('Message', 'Hello, %s' % name)
# #
# # app = Application()
# # #设置窗口标题：
# # app.master.title('Hello world')
# # #主消息循环
# # app.mainloop()
#
# from turtle import *
#
# def drawStar(x,y):
#     pu()
#     goto(x,y)
#     pd()
#     #set heading:0
#     seth(0)
#     for i in range(5):
#         pencolor('red')
#         fd(40)
#         rt(144)
#
#
#
# def cycDraw():
#
#     width(4)
#     pencolor('yellow')
#     forward(200)
#     right(90)
#
#     pencolor('red')
#     fd(100)
#     right(90)
#
#     pencolor('green')
#     fd(100)
#     right(90)
#
#     pencolor('blue')
#     fd(100)
#     right(90)
#
# for x in range(0,250,50):
#         drawStar(x,0)
#         cycDraw()
#
#
#
# done()


from turtle import *

colormode(255)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)

speed("fastest")

draw_tree(l, 4)

done()

import logging

def foo(s):
    return 10/ int(s)

def bar(s):
    return  foo(2)*2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
        print("Error", e)


def fact(n):
    if n<1:
        raise ValueError
    if n==1:
        return 1
    return n*fact(n-1)


from io import StringIO
f=StringIO('Hello\nhi!\nGoogbye!')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())

from io import BytesIO
from io import StringIO
f = BytesIO()
f.write('中文'.encode('utf-8'))

print(f.getvalue())



import PIL from Image, ImageFilter
im=Image.open('/Users/yangbo/Desktop/孕装照/0D1A9086.jpg')
im2=im.filter(ImageFilter.BLUR)
im2.save('/Users/yangbo/Desktop/1.jpg','jpg')


import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))