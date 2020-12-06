import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Instances:
screen = Screen()
player = Player()
cars = CarManager()

# Page setup:
screen.setup(width=600, height=600)
screen.tracer(0)

# Player movements:
screen.listen()
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # Detect collision with car

