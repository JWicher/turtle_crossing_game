from turtle import Turtle

TURTLE_STEP = 20
STARTING_POSITION = (0, -280)
DIRECTION = {
    "UP": 90,
    "LEFT": 180,
    "RIGHT": 0
}

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(DIRECTION["UP"])
        self.goto(STARTING_POSITION)

    def move(self, direction_type):
        self.setheading(DIRECTION[direction_type])
        self.forward(TURTLE_STEP)

    def go_to_start(self):
        self.goto(STARTING_POSITION)