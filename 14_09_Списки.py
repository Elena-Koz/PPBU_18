"""list"""
"""Список - упорядоченный набор объектов"""

""" 0 1 2 3 4 """
num = [22, 33, 44, 55, 99]
""" -5 -4 -3 -2 -1 """
# print(num[0])
# print(num[2])
# print(num[1:-2]) # срез, как в строках. первый объект под ...
# print(num[:])
# print(num[::2]) #  в срезах разделяет позицию старт и позицию стоп не запятые, а двоеточия
# print(num[2:])
# print(num[2::-1])
# print(num[::-1]) # срезы формируют отдельный объект

# nn = num
# # print(num, id(num))
# # print(num, id(nn))
# # print(nn is num)

# nn = num
# nn = num [:]
# num[1] = 3333
# print(num, id(num))
# print(num, id(nn))
# print(nn is num)

# num = [1, 2, [32, 4]]
# nn = num
# nn = num[:]
# nn= num.copy()
# nn= num.deepcopy(num)
# num[1] = 3333
# num[-1][1] = 400
# print(num, id)
# print(num, id(nn))
# print(nn is num)

x = 100
y = 100

# num = [22, 33, 44, 55,99]
# print(num)
# num.append(100) #добавить в конец, константная сложность
# print(num)
# num.insert(0, 300) # num.insert(index: 0, object: 300), линейная временная сложность
# print(num)
# # не создаем новый объект , а меняем сущ-щий
# # num.extend([1,2]) # можно назвать канкатинацией
# num += [1, 2]
# # создаем новый объект
# um = num + [1, 2]
# print(num)
#
# n = num.pop()# удаляет объекты конца списка, константа
# # встреч-ся во всех коллекциях, кроме кортежа,
# # с каждой коллекцие работает по-разному
# nn = num.pop(0)
# print(n)
# print(num)

num = [100, 33, 100, 55,100] # убирает только первое вхождение
num.remove(100)
print(num)
# print(num.index(100))
# как убрать все 100 в списке? через while
# while 100 in num:
#     num.remove(100)
# print(num)
print(num.index(100))
print(num.count(100))

# num.clear()
# print(num)

# Циклы
num = [22, 33, 44, 55, 99, 11]

# пришли цыфры, я хочу инвертироватьи х в строку
# for i in range(len(num)):   #len(num) вернет на число 5
#     print(i, num[i], end = " ") # видим и инцекс и значение
# print()
# cnt = 0 #счетчик
# for i in num:
#     print(cnt, i, end= " ")
#     cnt += 1
# print()
names = ['Dasha', 'Masha', 'Sasha', 'Glasha', 'Andrusha']
# names.reverse() № в обратной последовательности
# names.sort() # сорт по алфавиту
# names.sort(reverse=True)
# for k, i in enumerate(names1)
#     print(f'{k}, {i}')
# print(names)

for i in zip(names, num):
    print(i)

""" кортеж (Tuple)"""
"""Кортеж - упорядоченный набор неизменяемых объектов"""

# tp = (22, 33, 44, 99)
# k, i, z = 7,  # k - это константа,
# print(k, type (k))
# print(k, type(k), k[0])

tp = (22, 33, 44, 99)
k, *i, z = 7, 5, 9, 10, 1, 32, 56,100 # k - это константа, каждоц переменной по значение
print(k, i, z)

arr = [0] * 10
print(arr)
for i in range(len(arr)):
    arr[i] = i + 1 # задача заполить список от 1 до 10
print(arr)

ls = []
for i in range(10):
    ls.append(i + 1)
print(ls)



tp = ('login', 'password')
print(tp)
buf = list(tp)
buf[-1] = 'new password'
tp = tuple(buf)
print(tp)

"""левый циклический цикл"""
# l = [22, 33 44, 55, 99]
# temp = l[0]
# n = len(l) # len(l) равен 5, т к 5 цифр в спике
# for i in range (n-1):
#     l[i] = l[i + 1]
# l[-1] = temp
# print(l)
# temp - l.pop(0)
# l.append(temp)


x = 10
y = 15
print (x,y)
z = x
x = y
y = z
print (x,y)

x, y = y, x
print (x,y)
print(5 if len(ls)>7 else 125)
ls = [i+ 1 for i in range (10)]
print(ls)
