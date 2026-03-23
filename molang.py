import pgzrun
import random
WIDTH=500
HEIGHT=500

TITLE="CLICKER GAME"
Mo=Actor("molang.png")
score=0
drums=Actor("drum.png")
def draw():
    screen.fill(color="blue")
    Mo.draw()
    drums.draw()
    screen.draw.text(str(score),center=(400,50),color="grey")
def mo_jump():
    Mo.x=random.randint(0,500)
    Mo.y=random.randint(0,500)
def drums_jump():
    drums.x=random.randint(0,500)    
    drums.y=random.randint(0,500)
   
def  on_mouse_down(pos):
     global score
     if Mo.collidepoint(pos):     
         score+=1
         mo_jump()
     if drums.collidepoint(pos):
         score-=1
         drums_jump()

               



pgzrun.go()