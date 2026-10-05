import turtle as t

# 1. Create the screen object
screen = t.Screen()

# 2. Get the underlying tkinter window and pull it to the front
root_window = screen.getcanvas().winfo_toplevel()
root_window.call('wm', 'attributes', '.', '-topmost', '1')
root_window.call('wm', 'attributes', '.', '-topmost', '0')

t.colormode(255)
for i in range (60):
    t.color(127 , 127 , 80 + i*2)
    t.circle(i)
# 3. Always keep the window open at the end
t.done()
