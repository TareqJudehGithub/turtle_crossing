from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 300


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.go_to_start()
        self.left(90)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(0, new_y)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)

