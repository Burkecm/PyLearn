from turtle import Turtle
FONT = ("Courier", 12, "normal")
class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.game_level = 1
        self.teleport(-280, 280)
        self.write(arg=f"Level: {self.game_level}", move=False, align="left", font=FONT)

    def next_level(self):
        self.game_level += 1
        self.clear()
        self.write(arg=f"Level: {self.game_level}", move=False, align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.teleport(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="left", font=FONT)
    