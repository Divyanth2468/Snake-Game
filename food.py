from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        # We are inheriting the turtle class attributes and methods into the Food class
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def new_food(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))