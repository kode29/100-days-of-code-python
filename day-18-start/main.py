from turtle import Turtle, Screen
import random

timmy = Turtle()

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

def draw_shape(num_sides):
    tup = (random.randint(0, 255)/255, random.randint(0, 255)/255, random.randint(0, 255)/255)
    timmy.pencolor(tup)
    for _ in range(num_sides):
        angle = 360 / num_sides
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)


# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

screen = Screen()
# print(screen.colormode())
screen.exitonclick()