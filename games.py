import random
import turtle
from turtle import Turtle, Screen

screen = Screen()

t = Turtle("turtle")
t.speed(-1)


colors = ["#00FFFF","#8A2BE2","#7FFF00","#FF8C00","#00BFFF","#800000","#FF0000","#00FF7F"]

def dragging(x, y):
    t.color(random.choice(colors)) 
    t.ondrag(None)
    t.pendown()
    t.setheading(t.towards(x, y))
    t.goto(x,y)
    t.ondrag(dragging)
   
    


def clickright(x,y):
    t.clear()
   

def main():
    turtle.listen()

    t.ondrag(dragging)
    t.penup()


    turtle.onscreenclick(clickright, 3)
    

    screen.mainloop()

main()