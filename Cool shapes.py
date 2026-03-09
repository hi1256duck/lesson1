import pgzrun

WIDTH =300
HEIGHT =300

TITLE="AWESOME SHAPES"

def draw():
    r=225
    g=0
    b=61

    w=WIDTH
    h=HEIGHT-200

    
    for i in range(20):
        my_rect=Rect((0,200),(w,h))
        my_rect.center=150,150
        screen.draw.rect(my_rect,(r,g,b))
        w-=20
        h+=10
        g+=10
        r-=10







pgzrun.go()