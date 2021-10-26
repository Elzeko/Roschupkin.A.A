# -- coding: utf-8 --
n=int(input("введите кол-во слагаемых n:"))
sum = 0
for i in range(0, n):
    sum += int(input("введите слагаемое:"))
print(sum)    