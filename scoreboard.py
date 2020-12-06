from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_leve(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 260)
        self.color("red")
        self.pendown()
        self.write("Game Over!", align="center", font=("Courier", 20, "bold"))
