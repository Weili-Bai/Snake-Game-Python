from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_initial_snake()
        self.head = self.segments[0]

    def create_initial_snake(self):
        for pos in INITIAL_POSITIONS:
            self.add_segment(pos)

    def move(self):
        length = len(self.segments)
        for i in range(length - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(STEP)

    def up(self):
        direction = int(self.head.heading())
        if direction != DOWN:
            self.head.setheading(UP)

    def down(self):
        direction = int(self.head.heading())
        if direction != UP:
            self.head.setheading(DOWN)

    def left(self):
        direction = int(self.head.heading())
        if direction != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        direction = int(self.head.heading())
        if direction != LEFT:
            self.head.setheading(RIGHT)

    def is_hit_wall(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if x > 280 or x < -280 or y > 280 or y < -280:
            return True
        return False

    def add_segment(self, pos):
        curr = Turtle()
        curr.penup()
        curr.color("white")
        curr.goto(pos[0], pos[1])
        curr.shape("square")
        self.segments.append(curr)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def is_hit_body(self):
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                return True
        return False

    def is_game_over(self):
        return self.is_hit_body() or self.is_hit_wall()
