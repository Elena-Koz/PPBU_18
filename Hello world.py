x = 3
y = 5.45
# name = 'Mary'
# s = 'a'
# yes_no = True
#
# print(type(name))
# print(x, y, name, sep='...')
while True:
    try:
        x1 = float(input('Введите первое число: '))
        break
    except ValueError:
        print("Введённое значение не является числом")
x2 = float(input('Введите второе число: '))
x3 = float(input('Введите третье число: '))

print(f"Сумма чисел равна {x1+x2+x3}")
print("Hello, world")
print("Hello, world")