from turtle import Turtle
class Setup(Turtle):
    def __init__(self, xco):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setx(xco)
        self.color("white")
    def up(self):
        t = self
        y = self.ycor()
        y += 20
        t.sety(y)
    def down(self):
        t = self
        y = t.ycor()
        y -= 20
        t.sety(y)

