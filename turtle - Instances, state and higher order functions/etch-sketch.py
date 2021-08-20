from turtle import Turtle, Screen 
tim = Turtle()
screen = Screen()

def forward():
    tim.fd(10)
def backward():
    tim.backward(10)
def right():
    tim.right(10)
def left():
    tim.left(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkeypress(clear,"c")
screen.onkeypress(forward,"w")
screen.onkeypress(backward,"s")
screen.onkeypress(left,"a")
screen.onkeypress(right,"d")

screen.exitonclick()