from turtle import Turtle

FINISH_LINE = 280
STARTING_LINE =  -280

class Player(Turtle):
    def __init__(self, shape = "turtle"):
        super().__init__(shape)
        self.setheading(90)
        self.penup()
        self.sety(STARTING_LINE)
        self.level = 1
            
    def move(self):
        self.forward(10)

    def next_level(self):
        self.level += 1
        self.sety(STARTING_LINE)
