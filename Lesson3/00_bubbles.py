# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point,step):
    radius=50
    for _ in range(3):
        radius+=step
        sd.circle(center_position=point, radius=radius, width=3)


for _ in range(100):
        point=sd.random_point()
        bubble(point=point, step=random.randint(2,30))



# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()


