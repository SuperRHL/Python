from turtle import Turtle, Screen 
import random
screen = Screen()
screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title = 'make your bet',prompt = 'which turtle will win')
colors=["red","orange","yellow","green","blue","purple"]

is_race_on=False
all_turtle=[]

y=-180
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y)
    y+=30
    all_turtle.append(new_turtle)

if user_bet: is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:print(f"You have won, The {winning_color} turtle is the winner")
            else:print(f"You have lost, The {winning_color} turtle is the winner")
        turtle.forward(random.randint(0,5))
    



screen.exitonclick()