from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300


screen = Screen()
screen.setup(SCREEN_WIDTH*2, SCREEN_HEIGHT*2)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.update()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Run while game is on
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # Detect collision with Food
    if snake.head.distance(food) < 15:
        scoreboard.increase()
        snake.extend()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() < -SCREEN_WIDTH+20 or \
        snake.head.xcor() > SCREEN_WIDTH - 20 or \
        snake.head.ycor() < -SCREEN_HEIGHT + 20 or \
        snake.head.ycor() > SCREEN_WIDTH - 20:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()