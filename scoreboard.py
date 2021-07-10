from turtle import Turtle

ALIGNMENT = "center"

FONT = ("courier", 30, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.game_scores = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, 250)
        self.display_score()

    def game_score(self):
        self.game_scores += 1
        self.clear()
        self.display_score()

    def display_score(self):
        self.write(arg=f"Score = {self.game_scores}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg=f"GAME OVER,final score is {self.game_scores}", align="center", font=FONT)