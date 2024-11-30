from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier New", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0,275)
        self.color("white")
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)