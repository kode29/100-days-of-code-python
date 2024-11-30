import turtle as t
import random

timmy = t.Turtle()
timmy.pensize(15)
timmy.speed(10)
t.colormode(255)

def rand_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

def move_turtle():
    timmy.pencolor(rand_rgb())
    timmy.forward(30)
    angles = [0, 90, 180, 270]
    timmy.setheading(random.choice(angles))

for _ in range(200):
    move_turtle()

screen = t.Screen()
screen.exitonclick()