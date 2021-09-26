# -- coding: utf-8 --
n = int(input())
h = n % (1440) // 60
m = n % 60
print(h ,'часов:', m,'минут')
