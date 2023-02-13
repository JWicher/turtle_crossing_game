from turtle import Turtle

y_position = 250

class Finishline(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-300, y_position)
        self.pendown()
        self.goto(300, y_position)
