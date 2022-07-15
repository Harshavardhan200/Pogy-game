import time
from turtle import Screen
from setup import Setup
from BALL import Ball
from score import Score
def game():
    sc = Screen()
    sc.setup(800, 600)
    sc.bgcolor("black")
    r_paddle = Setup(380)
    l_paddle = Setup(-380)
    sc.listen()
    sc.onkey(r_paddle.up, "Up")
    sc.onkey(r_paddle.down, "Down")
    sc.onkey(l_paddle.up, "W")
    sc.onkey(l_paddle.down, "S")
    lives = 2
    sco = Score()
    b = Ball()
    w = 1
    sco.score()
    sco.update_l()
    sco.update_r()
    while w:
        # time.sleep(0.1)
        b.move()
        if b.ycor() > 240:
            b.bounce_back()
            b.speed('fastest')
        elif b.ycor() < -240:
            b.bounce_back()
            b.speed('fastest')
        elif b.distance(r_paddle) < 50 and b.xcor() > 280 or b.distance(l_paddle) < 50 and b.xcor() < -280:
            b.bounce_down()
            b.speed('fastest')
        else:
            sco.update_l()
            sco.update_r()
        if b.xcor() == 400:
            sco.r_paddle()
            b.reset()
            sco.clear()
            # sco.color('black')
            sco.score()
        if b.xcor() == -400:
            sco.l_paddle()
            if lives:
                lives -= 1
                b.reset()
                sco.clear()
                sco.score()

        if sco.life1 == 0:
            sc.clear()
            sc.bgcolor('black')
            sco.game_over()
            break
    sc.exitonclick()
game()