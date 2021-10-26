
# -- coding: utf-8 --
n=int(input("введите кол-во чисел фибаначи n:"))
k=int(input("введите порядковый номер k:"))
fib1=1
fib2=1
sum=0
for i in range(n):
    b=fib1
    fib1=fib2
    fib2=fib1+b
    if i>=k:
        sum+=b
print(sum)