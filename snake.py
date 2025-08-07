from turtle import Turtle

# In Python, constants are either initialized with all capitals snake case
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.Segments = []
        self.create_snake()
        self.head = self.Segments[0]

    #     Method to create snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.Segments.append(new_segment)

    def extend(self):
        self.add_segment(self.Segments[-1].position())


    #         Method to move snake ahead
    def move(self):
        """ Logic here to avoid segments from getting separated and smooth turn is:
    Place the 3rd segment(turtle) at the place of 2nd and 2nd at the place of 1
    Move forward segment 1 by 20"""
        for new_seg in range(len(self.Segments) - 1, 0, -1):
            new_x = self.Segments[new_seg - 1].xcor()
            new_y = self.Segments[new_seg - 1].ycor()
            self.Segments[new_seg].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



