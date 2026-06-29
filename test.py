import pgzrun
import random

WIDTH=800
HEIGHT=600
TITLE="THE ULTIMATE CAPITALS QUIZ"


score=0
time_left=7
game_over=False

quest=[
    ["Captials of india?","new york","new delhi","dhanka","rome","new dehli"],
    ["Captials of uk?","new york","london","paris","rome","london"],
    ["Captials of france?","new york","london","paris","rome","paris"]]

q_num=0
question=quest[q_num]    

boxes=[
    Rect(50,200,300,80),
    Rect(450,200,300,80),
    Rect(450,350,300,80),
    Rect(50,350,300,80),

]

def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.textbox(
        question[0],
        Rect(50,80,700,80),
        color="red"
    )

    for i in range(4):
        screen.draw.filled_rect(boxes[i],"red")
        screen.draw.textbox(
            question[i+1],
            boxes[i],
            color="black"
    if game_over:
        screen.clear()
        screen.fill(color="black")
        screen.draw.text(
            "Quiz completed!",
            center=(WIDTH//2,HEIGHT//2),
            color="blue")
            screen.draw.text(
                f"Final Score:{score}/{len(quest)}",
                center=(WIDTH//2,400),
                fontsize=40,
                color="purple"
            )
        
         
        screen.draw.text(f"Score:{score}",(50,20),color="beige")
        screen.draw.text(f"Time:{time_left}",(700,20),color="beige")
def on_mouse_down(pos):        
    global score,q_num,question,game_over

    if game_over:
        return
    for i in range(4):
        if boxes[i].collidepoint(pos):
            if str(i+1)==question[5]:
                score+=1
            q_num+=1    
            if q_num<len(quest):
                question=quest[q_num]
            else:
                game_over=True
def update_time():
    global timr_left,game_over
    if game_over:
        return
    if time_left>0:
        time_left -=1
    else:
        game_over=True
clock.schedule_interval(update_time,1)            







































pgzrun.go()
