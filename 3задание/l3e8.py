# -- coding: utf-8 --
n = int(input("введите кол-во ступенек<=9:"))
for i in range(n):
    for j in range(1, i+2):
        print(j, end = '')
    print()    