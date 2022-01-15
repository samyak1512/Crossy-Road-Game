import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_manager = CarManager()

pen = Scoreboard()


screen.listen()
screen.onkey(player.go_up,'Up')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()
    player.level_complete()
    pen.draw_score_level(player.level,player.score)
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            pen.game_over()
            game_is_on = False




    car_manager.MOVE_INCREMENT = ((player.level-1)*5)+10

screen.exitonclick()