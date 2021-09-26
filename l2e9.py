# -- coding: utf-8 --
a = int(input())
b = int(input())
c = int(input())
d = 0
def F(a,b,c,d):
  d = (a * b) / 2
  if (d == c): 
    return 'Да'
  elif (d != c): return 'Нет'
print(F(a,b,c,d))