from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

heading = 0

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_clockwise():
    tim.setheading(tim.heading()+10)

def rotate_counterclockwise():
    tim.setheading(tim.heading() - 10)

def clear_screen():
    tim.clear()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(rotate_clockwise, "a")
screen.onkey(rotate_counterclockwise, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()