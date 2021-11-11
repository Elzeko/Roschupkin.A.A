# -- coding: utf-8 --
S = input()
m = S.find('h')
n = S.rfind('h')
k = S[:m] + S[n+1:]
print(k)
