import simple_draw as sd
point1= sd.get_point(400, 400)

def corner5(point,angle,length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    return v1.end_point
point=point1
for angle in range(0,240,120):
    point=corner5(point=point,angle=angle,length=100)
else :
     sd.line(start_point=point1,end_point=point)
sd.pause()

import simple_draw as sd
point1 = sd.get_point(200, 200)


