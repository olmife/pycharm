# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (600, 800)
point_0 = sd.get_point(300, 30)

def draw_branch(point,point2 , angle, angle2, length, delta):
    if length < 30:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v1.draw()
    v2 = sd.get_vector(start_point=point2, angle=angle2, length=length, width=1)
    v2.draw()
    next_point = v1.end_point
    next_point2= v2.end_point
    next_angle = angle - delta *random.uniform(-1,1)
    next_angle2= angle2 - delta *random.uniform(-1,1)
    next_length = length * random.uniform(0.7,0.8)
    draw_branch(point=next_point, point2=next_point2, angle=next_angle, angle2= next_angle2, length=next_length, delta=delta)
    draw_branch(point=v1.end_point, point2=next_point2, angle=next_angle, angle2=next_angle2,
                length=(next_length*random.uniform(0.7,0.8)), delta=delta)
    draw_branch(point=v1.end_point, point2=next_point2, angle=next_angle, angle2=next_angle2,
                length=(next_length*random.uniform(0.7,0.8)), delta=delta)
    draw_branch(point=v1.end_point, point2=next_point2, angle=next_angle, angle2=next_angle2,
                length=(next_length * random.uniform(0.7, 0.8)), delta=delta)
    draw_branch(point=v1.end_point, point2=next_point2, angle=next_angle, angle2=next_angle2,
                length=(next_length * random.uniform(0.7, 0.8)), delta=delta)
    draw_branch(point=v1.end_point, point2=next_point2, angle=next_angle, angle2=next_angle2,
                length=(next_length * random.uniform(0.7, 0.8)), delta=delta)
    draw_branch(point=v1.end_point, point2=next_point2, angle=next_angle, angle2=next_angle2,
                length=(next_length * random.uniform(0.7, 0.8)), delta=delta)
for delta in range(-80, 90, 20):
    draw_branch(point=point_0,point2=point_0, angle=random.randint(30,150), angle2=random.randint(30,150),  length=100, delta=delta)

sd.pause()


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


