# -- coding: utf-8 --
a=int(input("введите a:"))
b=int(input("введите b:"))
if a <= b:
    for i in range (a, b + 1):
        print(i)
else:
    print('a > b') 