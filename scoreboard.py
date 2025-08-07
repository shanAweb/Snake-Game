from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color('white')
        self.goto(0, 250)
        self.write(f"Score : {self.score}", align='center', font=('Courier', 18, 'bold'))
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align='center', font=('Arial', 18, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align='center', font=('Arial', 18, 'bold'))




