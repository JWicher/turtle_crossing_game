from turtle import Turtle
import random

COLORS = ['red', 'blue', 'yellow', 'green', 'grey', 'black']
DIRECTION = {
    "LEFT": 180,
}

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=2)
        self.penup()
        self.starting_y_position = 0
        self.move_step = 0

        self.set_speed()
        self.set_color()
        self.setheading(DIRECTION["LEFT"])

    def set_position(self, starting_x_position, starting_y_position):
        self.starting_y_position = starting_y_position
        self.goto(starting_x_position, starting_y_position)

    def set_speed(self):
        self.move_step = random.randrange(10, 21, 5)

    def set_color(self):
        self.color(random.choice(COLORS))

    def move(self):
        self.forward(self.move_step)

    def back_to_edge(self):
        random_x_position = random.randrange(300, 360, 10)
        self.goto(random_x_position, self.starting_y_position)
        self.set_speed()
        self.set_color()

