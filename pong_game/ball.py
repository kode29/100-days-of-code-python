from turtle import  Turtle

class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.circle(5)
        self.setpos(0,0)
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + 1
        new_y = self.ycor() + 1
        self.goto(new_x, new_y)