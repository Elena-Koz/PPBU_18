# def voice_price (words, rate = 10):
#     return words * rate
# print(voice_price(3))
#
# def has_pass(points, threshold=10):
#     return points >= threshold
# print(has_pass(0,0))

# def shift_point(point, dx, dy):
#     x, y = point
#
#     return (x + dx, y + dy)
# print(shift_point((1, 1), -2, -3))
'''Напишите best_score(scores), которая возвращает наибольший результат игрока. Если игрок ещё не сыграл ни разу и список пуст, верните None. Для отрицательных результатов правило не меняется.'''
# def best_score(scores):
#     if not scores:
#         return None
#     return max(scores)
# print(best_score([-5, -2, -9]))


'''Каждому результату в списке добавляют одинаковый бонус. '''
'''Напишите add_vibe(values, bonus=1),'''
'''которая возвращает новый список увеличенных результатов. '''
'''Исходный список должен остаться прежним.'''

# def add_vibe(values, bonus=1):
#     return [value + bonus for value in values]
# result = add_vibe([2, 5])
# print(result)

# import tkinter as tk
#
# window = tk.Tk()
# window.title('Мой калькулятор')
# window.geometry("420x320")
# msg=tk.Label(window, text='Привет!', font=('Arial',18))
# msg.pack(pady=10)
# def on_start():
#     msg.config(text='Готов к расчетам!')
#
# start_button = tk.Button(window, text='Начать', font=('Arial', 14), command=on_start)
# start_button.pack(pady=10)
#
# window.mainloop()
#
# import tkinter as tk
#
# window = tk.Tk()
# window.title('Мой калькулятор')
# window.geometry("420x320")
# n = 0
# msg=tk.Label(window, text='Нажатий: 0.', font=('Arial',18))
# msg.pack(pady=10)
# def on_check():
#     global n
#     n += 1
#     msg.config(text=f'Нажатий: {n}')
#
#
# check_button = tk.Button(window, text='Проверить.', font=('Arial', 14), command=on_check)
# check_button.pack(pady=10)
#
#
# window.mainloop()


# import tkinter as tk
#
# window = tk.Tk()
# window.title('Мой калькулятор')
# window.geometry("420x320")
#
#
# name_entry = tk.Entry(window, font=('Arial', 14))
# name_entry.pack(pady=10)
# msg=tk.Label(window, text='Привет!', font=('Arial',18))
# msg.pack(pady=10)
#
# def on_greet():
#     name = name_entry.get().strip()
#     if name:
#         msg.config(text=f'Привет, {name}!')
#     else:
#         msg.config(text='Привет, гость!')
#
#
# greet_button = tk.Button(window, text='Поздороваться', font=('Arial', 14), command=on_greet)
# greet_button.pack(pady=10)
#
# window.mainloop()

# import tkinter as tk
#
# window = tk.Tk()
# window.title('Мой калькулятор')
# window.geometry("420x320")
#
# msg = tk.Label(window, text='Результат: —', font=('Arial', 18))
# msg.pack(pady=10)
#
# entry = tk.Entry(window, font=('Arial', 14))
# entry.pack(pady=10)
#
# def on_double():
#     n = int(entry.get())
#     msg.config(text=f'Результат: {2 * n}')
#
# double_button = tk.Button(window, text='Удвоить', font=('Arial', 14), command=on_double)
# double_button.pack(pady=10)
#
# window.mainloop()

# import tkinter as tk
#
# window = tk.Tk()
# window.title('Мой калькулятор')
# window.geometry("420x320")
#
# msg = tk.Label(window, text='Результат: —', font=('Arial', 18))
# msg.pack(pady=10)
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
#     msg.config(text=f'Результат: {a + b}')
#
# add_button = tk.Button(window, text='Сложить', font=('Arial', 14), command=on_add)
# add_button.pack(pady=10)
#
# window.mainloop()


import tkinter as tk

window = tk.Tk()
window.title('Мой калькулятор')
window.geometry("420x320")

msg = tk.Label(window, text='Результат: —', font=('Arial', 18))
msg.pack(pady=10)

tk.Label(window, text='Первое число', font=('Arial', 12)).pack()
first_entry = tk.Entry(window, font=('Arial', 14))
first_entry.pack(pady=5)

tk.Label(window, text='Второе число', font=('Arial', 12)).pack()
second_entry = tk.Entry(window, font=('Arial', 14))
second_entry.pack(pady=5)


def on_add():
    a = int(first_entry.get())
    b = int(second_entry.get())
    msg.config(text=f'Результат: {a + b}')

def on_add():
    a = int(first_entry.get())
    b = int(second_entry.get())
    msg.config(text=f'Результат: {a - b}')


add_button = tk.Button(window, text='Сложить', font=('Arial', 14), command=on_add)
add_button.pack(pady=10)
add_button = tk.Button(window, text='Вычесть', font=('Arial', 14), command=on_add)
add_button.pack(pady=10)

window.mainloop()