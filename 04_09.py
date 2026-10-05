from math import sqrt
a = 3
b = 4
c = 5

s = a * b / 2
p = (a + b + c) / 2
s = sqrt(p * (p-a) * (p - b) * (p - c))
print(round(s, 2))