import turtle as t
import random
screen = t.Screen()
screen.bgcolor('black')
tim = t.Turtle()
tim.shape('classic')
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


# challenge 2 dashed line

# for _ in range(20):
#     color = random.choice(['green','red','blue','black','yellow'])
#     tim.color(color)
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

# challenge 3 shapes

# n=3
# for i in range(n,11):
#     angle=360/n
#     for _ in range (n):
#         tim.forward(100)
#         tim.right(angle)
#     tim.color(random.choice(['green','red','blue','black','yellow']))
#     n+=1
    
#     print(angle)

# challenge 4 random walk

# tim.pensize(15)
# directions = [0,90,180,270]
# while True:
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())
#     tim.speed(random.choice(directions))
#     print(tim.pos())

# challenge 5 spirograph

# tim.speed(100)
# directions = [0,90,180,270]
# n=0
# while True:
#     tim.color(random_color())
#     tim.circle(60)
#     tim.setheading(n)
#     n+=10
#     print(n)

# final challenge

tim.speed(100)
directions = [0,90,180,270]
n=0
while True:
    tim.color(random_color())
    tim.circle(60)
    tim.setheading(n)
    n+=10
    print(n)

screen.exitonclick()
