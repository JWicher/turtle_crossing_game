from turtle import Turtle

FONT = ('Courier', 30, 'normal')
ALIGN = 'center'

class Message(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def show(self, message):
        self.write(message, align=ALIGN, font=FONT)
