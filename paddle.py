from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=.5, stretch_len=5)
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(position, 0)

    def move_up(self):
        self.forward(15)

    def move_down(self):
        self.backward(15)
