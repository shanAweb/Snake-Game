from turtle import Screen
import time


from snake import Snake
from food import Food
from scoreboard import Scoreboard

sleep_time = 0.1
# Screen creation
screen = Screen()
# canvas size to play game
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Snake control using keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Snake movement
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
        time.sleep(sleep_time - 0.02)

    # Detect collision with walls
    if snake.head.xcor() > 301 or snake.head.xcor() < -301 or snake.head.ycor() > 301 or snake.head.ycor() < -301:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.Segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()
