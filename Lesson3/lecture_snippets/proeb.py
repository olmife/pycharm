user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
month_list = {
    1 : 30,
    2 : 28,
    3 : 31,
}
if user_input in month_list:
    print(month_list.get(user_input))

user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
month_list = {
    1: 30,
    2: 28,
    3: 31,
}
if month in month_list:
    print(month_list.get(month))