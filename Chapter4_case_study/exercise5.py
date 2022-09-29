import turtle
SPACE_BETWEEN_COILS= 0.0002
INITIAL_COIL_SPACCING= 0.1

def draw_spiral(t, steps, length, a, b):
    theta = 0.0
    for i in range(steps):
        t.fd(length)
        dtheta = 1 / (a + b * theta)
        t.lt(dtheta)
        theta += dtheta


bob = turtle.Turtle()
draw_spiral(bob, 100,INITIAL_COIL_SPACCING,SPACE_BETWEEN_COILS)
turtle.mainloop()