import random
import turtle as t
t.colormode(255)
# import colorgram
# rgb_colors=[]
# colors = colorgram.extract('Spots.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     color_tuple = (r,g,b)
#     rgb_colors.append(color_tuple)
# print(rgb_colors)
color_list = [(236, 35, 108), (222, 231, 237), (145, 28, 65), (239, 74, 34), (6, 148, 93), (231, 238, 234), 
(232, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 
223, 0), (85, 28, 93), (172, 36, 98), (246, 219, 44), (42, 172, 112), (216, 130, 165), (216, 58, 26), (235, 164, 190), (156, 25, 
22), (20, 189, 230), (238, 169, 157), (162, 210, 182), (137, 211, 232), (0, 123, 53), 
(85, 131, 185), (181, 187, 212), (243, 13, 
24)]

screen = t.Screen()
screen.bgcolor('black')
n=-200
tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.speed(100)
for i in range(10):
    tim.setx(-300)
    tim.sety(n)
    n+=50
    for _ in range(10):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.fd(50)
        



screen.exitonclick()