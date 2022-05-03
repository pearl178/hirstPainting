from turtle import Turtle, Screen
import random

screen = Screen()
turtle = Turtle()


def hirst_painting():
    color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]

    turtle.pu()
    turtle.setheading(0)
    screen.screensize(600, 600)
    # turtle.goto(-300, -300)
    n = 0
    roll = 0
    while n < 10 and roll < 10:
        n += 1
        turtle.fd(50)
        screen.colormode(255)
        turtle.dot(20, random.choice(color_list))
        turtle.fd(50)
        if n == 10:
            n = 0
            current_heading = turtle.heading()
            turtle.setheading(90)
            turtle.forward(50)
            new_heading = current_heading+180
            turtle.setheading(new_heading)
            roll += 1


turtle.setheading(200)
turtle.pu()
turtle.hideturtle()
turtle.forward(600)
turtle.speed('fastest')
hirst_painting()
screen.exitonclick()


