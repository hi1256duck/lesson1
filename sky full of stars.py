import pgzrun 
import random

WIDTH=700
HEIGHT=500
TITLE="stars full of skys"
number_of_star=5
Slist=[]
next_star = 0
lines=[]
for i in range(number_of_star):

    star=Actor("star")
    star.pos=(random.randint(50,650),random.randint(50,450))
    Slist.append(star)
def draw():

    screen.blit("sky.png",(0,0))
    number = 1

    for star in Slist:
        screen.draw.text(str(number),(star.pos[0]-10, star.pos[1]+40))
        number+=1
        star.draw()
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))  

def on_mouse_down(pos):
    global next_star, lines
    if next_star < number_of_star:
        if Slist[next_star].collidepoint(pos):
            if next_star:
                lines.append((Slist[next_star-1].pos,Slist[next_star].pos))
            next_star = next_star+1
        else:
            lines=[]    
            next_satellite = 0            
pgzrun.go()