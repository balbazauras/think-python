import math
import turtle
def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)
# Exercise 5
bob=turtle.Turtle()
def koch(turtle,x):
    arc(turtle,x/3,40)
    turtle.lt(60)
    koch(turtle,x/3)
    turtle.lt(120/3)
    koch(turtle,x/3)
    turtle.lt(60)
    koch(turtle,x/3)
    if( x<3):
        turtle.fd(x)
koch(bob,400)
turtle.mainloop()
