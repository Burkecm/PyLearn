from turtle import Turtle
UPPER_BOUND = 250
LOWER_BOUND = -250

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.teleport(position, 0)
        self.color("white")
        self.shapesize(5, 1)

    def move_up(self):
        if self.ycor() < UPPER_BOUND:
            self.goto(self.xcor(), self.ycor()+10)

    def move_down(self):
        if self.ycor() > LOWER_BOUND:
            self.goto(self.xcor(), self.ycor()-10)