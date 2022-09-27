
from __future__ import print_function, division
import math
import turtle

def polyline(t, n, length, angle):

    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):

    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def internal_polygon(turtle,number_of_sides,length):
    angle=(number_of_sides-2)*180/number_of_sides
    radian = 360/number_of_sides*(math.pi/180)
    side=math.sqrt(length**2+length**2-(2*length*length*math.cos(radian)))
    for i in range(number_of_sides):
        turtle.fd(length)
        turtle.lt(180.0-angle/2) 
        turtle.fd(abs(side))
        turtle.lt(180.0-angle/2)
        turtle.fd(length)
        turtle.lt(180)
bob=turtle.Turtle()
internal_polygon(bob,7,100.0)
turtle.mainloop()

