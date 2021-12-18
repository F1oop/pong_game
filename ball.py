from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(.5, .5)
        self.penup()
        self.dx = 10
        self.dy = 10
        self.m = 1

    def ball_move(self):
        self.goto(self.xcor() + self.dx * self.m, self.ycor() + self.dy * self.m)

    def change_direction(self, num_of_col):
        self.m = self.m + num_of_col * 0.01
        if self.xcor() >= 350:
            self.dx = -10
        elif self.xcor() <= -350:
            self.dx = 10

        if self.ycor() >= 270:
            self.dy = -10
        elif self.ycor() <= -270:
            self.dy = 10

    def ball_reset(self):
        self.goto(0, 0)
