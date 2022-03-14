# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе



lamp_summ = 0
lamp_cost = 0
chair_summ = 0
chair_cost = 0
sofa_summ = 0
sofa_cost = 0
table_summ = 0
table_cost = 0

for item in store:
    if item == goods['Лампа']:
        for lamp in store[item]:
            quantity, cost= lamp['quantity'],lamp['price']
            print(quantity,cost)
            lamp_summ+=quantity
            lamp_cost+=quantity*cost
    elif item == goods['Стол']:
        for table in store[item]:
            quantity, cost = table['quantity'],table['price']
            table_summ +=quantity
            table_cost +=cost*quantity
    elif item == goods['Диван']:
        for sofa in store[item]:
            quantity, cost = sofa['quantity'], sofa ['price']
            sofa_summ += quantity
            sofa_cost += cost * quantity
    elif item == goods['Стул']:
        for chair in store[item]:
            quantity,cost = chair['quantity'], chair['price']
            chair_summ += quantity
            chair_cost += quantity*cost
print('Всего ламп ',lamp_summ,'на сумму',lamp_cost, 'руб')
print('Всего столов ',table_summ,'на сумму',table_cost,'руб')
print('Всего стульев',chair_summ,'на сумму',chair_summ,'руб')
print('Всего диванов',sofa_summ,'на сумму',sofa_cost,'руб')



