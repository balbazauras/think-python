
import turtle
import math
bob=turtle.Turtle()

radius=50
number_of_sides=360
circumference=2*math.pi*radius
length_of_circle_sides=circumference/number_of_sides
angle=90
def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(turtle,length,n):
    angle=360.0/n
    polyline(turtle,n,length,angle)

def polyline(turtle,n,length,angle):
    for i in range(n):
        turtle.fd(length)
        turtle.lt(angle)

def circle(turtle,radius):
    arc(turtle,360,radius)


def arc(turtle,angle,radius):
    arc_length=2*math.pi*radius*angle/360
    n=int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=float(angle)/n
    polyline(turtle,n,step_length,step_angle)

#arc(bob,90,50)
#circle(bob,radius)


#exercise 1
counter=0
def draw(t, length, n):
    +(+counter)
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)
draw(bob,100,5)
turtle.mainloop()
print(counter)

