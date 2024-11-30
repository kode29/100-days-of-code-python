import turtle as t
import random
import colorgram

# Parameters
grid_size = 10
spaces_between = 50
dot_size = 20

tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed(0)
t.colormode(255)

colors = colorgram.extract("image.jpg", 50)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

screen = t.Screen()

tim.penup()
start_x = -(screen.window_width()/4)
start_y = -(screen.window_height()/4)
tim.setposition(start_x, start_y)

for _ in range(grid_size):
    for _ in range(grid_size):
        tim.dot(dot_size, random.choice(rgb_colors))
        tim.forward(spaces_between)
    start_y += spaces_between
    tim.setposition(start_x, start_y)

screen.exitonclick()