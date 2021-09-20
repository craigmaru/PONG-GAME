from turtle import Turtle


UP = 20
DOWN = -20


# replace shortcut = CTRL + R
# width 20
# height = 100
# x_pos = 350
# y_pos = 0
# move up or down
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()  # connecting to the turtle class
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
