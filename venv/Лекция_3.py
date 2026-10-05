# from turtle import *
#
# shape ('turtle')
# speed ()
# colormode(255)
# pensize (4)
# r = 255
# g = 255
# b = 0
#
# br = 0
# bg = 255
# bb = 0
# color(br, bg, bb)
#
# for j in range(150,10,-25):
#     #fillcolor(r, g, b)
#     color((br, bg, bb), (r, g, b))
#     for i in range (8):
#         #fillcolor()
#         begin_fill()
#         circle(j)
#         end_fill()
#         rt(45)
#     r -= 30
#     g -= 15
#     b += 30
#     br += 30
#     bg -= 30
#     bb += 30


# import turtle
#
# turtle.colormode(255)
# for i in range (60):
#     turtle.color(127+ i*2, 127 + i*2, 80 + i*2)
#     turtle.circle(i)

# mainloop()

# i = 0
# while i < 10:
#     i += 1
#     if i == 7:
#         continue
#     print(i, end = " ")
# print()
#
# i = 0
# while i < 10:
#     i += 1
#     if i == 17:
#         break
#     print(i, end = " ")
# else:
#     print('\nOK')
# print()

# n = int(input('>'))
# sm = 0
# cnt = 0
# while n != 0:
#     sm += n
#     cnt += 1
#     print(f'Сумма - {sm}\n'
#           f'Кол-во - {cnt}')
#     n = int(input('>'))

# n = int(input('>'))
# nn = n
# sm = 0
# cnt = 0
# while n > 0:
#     rem = n % 10 # остаток от деления на 10
#     sm += rem
#     cnt += 1
#     n //= 10
#
# print(f'В числе "{nn}", {cnt} цифры, суммой {sm}') # в ф-сроке пишем то, что хотим увидеть в '' , а в фигурных скобках - переменные

s = 'Здравствуйте, гости!'
# print(s[0])
# print(s[1])
# print(s[-1])
# print(len(s))
# print(s[::1])
# print(s[:12])
# print(s[::-1])

# for i in s:
#     print(i, end=' ')

# for i in range(len(s)):
#     print(s[i], end = ' ')

# print(s.index(','))
# print(s.isalpha())
# print(s.isdigit())
# print(s.startswith('З'))
# print(s.endswith('!'))
# print(s.lower())
# print('и' in s)
print(n:=s.lower())
print(n)
print(s.title())