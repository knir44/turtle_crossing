import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle-Crossing")

scoreboard = Scoreboard()
player = Player()

#press_keys
screen.listen()
screen.onkeypress(fun = player.move_up,key = "Up")
screen.onkeypress(fun = player.move_up,key = "w")
screen.onkeypress(fun = player.move_down,key = "Down")
screen.onkeypress(fun = player.move_down,key = "s")

car_list = []
level_list = [10,8,6,4,2]
level = 0
counter = 0

#verifying the turtle doesn't tough any car
def game_over():
    global counter
    if not (counter % level_list[level]):
        car = CarManager()
        car_list.append(car)

    for any_car in car_list:
        if player.distance(any_car) < 30:
            return False
        any_car.move_for()

    counter += 2
    return True

#moving forward to the next level
def next_level():
    global  level
    player.reset_position()
    level += 1
    scoreboard.update_score()
    for any_car in car_list:
        any_car.increase_movement()

#making the first cars before the game
def first_show():
    pivot = 2
    for start in range(1,100):
        if not pivot % start:
            car = CarManager()
            car_list.append(car)


first_show()
game_is_on = True

while game_is_on:


    if player.level_up():
        next_level()

    game_is_on = game_over() and scoreboard.victory()

    time.sleep(0.1)
    screen.update()


if scoreboard.level < 5:
    scoreboard.loss()


screen.exitonclick()