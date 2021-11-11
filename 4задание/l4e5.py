# -- coding: utf-8 --
S = input()
m = S.find('f')
n = S.rfind('f')
if m != n:
    print('Номер первой f:',m)
    print('Номер второй f:',n)
elif m == n:
    if n == n == -1:
        print('f не найдено')
    else:
        print('Номер единственной f:',m)
    