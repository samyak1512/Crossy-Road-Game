FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('Black')

    def draw_score_level(self,level,score):
        self.clear()
        self.penup()
        self.goto(-280,250)
        self.pendown()
        self.write(f'Level:{level}              Score:{score}', align='left', font=FONT)


    def game_over(self):
        self.penup()
        self.goto(0 , 0)
        self.pendown()
        self.write('GAME OVER', align='center', font=FONT)