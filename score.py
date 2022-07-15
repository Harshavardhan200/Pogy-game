
from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.life1 = 3
        self.penup()
        self.color("white")
        self.hideturtle()
    def update_r(self):
        self.goto(-10, 240)
        self.write(f"{self.score1}", align="right", font=('Arial', 32, "normal"))
    def update_l(self):
        self.goto(10, 240)
        self.write(f"{self.score2}", align="left", font=('Arial', 32, "normal"))
    def r_paddle(self):
        self.clear()
        self.life1 -= 1
        self.score1 += 1
        self.clear()
        self.goto(-10, 240)
        self.write(f"{self.score1}", align="right", font=('Arial', 32, "normal"))
        self.goto(10, 240)
        self.write(f"{self.score2}", align="left", font=('Arial', 32, "normal"))
    def l_paddle(self):
        self.clear()
        self.life1 -= 1
        self.score2 += 1
        self.goto(10, 240)
        self.write(f"{self.score2}", align="left", font=('Arial', 32, "normal"))
        self.goto(-10, 240)
        self.write(f"{self.score1}", align="right", font=('Arial', 32, "normal"))
    def score(self):
        self.goto(-200, 240)
        self.clear()
        self.write(f' {self.life1}', align="left", font=('Arial', 32, "normal"))
    def game_over(self):

        self.goto(-100, 0)
        if self.score1 > self.score2:
            self.write(f"Player 1 win the game", align="left", font=('Arial', 32, "normal"))
        else:
            self.write(f"Player 2 is win the game", align="left", font=('Arial', 32, "normal"))