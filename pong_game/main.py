from turtle import Turtle, Screen

# Set up the screen
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Turtle()
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.setpos(350, 0)
right_paddle.color("white")
right_paddle.penup()

def go_up():
    new_y = right_paddle.ycor()+20
    right_paddle.goto(right_paddle.xcor(), new_y)

def go_down():
    new_y = right_paddle.ycor()-20
    right_paddle.goto(right_paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_running = True
while game_is_running:
    screen.update()

screen.exitonclick()
