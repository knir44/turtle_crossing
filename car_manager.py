from turtle import  Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 6
MOVE_INCREMENT = 0.2

class CarManager(Turtle):


    def __init__(self):

        super().__init__()
        self.shape("square")
        self.penup()
        yCor = random.randrange(-240,260,30)
        xCor = random.randint(300,320)
        self.goto(x=xCor, y=yCor)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)

    def move_for(self):
        self.forward(STARTING_MOVE_DISTANCE)


    def increase_movement(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE +=MOVE_INCREMENT

