# -- coding: utf-8 --
a = int(input())
n = 2
if a >= 2:
    while a % n != 0:
        n += 1
    print(n)
else:
    print('число меньше 2 ')