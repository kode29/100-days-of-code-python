import turtle as t
import random

timmy = t.Turtle()
timmy.speed(0)
t.colormode(255)

def rand_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

def draw_spirograph(gap):
    max = int(360 / gap)
    for angle in range(max):
        timmy.color(rand_rgb())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)

draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()