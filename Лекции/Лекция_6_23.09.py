# def is_eval(n: int) -> bool:
#     """Определяет четность числа
#     is_eval(2) -> True
#     is_eval(3) -> False
#     """
#     return n % 2 == 0
#
#
# # res = is_eval(4)
# # print(res)
#
#
# def choice_eval(x: int, y: int) -> None:
#     '''Выбирает четные числа из последовательности'''
#     for i in range(x, y + 1):
#         if is_eval(i):
#             print(i, end=' ')


# choice_eval(100, 140)

# for n in range(100,200):
#     for i in range (2, n):
#         if n % 1 == 0:
#             break
#     else:
#         print(n, end=' ')

# def num2(n: int) -> None:
#     if n > 1:
#         num2(n - 1)
#     print(n)
#
#
# def num1(n: int) -> None:
#     if n > 1:
#         num2(n - 1)
#     print(n)
#
#
# def num(n: int) -> None:
#     if n > 1:
#         num1(n - 1)
#     print(n)

# def num(x, n: int) -> None:
#     if n > x:
#         num(x, n - 1)
#     print(n)
# num(4, 8)

# def name(nm):
#
#     def surname(snm):
#         global cnt
#         cnt +=1
#         print(cnt, nm, snm)
#     return surname
# cnt = 0
# sur = name ('Mary')
# sur("TTT")
# sur("LLL")
# sur("KKK")
#
#
# pass

# def summ(a, y):
#     global x
#     z = 12
#     x += 1
#     print('x =', x, 'y =',y, 'z =',z)
#     return a
#
# z = 1000
# x = 5000
# res = summ(19, 20)
# print(res)
# print('X = ', x, 'Z =', z)

'''Ткинтер'''
# from tkinter import *
#
# def answer(event):
#     answ = num.get().strip()
#     result.config(text = answ)
#
# root = Tk()
# root.title("Start")
# root.geometry("300x300")
#
# prompt = Label(text = 'Введите значение')
# prompt.pack()

num = Entry(width = 5, font = 'Arial 15')
num.pack()

result = Label(text='Result',font = 'Arial 12', bg = 'lightgrey' )
result.pack(pady=10)

num.bind('<Return>', answer)

root.mainloop()