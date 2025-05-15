from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.penup()
        self.goto(0, 270)
        self.update_board()
        self.hideturtle()

    def update_board(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gain_score(self):
        self.score += 1
        self.clear()
        self.update_board()

    def game_over(self):
        self.clear()
        self.write(arg=f"Game Over! Final Score: {self.score}", align=ALIGNMENT, font=FONT)
