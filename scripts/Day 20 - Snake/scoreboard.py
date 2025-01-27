from turtle import Turtle
XPOS = 0
YPOS = 100
FONT = ("Courier", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.teleport(XPOS, YPOS)
        self.write(f"Score: {self.score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", font=("Arial", 20, "normal"))

    def game_over(self):
        self.teleport(-50, 0)
        self.write(f"GAME OVER", font=("Arial", 20, "normal"))