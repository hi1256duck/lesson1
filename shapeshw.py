import pgzrun
import random
WIDTH =600
HEIGHT =600

def draw():
    screen.draw.rect(Rect((150,150),(400,100)),color="cyan")
    screen.draw.rect(Rect((120,264),(199,100)),color="red")
    screen.draw.rect(Rect((random.randint(21,600),random.randint(21,600)),(100,600)),color="green")
    screen.draw.rect(Rect((random.randint(21,100),random.randint(21,100)),(600,500)),color="pink")
    screen.draw.rect(Rect((random.randint(21,600),random.randint(21,600)),(500,300)),color="purple")
    screen.draw.rect(Rect((random.randint(21,600),random.randint(21,600)),(200,200)),color="yellow")
   






pgzrun.go()