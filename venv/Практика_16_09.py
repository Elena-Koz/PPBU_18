# While

# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i += 1
# print ()
# n = 0
# while n <= 0:
#     n = int(input('Insert positive: '))
#     print(n)
# print()
#
# p = ' '
# while p != 'password':
#     p = input("Insert password: ")
#     print("Program starts")
# print()

import random

n = random.randint(1,7) # программа будет загадывать числа от 1 до 7
a = 0
while a != n:
    a = int(input('Guess number '))
print(f"Congrats! You are sucseed! It is number {n}")