import turtle


def draw_spiral(t, steps, length=3, a=0.1, b=0.0002):
    theta = 0.0
    for i in range(steps):
        t.fd(length)
        dtheta = 1 / (a + b * theta)
        t.lt(dtheta)
        theta += dtheta


bob = turtle.Turtle()
draw_spiral(bob, 100)
turtle.mainloop()