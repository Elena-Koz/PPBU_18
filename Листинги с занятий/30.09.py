# import math
# from tkinter import *
#
#
# def add(n1, d1, n2, d2):
#     n = n1 * d2 + n2 * d1
#     d = d1 * d2
#     return n, d
#
#
# def sub(n1, d1, n2, d2):
#     n = n1 * d2 - n2 * d1
#     d = d1 * d2
#     return n, d
#
#
# def mult(n1, d1, n2, d2):
#     n = n1 * d2
#     d = d1 * n2
#     return n, d
#
#
# def div(n1, d1, n2, d2):
#     if d1 == 0 or d2 == 0:
#         raise ZeroDivisionError('na 0 delit nelzya')
#
#     n = n1 * d2
#     d = d1 * n2
#     return n, d
#
#
# def handler():
#     try:
#         n1 = int(num1.get())
#         d1 = int(den1.get())
#         n1 = int(n2.get())
#         d1 = int(d2.get())
#         operator = oper.get().strip()
#
#         if operator == "+":
#             result = add(n1, d1, n2, d2)
#
#         elif operator == "-":
#             result = sub(n1, d1, n2, d2)
#         elif operator == "-":
#             result = mult(n1, d1, n2, d2)
#         nod = math.gcd(result[0], result[1])
#         n = int(result[0] / nod)
#         d = int(result[1] / nod)
#         int_part = ' '
#         if d < n:
#             int_part = int(n // d)
#             n = int(n % d)
#         if n = 0:
#             n = ''
#             d = ''
#
#         if n == d:
#             n = ''
#             d = ''
#         int_part = '1'
#
#         n3.config(text=n)
#         d3.config(text=d)
#         res.int.config((text=int.part)
#
#     except Exeptions as err:
#         print(err)
#
#
#
#
#
# root = Tk()
# root.title("Calculator drobey")
# root.geometry("300x130+600+200")
#
# frame = Frame(root)
# frame.pack(pady=10)
# num1 = Entry(frame, width=2)
# num1.config(font=("arial", 16))
# num1.grid(row=0, column=0)
# Label(frame, text=chr(8212) * 3).grid(row=1, column=0)
# den1 = Entry(frame, width=2)
# den1.config(font=("arial", 16), justify="center")
# den1.grid(row=2, column=0)
#
# oper = Entry(frame, width=2)
# oper.config(font=("Arial", 15), justify="center")
# oper.grid(row=1, column=1)
#
# n = Entry(frame, width=2)
# n.config(font=("arial", 16))
# n.grid(row=0, column=2)
# Label(frame, text=chr(8212) * 3).grid(row=1, column=2)
# d = Entry(frame, width=2)
# d.config(font=("arial", 16), justify="center")
# d.grid(row=2, column=2)
#
# btn = Button(frame, text='=', command=handler)
# btn.config(font=("Arial", 15), justify="center", width=2)
# btn.grid(row=1, column=3, padx=5)
#
# res_int = Label(frame, text='   ', bg='light grey', width=2)
# res_int.config(font=("Arial", 20), justify="center")
# res_int.grid(row=1, column=4)
#
# n3 = Label(frame, width=2, bg='light grey')
# n3.config(font=("arial", 16))
# n3.grid(row=0, column=5)
# Label(frame, text=chr(8212) * 3).grid(row=1, column=5)
# d3 = Label(frame, width=2, bg='light grey')
# d3.config(font=("arial", 16), justify="center")
# d3.grid(row=2, column=5)
#
# mainloop()

# n= int(input('>'))
# print(n)
#
# try:
#     n = int(input('>'))
#     print(n)
# except ValueError:
#     print("please, enter a number")


from operator import abs
from pstats import add_func_stats
from pydoc import text
from tkinter import *
from unittest import result
import math


def add(num1, den1, num2, den2):
    n = num1 * den2 + num2 * den1
    d = den1 * den2
    return n, d


def sub(num1, den1, num2, den2):
    n = num1 * den2 - num2 * den1
    d = den1 * den2
    return n, d


def mul(num1, den1, num2, den2):
    n = num1 * num2
    d = den1 * den2
    return n, d


def div(num1, den1, num2, den2):
    if den1 == 0 or den2 == 0:
        raise ZeroDivisionError("Деление на ноль")
    n = num1 * den2
    d = num2 * den1
    return n, d


def handler():
    try:
        num1 = int(n1.get())
        den1 = int(d1.get())
        num2 = int(n2.get())
        den2 = int(d2.get())
        oper = o.get().strip()
        if den1 == 0 or den2 == 0:
            raise ZeroDivisionError("Деление на ноль")

        if oper == '+':
            result = add(num1, den1, num2, den2)
        elif oper == '-':
            result = sub(num1, den1, num2, den2)
        elif oper == '*':
            result = mul(num1, den1, num2, den2)
        elif oper == '*':
            result = div(num1, den1, num2, den2)


        nod = math.gcd(result[0], result[1])  ####импортировать без команды сверху (модуль математика)
        n = int(result[0] / nod)
        d = int(result[1] / nod)
        int_part = ''
        if abs(d) < abs(n):
            int_part = int(n // d)
            n = int(n % d)

        if n == 0:
            n = ''
            d = ''

        if n == d:
            n = ''
            d = ''
            int_part = '1'


        n3.config(text=n)
        d3.config(text=d)
        res_int.config(text=int_part)


    except Exception as err:
        pass


root = Tk()
root.title("Калькулятор дробей")
root.geometry("300x130+600+200")


frame = Frame(root) ###создаем в окне рут-область
frame.pack(pady=10) ###и размещаем его по центру

n1 = Entry(frame, width=2)
n1.config(font=("Arial", 15), justify="center")
n1.grid(row=0, column=0) ###менеждер разметки (сетка)

Label(frame, text=chr(8212)*3).grid(row=1, column=0)


d1 = Entry(frame, width=2)
d1.config(font=("Arial", 15), justify="center")
d1.grid(row=2, column=0)


o = Entry(frame, width=2)
o.config(font=("Arial", 15), justify="center")
o.grid(row=1, column=1, padx=5)


n2 = Entry(frame, width=2)
n2.config(font=("Arial", 15), justify="center")
n2.grid(row=0, column=2) ###менеждер разметки (сетка)

Label(frame, text=chr(8212)*3).grid(row=1, column=2)


d2 = Entry(frame, width=2) ### Entry окошко с надписью (не изменимо)
d2.config(font=("Arial", 15), justify="center")
d2.grid(row=2, column=2)

btn = Button(frame, text='=', command=handler) ##клавишу сокращать можно чтоб легче писать/ command=handler - результат выводит
btn.config(font=("Arial", 15), justify="center", width=3) ###шрифт в окне Arial - стиль шрифта
btn.grid(row=1, column=3, padx=5)


res_int = Label(frame,text="    ", bg='light grey', width=2) ###создали кнопку и закрасили ее в серый
res_int.config(font=("Arial", 22), justify="center")
res_int.grid(row=1, column=4)


n3 = Label(frame, width=2, bg='light grey')  #### Label окошко куда писать (изменяется пользователем - ввести цифру)
n3.config(font=("Arial", 15), justify="center")
n3.grid(row=0, column=5, padx=5) ###менеждер разметки (сетка)

Label(frame, text=chr(8212)*3).grid(row=1, column=2)


d3 = Label(frame, width=2, bg='light grey')
d3.config(font=("Arial", 15), justify="center")
d3.grid(row=2, column=5, padx=5) ####column колонка с права в лево





root.mainloop()