from turtle import Turtle

ALIGNMENT = "center"

FONT = ("courier", 30, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.game_scores = 0
        with open("data.txt") as highscore:
            high_score = int(highscore.read())
        self.high_score = high_score
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, 250)
        self.display_score()

    def game_score(self):
        self.game_scores += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"Score = {self.game_scores} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.game_scores > self.high_score:
            self.high_score = self.game_scores
            with open("data.txt", mode="w") as highscore:
                highscore.write(str(self.high_score))
        self.game_scores = 0
        self.display_score()
