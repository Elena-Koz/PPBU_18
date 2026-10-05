# import tkinter as tk
#
# window = tk.Tk()
# window.title('Мой калькулятор')
# window.geometry("420x320")
#
# result_label = tk.Label(window, text='Результат: —', font=('Arial', 18))
# result_label.pack(pady=10)
#
# tk.Label(window, text='Первое число', font=('Arial', 12)).pack()
# first_entry = tk.Entry(window, font=('Arial', 14))
# first_entry.pack(pady=5)
#
# tk.Label(window, text='Второе число', font=('Arial', 12)).pack()
# second_entry = tk.Entry(window, font=('Arial', 14))
# second_entry.pack(pady=5)
#
#
# def on_add():
#     a = int(first_entry.get())
#     b = int(second_entry.get())
#     result_label.config(text=f'Результат: {a + b}')
#
#
# tk.Button(window, text='Сложить', font=('Arial', 14), command=on_add).pack(pady=10)
#
# window.mainloop()

# import tkinter as tk
#
# window = tk.Tk()
# window.title('Мой калькулятор')
# window.geometry("420x320")
#
# result_label=tk.Label(window, text= 'Результат: —', font = ('Arial', 18))
# result_label.pack(pady = 10)
#
# tk.Label(window, text='Первое число', font= ('Arial', 16))
# first_entry = tk.Entry(window, font=('Arial', 14))
# first_entry.pack(pady=5)
#
# tk.Label(window, text='Второе число', font= ('Arial', 16))
# second_entry = tk.Entry(window, font=('Arial', 14))
# second_entry.pack(pady=5)
#
# def on_add():
#     a = int(first_entry.get())
#     b = int(second_entry.get())
#     result_label.config(text=f'Результат: {a + b}')
#
# def on_subtract():
#     a = int(first_entry.get())
#     b = int(second_entry.get())
#     result_label.config(text=f'Результат: {a - b}')
#
# tk.Button(window, text='Сложить', font=('Arial', 14), command=on_add).pack(pady=10)
# tk.Button(window, text='Вычесть', font=('Arial', 14), command=on_subtract).pack(pady=10)
# window.mainloop

# import tkinter as tk
#
# window = tk.Tk()
# window.title('Мой калькулятор')
# window.geometry("420x320")
#
# result_label = tk.Label(window, text='Результат: —', font=('Arial', 18))
# result_label.pack(pady=10)
#
# tk.Label(window, text='Первое число', font=('Arial', 12)).pack()
# first_entry = tk.Entry(window, font=('Arial', 14))
# first_entry.pack(pady=5)
#
# tk.Label(window, text='Второе число', font=('Arial', 12)).pack()
# second_entry = tk.Entry(window, font=('Arial', 14))
# second_entry.pack(pady=5)
#
#
# def on_add():
#     a = int(first_entry.get())
#     b = int(second_entry.get())
#     result_label.config(text=f'Результат: {a + b}')
#
#
# def on_subtract():
#     a = int(first_entry.get())
#     b = int(second_entry.get())
#     result_label.config(text=f'Результат: {a - b}')
#
#
# tk.Button(window, text='Вычесть', font=('Arial', 14), command=on_subtract).pack(pady=10)
# tk.Button(window, text='Сложить', font=('Arial', 14), command=on_add).pack(pady=10)
#
# window.mainloop()
#
# import tkinter as tk
# window = tk.Tk()
# window.title('Мой калькулятор')
# window.geometry('420x320')
#
# result_label = tk.Label(window, text = 'Результат: —', font = ('Arial', 16))
# result_label.pack(pady = 10)
#
# tk.Label(window, text='Первое число', font=('Arial', 12)).pack()
# first_entry = tk.Entry(window, font=('Arial', 14))
# first_entry.pack(pady=5)
#
# tk.Label(window, text='Второе число', font=('Arial', 12)).pack()
# second_entry = tk.Entry(window, font=('Arial', 14))
# second_entry.pack(pady=5)

