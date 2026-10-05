# s = ' Здравствуйте, гости!'
# print(s.capitalize())
# print(s.rjust(40))
# print(s.ljust(40))
# print(s.center(40))
# print(s.strip('!'))
# print(s.strip('Зд' '!'))
# print(s.index('т', 8, 11))
# print(s.replace('т', 'LN').replace(',', ''))

#----------СПИСКИ (list)-------------
# num = [22,33,44,55,99]
# print(num[-2])
# print(num[1:-2])
# nn = num
# nn = num
# print(num, id(num))
# print(nn, id(nn))
# print(nn is num)

# nn = num
# nn = num[:]
# num[1]=333
# print(num, id(num))
# print(nn, id(nn))
# print(nn is num)

# num = [1, 2, [32, 4]]
# nn = num
# nn = num.copy()
# num[1]=333
# num[-1][1]=400
# print(num, id(num))
# print(nn, id(nn))
# print(nn is num)

# num = [22,33,44,55,99]
# # num.insert(0,300)
# # print(num)
#
# n = num.pop()
# n1 = num.pop(0)
# print(n, n1)
# print(num)

# num = [22,100,44,100,99, 100, 100]

# num.remove(100)
# print(num)
# while 100 in num:
#     num.remove(100)
# print(num)

num = [22,33,44,55,99]
# print((100)in num)
for i in range(len(num)):
    print(i, num[i], end=" ")
print()

cnt=0
for i in num:
    print(cnt, i, end=" ")
    cnt += 1
print()

'''Кортеж (tuple)'''
tp =(22, 33, 44, 99)
# k = 7,
# print(k, type(k), k[0])

# k , *i , z = 7, 5, 9, 10, 1, 32, 56, 100
# print(k, i, z)
# print(type(k))
# print (type(i))
# print(type(z))