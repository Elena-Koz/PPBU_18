import turtle as t

# t.ht () #hideturtle
# t.pensize(3)
# t.color("blue")
# # t.rt(120)
# for i in range(4, 56, 4):
#     t.fd(i)
#     t.rt(90)
# t.rt(270)
# for i in range(52, 0, -4):
#     t.fd(i)
#     t.rt(90)

# import turtle as t # Циклы - 4 цикла
# t.ht()
# r = 40
# t.pensize(5)
# t.color("#FFA500")
# t.fillcolor("#A200FF")
# for i in range (6):
#     t.begin_fill()
#     t.circle(r)
#     t.end_fill()
#     t.rt(60)
# r = 30
# for i in range (6):
#     t.begin_fill()
#     t.circle(r)
#     t.end_fill()
#     t.rt(60)
# r = 20
# for i in range (6):
#     t.begin_fill()
#     t.circle(r)
#     t.end_fill()
#     t.rt(60)
#
# r = 10
# for i in range (6):
#     t.begin_fill()
#     t.circle(r)
#     t.end_fill()
#     t.rt(60)


# Вложенные циклы - краткая запись
# t.ht()
# r = 40
# t.pensize(4)
# t.color("#FFA500")
# t.fillcolor("#A200FF")
# for j in range(4) :
#     for i in range (6):
#         t.begin_fill()
#         t.circle(r)
#         t.end_fill()
#         t.rt(60)
#     r = r - 10

# Вложенные циклы - 3 цветка подряд
# t.speed(0)
# # t.ht()
# # r = 20
# # t.pensize(4)
# # t.color("#FFA500")
# # t.fillcolor("#A200FF")
# # for j in range(4) :
# #     for i in range (6):
# #         t.begin_fill()
# #         t.circle(r)
# #         t.end_fill()
# #         t.rt(60)
# #     r = r - 5
# # t.pu() # pen up
# # t.fd(80)
# # t.pd() # pen down
# # r = 20
# # for j in range(4) :
# #     for i in range (6):
# #         t.begin_fill()
# #         t.circle(r)
# #         t.end_fill()
# #         t.rt(60)
# #     r = r - 5
# # t.pu() # pen up
# # t.fd(80)
# # t.pd() # pen down
# # r = 20
# # for j in range(4) :
# #     for i in range (6):
# #         t.begin_fill()
# #         t.circle(r)
# #         t.end_fill()
# #         t.rt(60)
# #     r = r - 5

# Запишем три цикла выше кратко:
# import time
# t.speed(0)
# t.ht()
# r = 20
# t.pensize(4)
# t.color("#FFA500")
# t.fillcolor("#A200FF")
# for k in range(3):
#     print("___k =  " + str(k))
#     for j in range(4) :
#         print("_j = " + str(j))
#         for i in range (6):
#             print ("i = " + str(i))
#             t.begin_fill()
#             t.circle(r)
#             t.end_fill()
#             t.rt(60)
#             time.sleep(0.1)
#         r = r - 5
#     t.pu() # pen up
#     t.fd(80)
#     t.pd() # pen down
#     r = 20

# Диапазоны (цвета) внутри вложенных циклов

# import turtle as t
#
# r = 40
# t.ht()
# t.colormode(255)
# t.pensize(10)
# t.color(255, 165, 0)
# t.fillcolor(162, 0, 255)
# for j in range (4):
#     for i in range(6):
#         t.begin_fill()
#         t.circle(r)
#         t.end_fill()
#         t.rt(60)
#     r = r - 10

# Введем диапазон range прямо в цикл

# import turtle as t
#
# r = 40
# t.ht()
# t.colormode(255)
# t.pensize(5)
#
# for r in range (40, 0, -10):
#     for i in range(6):
#         t.color(255, 165, r * 6)
#         t.fillcolor(162, r * 6, 255)
#         t.begin_fill()
#         t.circle(r)
#         t.end_fill()
#         t.rt(60)
#     r = r - 10

# Не работает
from turtle import*
shape("turtle")
speed(0)
colormode (255)
pensize(4)
r = 255
g = 255
b = 0
color ("green", (r,g,b))

for j in range(150, 10, -25):
    fillcolor (r , g, b)
        for i in range(8):
            begin_fill()
            circle(j)
            end_fill()
            rt(45)
        r -=30
        g -=15
        b +=30

mainloop