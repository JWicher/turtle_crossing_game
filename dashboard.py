from turtle import Turtle

FONT = ('Courier', 30, 'normal')
ALIGN = 'center'

class Dashboard(Turtle):

    def __init__(self):
        super().__init__()
        self.wins = 0
        self.losses = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Wins: {self.wins} Losses: {self.losses}", align=ALIGN, font=FONT)

    def player_wins(self):
        self.wins += 1
        self.update_score()

    def player_lost(self):
        self.losses += 1
        self.update_score()
