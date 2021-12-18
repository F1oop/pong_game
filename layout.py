from turtle import Turtle


class Layout(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.color("White")
        self.draw_middle_line()
        self.update_score()
        self.hideturtle()

    def draw_middle_line(self):
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        while self.ycor() < 300:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"{self.l_score}          {self.r_score}", align="center", font=('Courier', 20, 'normal'))

    def increase_score(self, player):
        if player == "left_player":
            self.l_score += 1
        if player == "right_player":
            self.r_score += 1
        self.update_score()
        if self.l_score or self.r_score == 3:
            self.game_over(player)
            return False
        return True

    def game_over(self, player):
        self.goto(0, 0)
        self.write(f"Game Over, {player} won", align="center", font=('Courier', 40, 'normal'))
