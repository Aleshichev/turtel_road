import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:  #  столкновене с машинами
        if car.distance(player) < 22:
            game_is_on = False
            scoreboard.game_over()


    if player.is_at_finish_line():
        player.gotostart()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()