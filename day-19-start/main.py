from turtle import Turtle, Screen
import random

is_race_running = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
start_x = -230
start_y = -75

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(start_x, start_y)
    start_y += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_running = True

while is_race_running:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_running = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You lose. The {winning_color} turtle is the winner")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()