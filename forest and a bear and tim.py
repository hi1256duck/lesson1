import random
import pgzrun
WIDTH=800
HEIGHT=500

tim=Actor("oldman")
tim.pos=(88,67)
jamal=Actor("bear")   
jamal.pos=(500,67)    
def draw():
    screen.blit("forest2",(0,0))
    tim.draw()
    jamal.draw()


def update():
    if keyboard.left:
      tim.x=tim.x-2
    if keyboard.right:
      tim.x=tim.x+2  
    if keyboard.up:
      tim.y=tim.y-2
    if keyboard.down:
      tim.y=tim.y+2

    if tim.colliderect(jamal):
      jamal.pos=(random.randint(0,800),random.randint(0,500))
    
 
     


pgzrun.go()