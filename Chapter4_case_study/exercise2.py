from __future__ import print_function, division

import math
import turtle


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    arc(t, r, 360)

def flower(turtle,radius,number_of_leaves):
    angle=360.0/number_of_leaves
    for i in range(number_of_leaves):
        arc(turtle,radius,angle)
        bob.lt(180-angle) 
        arc(turtle,radius,angle)
        bob.rt(angle/2)



bob = turtle.Turtle()
radius = 100
number_of_leaves=8
flower(bob,radius,number_of_leaves)
turtle.mainloop()