# -- coding: utf-8 --
n = int(input("введите кол-во слогаемых факториалов n:"))
sum = 1
sum1 = 0
for i in range(1, n + 1):
    sum *= i
    sum1 += sum
print(sum1)