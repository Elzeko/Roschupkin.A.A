# -- coding: utf-8 --
N = int(input())
a = 1
while 2 ** a < N:
    a += 1
else:
    print('Показатель степени:' ,a -1)
    print('Степень:' ,2 ** (a - 1))