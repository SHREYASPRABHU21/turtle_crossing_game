from turtle import *

class Tortoise(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(0,-180)
        self.left(90)

    def move_up(self):
        self.forward(15)