# -- coding: utf-8 --
n = int(input("введите кол-во слогаемых n:"))
fib1 = 1
fib2 = 1
sum = 0
for i in range(n):
    b = fib1
    fib1 = fib2
    fib2 = fib1+b
    sum += b
print(sum)