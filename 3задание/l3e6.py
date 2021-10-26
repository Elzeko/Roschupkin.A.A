# -- coding: utf-8 --
n = int(input("введите число факториала n:"))
sum = 1
for i in range(1, n + 1):
    sum *= i
print(sum)    