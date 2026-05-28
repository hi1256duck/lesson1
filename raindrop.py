import pgzrun

WIDTH=300
HEIGHT=500
TITLE="DROP"

fahad=Actor("raindrop")
fahad.pos=(150,100)
def draw():
    
    screen.fill(color="blue")
    fahad.draw()

def update():
    fahad.y+=5
    if fahad.y==500:
        fahad.y=0














pgzrun.go()