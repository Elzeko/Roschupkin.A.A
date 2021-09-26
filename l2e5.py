# -- coding: utf-8 --
a = int(input())
b = int(input())
c = int(input())
def min(a,b,c):
  if (a < c) and (a < b):
    return a
  elif b < c: return b
  else: return c
print(min(a,b,c))