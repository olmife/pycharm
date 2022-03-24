# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start_x,start_y=50,50
end_x,end_y=350,450

# def line(point1,point2,step):

for color in rainbow_colors:
        point1 = sd.get_point(start_x, start_y)
        point2 = sd.get_point(end_x, end_y)
        sd.line(start_point=point1, end_point=point2,color=color)
        start_x+=5
        end_x+=5
sd.pause()



# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво




sd.pause()
