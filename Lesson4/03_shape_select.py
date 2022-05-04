# -*- coding: utf-8 -*-
# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

shape = input("Введите, пожалуйста, цвет фигуры: \n"
               "возможные варианты цветов:\n"
              "1:Треугольник\n"
              "2:Квадрат\n"
              "3:Пятиугольник\n"
              "4:Шестиугольник")
shape = int(shape)
import simple_draw as sd
point1 = sd.get_point(250, 250)
def corner5(point,angle,length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    return v1.end_point
point=point1
#triangle
if shape==1:
    for angle in range(0, 240, 120):
        point = corner5(point=point, angle=angle, length=100)
    else:
        sd.line(start_point=point1, end_point=point)
#coub
elif shape==2:
    for angle in range(0, 270, 90):
        point = corner5(point=point, angle=angle, length=100)
    else:
        sd.line(start_point=point1, end_point=point)
#5-angle
elif shape==3:
    for angle in range(0, 270, 72):
        point = corner5(point=point, angle=angle, length=100)
    else:
        sd.line(start_point=point1, end_point=point)
#6-angle
elif shape==4:
    for angle in range(0, 300, 60):
        point = corner5(point=point, angle=angle, length=100)
    else:
        sd.line(start_point=point1, end_point=point)
else:
    print("вы ввели неврное значение")
sd.pause()

