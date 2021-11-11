# -- coding: utf-8 --
S = input()
m = S.count('f')
n = S.find('f')
if m > 0:
    if m > 1: 
        print(S.find('f', n + 1))
    else:
        print(-1)
else:
    print(-2)