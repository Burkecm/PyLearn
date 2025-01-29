from turtle import Turtle
XPOS = -100
YPOS = 100
FONT = ("Courier", 12, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_high_score()
        self.hideturtle()
        self.color("white")
        self.teleport(XPOS, YPOS)
        self.update()
        
        # self.write(f"Score: {self.score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score: {self.high_score}", font=FONT)

    def reset(self):
        self.high_score = self.score if self.score > self.high_score else self.high_score
        self.score = 0
        with open("scripts\Day 20 - Snake\highscore.txt", "w") as hs:
            hs.write(str(self.high_score))
        self.update()

    def read_high_score(self):
        with open("scripts\Day 20 - Snake\highscore.txt") as hs:
            self.high_score = int(hs.read())

    # Deprecated
    def game_over(self):
        self.teleport(-50, 0)
        self.write(f"GAME OVER", font=FONT)
