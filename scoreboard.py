from turtle import  Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x = -220 , y =250)#x = -220, y = 250
        self.update_score()


    def update_score(self):
        self.clear()
        self.level += 1
        self.write(  arg = f"Level: {self.level}",   align='center', font =   FONT)

    def victory(self):
        if self.level > 5:
            self.goto(0, 0)
            self.penup()
            self.hideturtle()
            self.write("victory", align='center', font=FONT)
            return False
        return True

    def loss(self):
        self.goto(0,0)
        self.penup()
        self.hideturtle()
        self.write("Game Over!", align='center' ,font =   FONT)

