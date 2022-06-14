import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

turtle = Player()
screen = Screen()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

screen.listen()
screen.onkey(turtle.go_up, "Up")
screen.onkey(turtle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.finish_line():
        turtle.starting_pos()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()