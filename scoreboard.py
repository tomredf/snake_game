from turtle import Turtle
ALIGN = "center"
FONT = ("courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, ALIGN, FONT)

    def set_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
