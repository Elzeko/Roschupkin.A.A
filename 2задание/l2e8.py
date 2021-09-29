# -- coding: utf-8 --
a = int(input())
b = int(input())
c = int(input())
def F(a,b,c):
  if ((a == b) and (a == c)) or ((a == b) and (b == c)) or ((c == b) and (a == c)):
    return '3'
  elif (a == b) or (a == c) or (b == c): 
    return '2'
  else: return '0'
print(F(a,b,c))