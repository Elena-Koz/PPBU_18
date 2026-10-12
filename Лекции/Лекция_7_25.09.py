'''https://github.com/StIgorLeonSimf/PPBU'''

'''Ткинтер'''
# from tkinter import *
#
# # def answer(event):
# #     answ = num.get().strip()
# #     result.config(text = answ)
#
#
# def answer():
#     answ = num.get().strip()
#     result.config(text = answ)
#
# root = Tk()
# root.title("Start")
# root.geometry("300x300")
#
# prompt = Label(text = 'Введите значение')
# prompt.pack()
#
# num = Entry(width = 5, font = 'Arial 15')
# num.pack()
#
# result = Label(text='Result',font = 'Arial 12', bg = 'lightgrey' )
# result.pack(pady=10)
#
# btn = Button(text = 'Выполнить', command = answer)
# btn.pack()
#
# num.bind('<Return>', answer)
#
# root.mainloop()

'''Библиотека Day/Time'''
from datetime import datetime, date, time, timedelta

# d = date(2024, 12, 31)
# print(d, type(d))
#
# t = time(12, 31, 16)
# print(t, type (t))
#
# dt = datetime.combine(d, t)
# print(dt, type(dt))

# d= date.today()
# # dt= datetime.now()
# print(dt)
# print(d)
# dt = datetime.now().replace(microsecond = 0)
# dt = dt.replace(year = 2020, month = 12, day = 24)
# print(dt)
#
# dtt = input('Введите дату (дд.мм.гггг):')
# datte = datetime.strptime(dtt, '%d.%m.%Y')
# print(datte, type(datte))

# dt = datetime.now().replace(microsecond=0)
# dtt = dt.timetuple()
# print(dtt)

# dtt = dt.isocalendar()
# print(dtt)
#
# day = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')
# print(day[dt.weekday()])

'Задача : рассчитать время до даты'

birthday = input('Введите дату рождения (дд.мм.гггг):')
birthday = datetime.strptime(birthday, '%d.%m.%Y').date()
dt_now = date.today()
year_ = dt_now.year
birthday = birthday.replace(year=year_)
print(birthday, dt_now, year_)
if birthday < dt_now:
    birthday = birthday.replace(year=year_ + 1)
res = birthday - dt_now

if res.days==0:
    print('С днем рожденичя!')
else:
    print(f'До Вашего дня рождения осталось {res.days} дн.')
