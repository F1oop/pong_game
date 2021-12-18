from turtle import Turtle


class Layout(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()
        self.draw_middle_line()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score}          {self.r_score}", align="center", font=('Courier', 30, 'normal'))
        # self.score += 1

    def draw_middle_line(self):
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        while self.ycor() < 300:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=('Courier', 40, 'normal'))