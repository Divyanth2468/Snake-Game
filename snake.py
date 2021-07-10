from turtle import Turtle

CORDS = [0, -20, 20]

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in CORDS:
            self.add_segment(position)

    def add_segment(self, position):
        timmy = Turtle("square")
        timmy.penup()
        timmy.color("white")
        timmy.setx(position)
        self.segments.append(timmy)

    def extend(self):
        # Add a new segment to the snake
        self.add_segment(self.segments[-1].xcor())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].pos())
        self.head.forward(MOVE_DISTANCE)