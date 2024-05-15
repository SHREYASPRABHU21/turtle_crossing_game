from turtle import *
from random import *
from tortoise import *



steps = 20
colors = ["black","red","orange","blue","green","yellow"]

class Cars():
    def __init__(self):
        super().__init__()
        self.steps = 20
        self.cars = []

    def generate_cars(self,cor):
        self.car = Turtle()
        self.car.shape("square")
        self.car.shapesize(stretch_wid=1, stretch_len=1.5)
        self.car.color(choice(colors))
        self.car.penup()
        self.car.goto(cor)
        self.cars.append(self.car)
    # def row_cars(self):
    #     y = -120
    #     inc = 0
    #     while y < 140:
    #         for i in range(10):
    #     #             x = randint(-480,280)
    #     #             y = -120 + inc
    #     #             cor = (x,y)
    #     #             self.generate_cars(cor)
    #         inc += 30

    def move_car(self):

        for car in self.cars:
            car.forward(20)


    def row_cars(self,x):
        y = randint(-140,140)
        new_x = randint(x-200,x)
        cor = (new_x,y)
        self.generate_cars(cor)

        # x = 300 - 270
        # x = -170 -> 170

