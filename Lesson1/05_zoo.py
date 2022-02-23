#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1,'Bear')
print(zoo)
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
zoo= zoo+birds
print(zoo)

#  и выведите список на консоль

# уберите слона
#  и выведите список на консоль
del zoo[3]
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
lion_cage= (zoo.index('lion'))+1
bird_cage= (zoo.index('lark'))-1
print ('Лев сидит в клетке номер:', lion_cage)
print('Жаворонок сидит в клетке номер:', bird_cage)


