from turtle import *
from tortoise import *
from cars import *
from levels import *
import time

screen = Screen()
screen.setup(width= 600,height= 400)
screen.tracer(0)
screen.listen()

tortoise = Tortoise()
levels = Levels()
cars = Cars()
x = 300

while x >-300:

    cars.row_cars(x)
    x -= 30
speed = 0.8
screen.onkey(tortoise.move_up,"w")

game_is_on = True

while game_is_on:
    screen.update()
    # time.sleep(speed)
    if levels.level == 1:
        time.sleep(speed)
    x -= 100
    if x <= -300:
        x = -340
    cars.row_cars(x)
    cars.move_car()
    for car in cars.cars:
        if tortoise.distance(car) < 15:
            levels.game_over()
            game_is_on = False

    if tortoise.ycor() >180:
        levels.level_update()
        tortoise.goto(0,-180)
        time.sleep(speed * 0.8)
































screen.exitonclick()