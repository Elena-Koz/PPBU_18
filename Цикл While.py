# i = 0
#
# while i < 10:
#     i += 1 # i + 1 всегда присваивается правая часть, после этой этой строки ай=1
#     if i == 7:
#         continue
#     print(i, end=" ")
# print()
#
# i = 0
# while i < 10:
#     i += 1 # i + 1 всегда присваивается правая часть, после этой этой строки ай=1
#     if i == 17:
#         break
#     print(i, end=" ")
#
# else:
#     print("\nOK")

# n = int(input(">"))
# cnt = 0
# while n != 0:
#     sm =+ n
#     cnt += 1
#     n = int(input(">"))
# print(f"Summ - {sm}\n"
#       f"Quantity - {cnt}")
#
#   s = 3 + 2
#     k = 1+1=1
# 123 %10 = 3
#     // 10 = 12 % 10
#
# n = int(input(">"))
# nn = n
# sm = 0
# cnt = 0
# while n > 0:
#     rem = n % 10
#     sm = + rem
#     cnt += 1
#     n//= 10
#
# print(f`В числе "{nn}" {cnt} ц.суммой {sm}`)
#
#
#

# Task 1
i = 3
while i < 50:
    print(i)
    i += 10

# Task 2
while True:
    password = input("Введите пароль: ")
    if len(password) >= 8:
        break
    print("Длина пароля должна быть не менее 8 символов")

# Task 3
while True:
    data = input("Введите параметры автомобиля по шаблону\nLADA 2010г 205000км 450000руб: ")
    params = data.split()
    if len(params) == 4:
        break
    print("Данные введены некорректно!")
print(f"Продаётся автомобиль\nМарка: {params[0]}\nГод выпуска: {params[1]}\nПробег: {params[2]}\nЦена: {params[3]}")
