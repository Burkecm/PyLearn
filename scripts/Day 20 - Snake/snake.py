from turtle import Turtle
SEGMENT_SIZE = 20
HEADING_LEFT = 180
HEADING_RIGHT = 0
HEADING_UP = 90
HEADING_DOWN = 270
class Snake:
    def __init__(self, length = 3):
        self.body = []
        for i in range(0, length+1):
            self.body.append(self.new_segment(0-(SEGMENT_SIZE*i), 0))
        # self.body = [self.new_segment(0, 0), self.new_segment(-SEGMENT_SIZE, 0), self.new_segment(-2*SEGMENT_SIZE, 0)]
        self.head = self.body[0]

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

