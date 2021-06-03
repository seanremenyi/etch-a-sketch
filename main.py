from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)


def rotate_right():
    tim.right(25)


def move_backwards():
    tim.backward(20)


def rotate_left():
    tim.left(25)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_right)
screen.onkey(key="d", fun=rotate_left)
screen.exitonclick()
