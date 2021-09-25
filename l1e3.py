# -- coding: utf-8 --
x = 18
name = 'Андрей'
age = 12
if (age > 0) and (age >= 16) and (age < 75) and (name != 'Иван'):
    print('Поздравлем вы поступили в ВГУИТ!')
elif age < 16: print('Сначала нужно окончить школу! Вам осталось учится',x-age,'лет.')