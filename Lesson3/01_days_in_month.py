# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
if month==1:
    days= 31
elif month==2:
    days=28
elif month==3:
    days= 30
elif month==4:
    days=31
elif month==5:
    days=31
elif month==6:
    days= 30
elif month==7:
    days = 31
elif month==8:
    days = 31
elif month==9:
    days = 30
else :
    print('Вы ввели некорректное число месяца')
print('В этом месяце', days, 'дней')

user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
month_list = {
    1 : 30,
    2 : 28,
    3 : 31,
}
if month in month_list:K
    print(month_list.get(month))

