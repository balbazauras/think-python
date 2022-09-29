import math

class Circle:
    def __init__(self,center,radius):
        self.center=center
        self.radius=radius

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Rectangle:
    def __init__(self,width, height, corner):
        self.width=width
        self.height=height
        self.corner=corner

def point_in_circle(circle,point):
    '''
    function return True if point is on circle or inside circle
    '''
    h=circle.center.x 
    k=circle.center.y
    if(point.x-h)**2+(point.y-k)**2 == circle.radius**2: 
        return True
    elif math.sqrt((point.x-h)**2+(point.y-k)**2 )<circle.radius:
        return True
    else: 
        return False
    
def rect_in_circle(circle,rectangle):
    '''
    function returns True if all 4 rectangle corners are in circle
    '''
    for point in get_rectangle_points(rectangle):
        #print ("x: "+str(point.x)+" y:"+ str(point.y) )
        if not point_in_circle(circle,point):
            return False
    return True

def get_rectangle_points(rectangle):
    '''
    function adds all 4 corner coordinates to list
    '''
    # setting variables for rectangle
    x=rectangle.corner.x 
    y=rectangle.corner.y
    w=rectangle.width
    h=rectangle.height
    points_to_check=list()
    # adding rectangle corners to list
    points_to_check.append(Point(x,y))
    points_to_check.append(Point(x,y+h))
    points_to_check.append(Point(x+w,y+h))
    
    points_to_check.append(Point(x+w,y))
    
    return points_to_check


def rect_circle_overlap(circle,rectangle):
    '''
    function returns True if at least one point of rectangle is in circle
    '''
    for point in get_rectangle_points(rectangle):
        # print ("x: "+str(point.x)+" y:"+ str(point.y) )
        if not point_in_circle(circle,point): 
            return True
    return False
def main():
    circle_point=Point(150,100) # set circle center point
    circle=Circle(circle_point,75) # set circle point and radius
    rectangle_point=Point(150,100) #lower left rectangle point
    rectangle=Rectangle(10,10,rectangle_point) # width, height, corner point
    point_to_check=Point(4,4) # coordantes of a point which needs to be checked
    
    print ("Point is in circle: "+str(point_in_circle(circle,point_to_check)))
    print ("Atleast 1 corner of rectangle is in circle: "+str(rect_in_circle(circle,rectangle)))
    print ("Are all 4 corners of rectangle in circle: "+str(rect_in_circle(circle,rectangle)))

if __name__ == '__main__':
    main()



