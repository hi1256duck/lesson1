import pgzrun 
import random

WIDTH=500
HEIGHT=500
TITLE="stars full of skys"
Slist=[]
for i in range(12):

    star=Actor("star")
    star.pos=(random.randint(0,500),random.randint(0,500))
    Slist.append(star)
def draw():
    screen.blit("sky.png",(0,0))
    for i in Slist:
        i.draw()

        
pgzrun.go()