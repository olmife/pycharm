# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом


# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg



sd.pause()
# -*- coding: utf-8 -*-

import simple_draw as sd


# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны

# Нарисовать все фигуры
# Выделить общую часть алгоритма рисования в отдельную функцию
# Измените функции рисования фигур, вызывая из них общую функцию.
# Придумать, как устранить разрыв в начальной точке фигуры

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

def triangle(point, angle, length):
    for _ in range(3):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        angle = angle + 120
        point = v1.end_point


def square(point, angle, length):
    for _ in range(4):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        angle = angle + 90
        point = v1.end_point


def pentagon(point, angle, length):
    for count in range(4):
        count += 1
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        if count == 1:
            v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        if count == 4:
            sd.line(start_point=v1.end_point, end_point=v2.start_point, width=3)
        angle = angle + 70
        point = v1.end_point


def hexagon(point, angle, length):
    for count in range(5):
        count += 1
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        if count == 1:
            v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        if count == 5:
            sd.line(start_point=v1.end_point, end_point=v2.start_point, width=3)
        angle = angle + 60
        point = v1.end_point


point_triangle = sd.get_point(100, 100)
triangle(point=point_triangle, angle=50, length=150)

point_square = sd.get_point(400, 100)
square(point=point_square, angle=20, length=150)

point_pentagon = sd.get_point(100, 350)
pentagon(point=point_pentagon, angle=20, length=100)

point_hexagon = sd.get_point(400, 350)
hexagon(point=point_hexagon, angle=20, length=100)

sd.pause()

# def draw(point, angle, length):
#     for _ in range(3):
#         v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         v1.draw()
#         angle = angle + 120
#         point = v1.end_point
#     for _ in range(4):
#         v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         v1.draw()
#         angle = angle + 90
#         point = v1.end_point
#     for count in range(4):
#         count += 1
#         v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         v1.draw()
#         if count == 1:
#             v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         if count == 4:
#             sd.line(start_point=v1.end_point, end_point=v2.start_point, width=3)
#         angle = angle + 70
#         point = v1.end_point
#     for count in range(5):
#         count += 1
#         v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         v1.draw()
#         if count == 1:
#             v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         if count == 5:
#             sd.line(start_point=v1.end_point, end_point=v2.start_point, width=3)
#         angle = angle + 60
#         point = v1.end_point
#
#
# point_triangle = sd.get_point(350, 150)
# draw(point_triangle, 50, 150)