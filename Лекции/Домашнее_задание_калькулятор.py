import tkinter as tk

window = tk.Tk()
window.title('Калькулятор')
window.geometry('420x320')

result_label = tk.Label(window, text='Результат: -', font=('Arial, 16'))
result_label.pack(pady=10)

n = tk.Label(window, text='Введите три числа и нажмите на кнопку для вычисления суммы', font=('Arial', 10))
n.pack(pady=10)

first_entry = tk.Entry(window, font=('Arial', 14))
first_entry.pack(pady=10)

second_entry = tk.Entry(window, font=('Arial', 14))
second_entry.pack(pady=10)

third_entry = tk.Entry(window, font=('Arial', 14))
third_entry.pack(pady=10)


def on_add():
    a = int(first_entry.get())
    b = int(second_entry.get())
    c = int(third_entry.get())
    result_label.config(text=f'Результат: {a + b + c}')

def on_multiply():
    a = int(first_entry.get())
    b = int(second_entry.get())
    c = int(third_entry.get())
    result_label.config(text=f'Результат: {a * b * c}')


tk.Button(window, text='Сложить три числа', font=('Arial', 14), command=on_add).pack(pady=10)
tk.Button(window, text='Умножить три числа', font=('Arial', 14), command=on_multiply).pack(pady=10)

window.mainloop()

