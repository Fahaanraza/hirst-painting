from turtle import Turtle, Screen, pendown
import random
import turtle
dino = Turtle()
dino.hideturtle()
dino.speed("fastest")
dino.penup()
dino.setposition(-200, -200)
turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


for i in range(5):
    for i in range(10):
        dino.pencolor(random_colour())
        dino.dot(20)
        dino.fd(50)
    dino.right(270)
    dino.fd(50)
    dino.right(270)
    dino.fd(50)
    for i in range(10):
        dino.pencolor(random_colour())
        dino.dot(20)
        dino.fd(50)
    dino.right(90)
    dino.fd(50)
    dino.right(90)
    dino.fd(50)
screen = Screen()
screen.exitonclick()
