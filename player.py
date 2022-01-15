STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



from turtle import Turtle


def go_to_start(self):
    self.goto(STARTING_POSITION)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        go_to_start(self)
        self.setheading(90)
        self.level = 1
        self.score = 0
        self.highscore = 0


    def go_up(self):
        self.forward(MOVE_DISTANCE)

        self.score += 1


    def level_complete(self):
        if self.ycor() > FINISH_LINE_Y:
            go_to_start(self)
            self.level += 1

