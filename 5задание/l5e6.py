# -- coding: utf-8 --
a = int(input('Введите число:'))
n = 0
s = 0
while a != 0:
    n += 1
    s += a
    a = int(input('Введите число:'))
print(s / n)