from turtle import Screen
from paddle import Paddle
from layout import Layout

screen = Screen()
layout = Layout()
r_paddle = Paddle(350)
l_paddle = Paddle(-350)

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

screen.exitonclick()