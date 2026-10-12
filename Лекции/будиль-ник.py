'''Будильник'''
from tkinter import *
from tkinter import messagebox as mb
import time
import pygame


pygame.mixer.init()
pygame.mixer.music.load('Kalimba.mp3')

def tick():
    global screen_time, time_alarm
    current_time = time.strftime("%H:%M:%S")
    if (time_alarm == current_time or
            time_alarm == time.strftime("%X:%M") or
            time_alarm == time.strftime("%H")):
        time_alarm = ''
        pygame.mixer.music.stop()
    screen_time.after(1000, tick)
    screen_time.config(text=current_time)


def on_click():
    global time_alarm
    time_alarm = entry_time.get().strip()

    mb.showinfo('Включение будильника',
                f'Будильник включен на {time_alarm}')


def off_click():
    global time_alarm
    time_alarm = ''
    entry_time.delete(0, END)
    pygame.mixer.music.stop()
    mb.showwarning('Выключение будильника',
                f'Будильник выключен')

time_alarm = ''
root = Tk()
root.title('будильник')
root.geometry("400x340")
root.config(bg='black')
screen_time = Label(text='00:00:00', font='Arial, 50')
screen_time.config(bg='black', fg='lime')
screen_time.pack()

entry_time = Entry(root, width=20, font='Arial, 20', justify=CENTER)
entry_time.pack()

on = Button(root, text='Включить', font=('Arial, 10'), bg='green', width=15, command=on_click).pack(pady=10)
off = Button(root, text='Выключить', font=('Arial, 10'), bg='green', width=15, command=off_click).pack()

tick()
root.mainloop()
