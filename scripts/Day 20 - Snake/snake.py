from turtle import Turtle
SEGMENT_SIZE = 20
HEADING_LEFT = 180
HEADING_RIGHT = 0
HEADING_UP = 90
HEADING_DOWN = 270
DEFAULT_LENGTH = 3

class Snake:
    def __init__(self, length = DEFAULT_LENGTH):
        self.body = []
        self.make_snake(length)
        self.head = self.body[0]

    def make_snake(self, length):
        for i in range(0, length+1):
            self.body.append(self.new_segment(0-(SEGMENT_SIZE*i), 0))

    def new_segment(self, x, y):
        segment = Turtle("square")
        segment.color("white")
        segment.teleport(x, y)
        segment.penup()
        return segment
    
    def grow(self):
        self.body.append(self.new_segment(self.body[-1].xcor(), self.body[-1].ycor()))

    def left(self):
        if self.head.heading() != HEADING_RIGHT:
            self.head.setheading(HEADING_LEFT)   

    def right(self):
        if self.head.heading() != HEADING_LEFT:
            self.head.setheading(HEADING_RIGHT)

    def up(self):
        if self.head.heading() != HEADING_DOWN:
            self.head.setheading(HEADING_UP)

    def down(self):
        if self.head.heading() != HEADING_UP:
            self.head.setheading(HEADING_DOWN)

    def move_forward(self):
        for segment in range(len(self.body)-1, 0, -1):
            x = self.body[segment-1].xcor()
            y = self.body[segment-1].ycor()
            self.body[segment].goto(x, y)
        self.body[0].forward(SEGMENT_SIZE)

    def reset(self, length=DEFAULT_LENGTH):
        for segment in self.body:
            segment.hideturtle()
        self.body.clear()
        self.make_snake(length)
        self.head = self.body[0]