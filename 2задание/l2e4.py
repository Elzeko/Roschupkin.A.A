# -- coding: utf-8 --
a = int(input())
b = int(input())
l = int(input())
N = int(input())
def shnr(a,b,l,N):
  return (2 * l + a * (2 * N - 1) + 2 * (N - 1) * b)
print(shnr(a,b,l,N))