# def on_add():
#     a = int(first_entry.get())
#     b = int(second_entry.get())
#     result_label.config(text=f'Результат: {a + b}')
#
#
# def on_subtract():
#     a = int(first_entry.get())
#     b = int(second_entry.get())
#     result_label.config(text=f'Результат: {a - b}')
#
#
# def on_swap():
#     tmp = first_entry.get()
#     first_entry.delete(0, tk.END)
#     first_entry.insert(0, second_entry.get())
#     second_entry.delete(0, tk.END)
#     second_entry.insert(0, tmp)
#
#
# tk.Button(window, text='Вычесть', font=('Arial', 14), command=on_subtract).pack(pady=10)
# tk.Button(window, text='Поменять местами', font=('Arial', 14), command=on_swap).pack(pady=10)
# tk.Button(window, text='Сложить', font=('Arial', 14), command=on_add).pack(pady=10)
#
#
# window.mainloop()

# import tkinter as tk
#
# window = tk.Tk()
# window.title('Мой калькулятор')
# window.geometry("420x320")
#
# result_label = tk.Label(window, text='Результат: -', font=('Arial, 16'))
# result_label.pack(pady=10)
#
# tk.Label(window, text='Первое число', font=('Arial, 14')).pack()
# first_entry = tk.Entry(window, font=('Arial', 12))
# first_entry.pack(pady=5)
#
# tk.Label(window, text='Второе число', font=('Arial, 14')).pack()
# second_entry = tk.Entry(window, font=('Arial', 12))
# second_entry.pack(pady=5)
#
#
# def on_add():
#     try:
#         a = int(first_entry.get())
#         b = int(second_entry.get())
#         result_label.config(text=f'Результат: {a + b}')
#
#     except ValueError:
#         result_label.config(text='Ошибка: введите целые числа', fg='red')
#
# def on_substract():
#     try:
#         a = int(first_entry.get())
#         b = int(second_entry.get())
#         result_label.config(text=f'Результат: {a - b}')
#     except ValueError:
#         result_label.config(text= 'Ошибка: введите целые числа', fg='red')
#
#
# def on_swap():
#     tmp = first_entry.get()
#     first_entry.delete(0, tk.END)
#     first_entry.insert(0, second_entry.get())
#     second_entry.delete(0, tk.END)
#     second_entry.insert(0, tmp)
#
#
#
# tk.Button(window, text='Сложить', font=('Arial', 12), command=on_add).pack(pady=10)
# tk.Button(window, text = 'Поменять местами', font = ('Arial', 12), command = on_swap).pack(pady=10)
# tk.Button(window, text='Вычесть', font=('Arial', 12), command=on_substract).pack(pady=10)
#
#
# window.mainloop()
#
# import tkinter as tk
#
# window = tk.Tk()
# window.title('Мой калькулятор')
# window.geometry("420x320")
#
# result_label = tk.Label(window, text='Результат: —', font=('Arial', 18))
# result_label.pack(pady=10)
#
# tk.Label(window, text='Первое число', font=('Arial', 12)).pack()
# first_entry = tk.Entry(window, font=('Arial', 14))
# first_entry.pack(pady=5)
#
# tk.Label(window, text='Второе число', font=('Arial', 12)).pack()
# second_entry = tk.Entry(window, font=('Arial', 14))
# second_entry.pack(pady=5)
#
#
# def on_add():
#     try:
#         a = int(first_entry.get())
#         b = int(second_entry.get())
#         result_label.config(text=f'Результат: {a + b}')
#     except ValueError:
#         result_label.config(text='Ошибка: введите целые числа')
#
#
# def on_subtract():
#     try:
#         a = int(first_entry.get())
#         b = int(second_entry.get())
#         result_label.config(text=f'Результат: {a - b}')
#     except ValueError:
#         result_label.config(text='Ошибка: введите целые числа')
#
#
# def on_swap():
#     tmp = first_entry.get()
#     first_entry.delete(0, tk.END)
#     first_entry.insert(0, second_entry.get())
#     second_entry.delete(0, tk.END)
#     second_entry.insert(0, tmp)
#
#
# tk.Button(window, text='Вычесть', font=('Arial', 14), command=on_subtract).pack(pady=10)
# tk.Button(window, text='Поменять местами', font=('Arial', 14), command=on_swap).pack(pady=10)
# tk.Button(window, text='Сложить', font=('Arial', 14), command=on_add).pack(pady=10)
#
# window.mainloop()
