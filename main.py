from turtle import Screen
from paddle import Paddle
from layout import Layout
from ball import Ball
import time

screen = Screen()
layout = Layout()
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
game_is_live = True
number_of_collisions = 0

screen.setup(height=600, width=800)
screen.bgcolor("red")
screen.title("Pong")
screen.listen()
screen.tracer(0)
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

while game_is_live:
    screen.update()
    time.sleep(.1)
    ball.ball_move()

#     check for collision with paddle
    if (ball.distance(l_paddle) <= 50 and ball.xcor() < -345) or (ball.distance(r_paddle) <= 50 and ball.xcor() > 345):
        number_of_collisions += 1
        ball.change_direction(number_of_collisions)

#     check for collisions with horizontal walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.change_direction(number_of_collisions)

#     check for collisions with vertical walls
    if ball.xcor() >= 390:
        game_is_live = layout.increase_score("left_player")
        ball.ball_reset()
        l_paddle.paddle_reset(-350)
    if ball.xcor() <= -390:
        game_is_live = layout.increase_score("right_player")
        ball.ball_reset()
        r_paddle.paddle_reset(350)

screen.exitonclick()