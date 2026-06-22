import pgzrun
import random
WIDTH=600
HEIGHT=500
TITLE="HUNTER WHO'S SHOOTING"



birds=[]
pizza=Actor("bird")
pizza.pos=(random.randint(0,600),random.randint(-100,0))
birds.append(pizza)




brian=Actor("hunter" )
brian.pos=(WIDTH/2,HEIGHT-60)
bullets=[]
def on_key_down(key):
    if key == keys.UP:
        b=Actor("bullet")
        b.x=brian.x
        b.y=brian.y-50
        bullets.append(b)

def draw():

    screen.blit("field",(0,0))
    brian.draw()  
    
    for b in bullets:
        b.draw()
    for p in birds:
        p.draw()    
def update():
    if keyboard.left:
        brian.x-=10
    if keyboard.right:    
        brian.x+=10
    for b in bullets:
        b.y-=6
        if b.y <=0:    
            bullets.remove(b)        
    for p in birds:
        p.y+=6
        if p.y>=HEIGHT:
            p.pos=(random.randint(0,600),random.randint(-100,0))
        for b in bullets:    
            if p.colliderect(b):
                bullets.remove(b)
                birds.remove(p)
                pizza=Actor("bird")
                pizza.pos=(random.randint(0,600),random.randint(-100,0))
                birds.append(pizza)






pgzrun.go()