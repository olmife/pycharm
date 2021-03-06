# -*- coding: utf-8 -*-



# Часть 1.

# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()

# Результат решения см lesson_004/results/exercise_01_shapes.jpg
# def triangle(point,angle,lenth):
#     v1=sd.get_vector(start_point=point,angle=angle,length=length)
#     v1.draw()
#     v2=sd.get_vector(start_point=v1.end_point,angle=angle+120,length=length)
#     v2.draw()
#     v3=sd.get_vector(start_point=v2.end_point,angle=v2.angle+120,length=length)
#     v3.draw()
# def coub(point,angle,lenth):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle+90, length=length)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle+180, length=length)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle +270, length=length)
#     v4.draw()
# user_input = input("Введите, пожалуйста, номер месяца: ")
# month = int(user_input)
# print('Вы ввели', month)
# month_list = {
#     1 : 12,
#     2 : 28,
#     3 : 31,
# }
# if month in month_list:
#     print(month_list.get(month))
import simple_draw as sd
point1= sd.get_point(400, 400)
point2= sd.get_point(100,400)
point3= sd.get_point(100, 100)
point4= sd.get_point(400,100)
def corner5(point,angle,length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    return v1.end_point
# triangle
point=point1
for angle in range(0,240,120):
    point=corner5(point=point,angle=angle,length=100)
else :
     sd.line(start_point=point1,end_point=point)
# coub
point= point2
for angle in range(0,270,90):
    point=corner5(point=point,angle=angle,length=100)
else :
    sd.line(start_point=point2,end_point=point)
# corner5
point = point3
for angle in range(0,270,72):
    point=corner5(point,angle,100)
else :
    sd.line(start_point=point3,end_point=point)
# corner6
point = point4
for angle in range(0,300,60):
    point=corner5(point,angle,120)
else :
    sd.line(start_point=point4,end_point=point)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
