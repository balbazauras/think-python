import turtle
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from exercise1 import Rectangle,Point,Circle,get_rectangle_points
from Chapter4_case_study.exercise4 import arc
def draw_rect(turle, rectangle):
    '''
    turle- turtle instance
    rectangle- rectangle instance
    functions draws a rectangle
    '''
    
    move_to_point(turle,rectangle.corner.x,rectangle.corner.y) # move to starting corner
    for point in get_rectangle_points(rectangle): # iterates through point list
        turle.goto(point.x,point.y) # move to following point
    turle.goto(rectangle.corner.x,rectangle.corner.y) # get back to starting position


def draw_circle(turle,circle):
    arc(turle,360,circle.radius)

def move_to_point(turle,x,y):
    '''
    goes to point without drawing lines
    '''
    turle.penup()# dont draw line
    turle.goto(x,y)# travel to point
    turle.pendown() #draw line



def main():
    rectangle_corner=Point(50,50) # rectangle's lower left corner
    rectangle=Rectangle(100,200,rectangle_corner) # rectangle's width, height, corner
    circle_center=Point(50,50) # circle center x and y coordinates
    circle=Circle(circle_center,50)# circle center, radius 
    bob=turtle.Turtle() # turtle instance
    bob.speed(2) # adjust turle speed
    draw_rect(bob,rectangle)
    draw_circle(bob,circle)
    turtle.mainloop() #dosen't allow window to close automatically 

if __name__ == '__main__':
    main()
