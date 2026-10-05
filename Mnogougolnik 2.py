import turtle as t
import time

t.ht()
Ugol = 8
t.color("red")
t.begin_fill()
for i in range(Ugol):
    t.forward(100)
    t.left(360 * 3 / Ugol)
t.end_fill()
time.sleep(3)
