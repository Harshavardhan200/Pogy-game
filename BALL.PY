from turtle import Turtle
# import pogy
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("white")
        self.x = 10
        self.y = 10
    def move(self):
        self.goto(self.xcor()+self.x, self.ycor()+self.y)
    def bounce_back(self):
        self.y *= -1
    def bounce_down(self):
        self.x *= -1
    def reset(self):
        self.goto(0, 0)