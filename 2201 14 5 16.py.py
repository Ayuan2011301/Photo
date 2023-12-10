import turtle as t  
import random
t.speed(0) 
clor=['pink','yellow','red','blue','purple']
def flower(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    r=random.randint(10,50)
    t.fillcolor(random.choice(color))
    t.begin_fill()
    for i in range(5):
        t.circle(r)
        t.left(72)
    t.end_fill
    t.dot(r,'yellow')
t.onscreenclick(flower)
t.done()