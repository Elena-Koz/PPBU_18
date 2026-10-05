import turtle
import time

Ugol = input ("Введите количество углов ")
Ugol = int(Ugol)
Color = input("Введите цвет на анг яз ")
turtle.color(Color)
turtle.begin_fill()
for i in range(Ugol):
    turtle.forward(100)
    turtle.left(360 / Ugol)
turtle.end_fill()
time.sleep(3)
