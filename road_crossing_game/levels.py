from turtle import *

class Levels(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color("black")
        self.hideturtle()
        self.level_update()


    def level_update(self):
        self.clear()
        self.goto(-280,160)
        self.level += 1
        self.write(f"Level: {self.level}",font=("Arial",20,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.hideturtle()
        self.penup()
        self.write("Game Over.")