from turtle import Turtle


class MiddleLine(Turtle):

    def __init__(self):
        super().__init__()  # connecting to the turtle class
        self.color("white")
        self.hideturtle()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0, -295)
        self.setheading(90)
        self.line()

    def line(self):
        for i in range(15):
            self.pensize(5)
            self.forward(30)
            self.penup()
            self.forward(30)
            self.pendown()
