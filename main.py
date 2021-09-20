from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import MiddleLine
import time

# TODO create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("MARU PONG")
screen.tracer(0)

# TODO tennis court line
line = MiddleLine()

# TODO create and move a paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# TODO create the ball and make it move
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, key="w")
screen.onkey(l_paddle.go_down, key="s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # TODO detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO detect collision  with paddle and bounce back
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # TODO detect when paddle misses ball
    # Right Paddle Miss
    if ball.xcor() > 380:
        ball.reset_position()
        # TODO keep score
        scoreboard.l_point()

    # Left Paddle Miss
    if ball.xcor() < -380:
        ball.reset_position()
        # TODO keep score
        scoreboard.r_point()


screen.exitonclick()
