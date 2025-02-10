from turtle import Turtle
FONT = ("Courier", 80, "normal")
class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.pencolor("white")
        self.penup()
        self.p1_score = 0
        self.p2_score = 0
        self.update()

    def increment_p1_score(self):
        self.p1_score += 1
        self.update()

    def increment_p2_score(self):
        self.p2_score += 1
        self.update()


    def update(self):
        self.clear()
        self.teleport(-100, 200)
        self.write(self.p1_score, align="right", font=FONT)
        self.teleport(100, 200)
        self.write(self.p2_score, align="left", font=FONT)
