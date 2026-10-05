# PI = 3.1415926
# x = 6
#
#
# # n1 = int(input("Введите значение1: "))
# # n2 = int(input("Введите значение2: "))
# # print(n1 + n2)
# # print (type(n1), type(n2))
#
# # Решаем задачу по треугольнику
# from math import(sqrt)
# # 1. Вводим данные
# a = 3
# b = 4
# # 2. Решаем
# s = a*b/2 # это формула прямоугольного треугольника
# # Получаем результат
# print(s)
#
# # 1. Вводим данные
# a = 31
# b = 43
# c = 57
# # 2. Решаем
# p = (a + b + c) / 2 # Формула Герона
# s = sqrt (p * (p-a) * (p-b) * (p-c))
# # Получаем результат
# print(round(s, 2))

# Ветвления
# Операции сравнения
# a = 26
# b = 36
# c = a < b
# print(c)
#
# if a < b:
#     print('A < B')
#
# else:
#     if a < b:
#         print('A > B')
#     else:
#         print('A == B')
# print('END')

h = float(input('Введите время суток: '))
if h >= 4 and h <12:
    print('Morning')
elif h >=12 and h < 17:
    print('Day')
elif h >= 17 and h < 24:
    print('Evening')
elif h >= 0 and h < 4 or h == 24:
    print('Night')
else:
    print('Time is not correct')




# color = input('Цвет светофора: ')
# match color:
#     case 'red'| 'no':
#         print('STOP')
#     case'green':
#         print ('GO')
#     case 'yellow':
#         print ('READY')
#     case_:
#         print('цвет', color)

        #'ЦИКЛ for. Start for'
# for i in 23, 45, 22, 32:
#     print(i, 'YES')

# n = 10
# for i in range(20, n-1, -1):
#     print(i , end=' ')
# print()
# print(i)

# for i in range(1,10):
#     for j in range (1, 10):
#         print(f'{i*j:2}', end=' ')
#     print()


