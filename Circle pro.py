import turtle as t
# print(range(3))
r = input("Введите радиус: ")
r = int(r)

# 1. Create the screen object
screen = t.Screen()

# 2. Get the underlying tkinter window and pull it to the front
root_window = screen.getcanvas().winfo_toplevel()
root_window.call('wm', 'attributes', '.', '-topmost', '1')
root_window.call('wm', 'attributes', '.', '-topmost', '0')

t.colormode(255)
t.bk(80)
for i in range(3):
    t.begin_fill()
    t.color(255, 127, 80 * i)
    t.circle(r)
    t.end_fill()
    t.penup()
    t.fd(r * 2)
    t.pendown

# 3. Always keep the window open at the end
t.done()
