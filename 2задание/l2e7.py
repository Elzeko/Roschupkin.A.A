# -- coding: utf-8 --
n = int(input())
def year(n):
  if ((n % 4 == 0) and (n % 100 != 0)) or (n % 400 == 0):
    return'Да'
  else: return'Нет'
print(year(n))