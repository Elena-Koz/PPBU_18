#Это часть лекции, на первую я опоздала
from tkinter import *

def answer(event):
    answ = num.get().strip()
    result.configure(text=answ)

root = Tk()
root.title('Старт')
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
print(WIDTH,HEIGHT)
root.geometry("300x300+480+250")

prompt = Label(text='Введите значение', font='Arial 15')
prompt.pack()
num = Entry(width=5, font='Arial 12', justify = 'center')
num.pack()

result = Label(text='   ', font='Arial 15', bg='light grey')
result.packpady=(10)


num.bind('<Return>', answer)


root.mainloop()