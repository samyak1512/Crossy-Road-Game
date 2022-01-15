from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5




class CarManager:

    def __init__(self):
        self.all_cars = []
        self.MOVE_INCREMENT = 10

    def create_cars(self):
        random_delay = random.randint(1, 6)
        if random_delay == 1:

            new_car = Turtle('square')
            new_car.penup()
            random_color = random.choice(COLORS)
            new_car.color(random_color)
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)



    def move_cars(self):
        for new_car in self.all_cars :
            new_car.backward(self.MOVE_INCREMENT)



