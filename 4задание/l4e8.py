# -- coding: utf-8 --
S = input()
m = S[S.find('h'):S.rfind('h') + 1]
m = m[::-1]
print(S[:S.find('h')] + m + S[S.rfind('h') + 1:])