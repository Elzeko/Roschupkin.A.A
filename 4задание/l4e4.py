# -- coding: utf-8 --
S = input()
m = S.find(' ')
print(S[m+1:]+S[m]+S[:m])