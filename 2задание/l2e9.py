# -- coding: utf-8 --
n = int(input())
n1 = 0
m = int(input())
m1 = 0
k = int(input())
def F(n, n1, m, k):
  for n1 in range(1, n):
    for m1 in range(1, m):
      if k < m * n and k == m * n1 or k == n * m1:
        return 'да'
      else:
        return'нет'
print(F(n, n1, m, k)) 
