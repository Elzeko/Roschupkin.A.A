a = int(input('Введите число:'))
b = 0
n = 0
m = 0
while a != 0:
    if b == a:
        n += 1
    else:
        b = a
        m = max(m, n)
        n = 1
    a = int(input('Введите число:'))
m = max(m, n)
print('Наибольшее количество повт. элементов:' ,m)