from turtle import Screen
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard
import time

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
window = Screen()
window.title("Snake Game")
window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
window.bgcolor("black")
window.tracer(0)
snake = Snake()
food = Food()
score_board = ScoreBoard()
window.listen()
window.onkey(fun=snake.up, key="Up")
window.onkey(fun=snake.down, key="Down")
window.onkey(fun=snake.left, key="Left")
window.onkey(fun=snake.right, key="Right")
while not snake.is_game_over():
    window.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.gain_score()
        snake.grow()
    if snake.is_game_over():
        score_board.game_over()
window.exitonclick()
