# -- coding: utf-8 --
S = input()
m = int(len(S))
n = int(len(S)) // 2 + 1
f = str(S[n:m]) + str(S[:n])
print(m ,n ,f)