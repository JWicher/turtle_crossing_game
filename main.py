from turtle import Screen
import time

from player import Player
from traffic import Traffic
from message import Message
from dashboard import Dashboard
from finish_line import Finishline

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)

player = Player()
traffic = Traffic()
message = Message()
dashboard = Dashboard()
finish_line = Finishline()

screen.listen()
screen.onkeypress(lambda: player.move("UP"), "Up")
screen.onkeypress(lambda: player.move("LEFT"), "Left")
screen.onkeypress(lambda: player.move("RIGHT"), "Right")

game_is_on = True

def game_restart():
    time.sleep(0.5)
    player.go_to_start()
    message.clear()

while game_is_on:
    time.sleep(0.1)
    traffic.move_cars()
    screen.update()

    if player.ycor() > 260:
        message.show('You win!')
        dashboard.player_wins()
        game_restart()

    if traffic.turtle_collision(player):
        message.show("You lost")
        dashboard.player_lost()
        game_restart()

screen.exitonclick()
