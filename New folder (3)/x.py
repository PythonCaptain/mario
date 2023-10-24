import pgzrun
import os
import random

os.environ["SDL_VIDEO_CENTERED"] = "1"

WIDTH = 1000
HEIGHT = 700
TITLE = "Mario Game -> 1.0.0"

mario = Actor("mario" , (500 , 350))
gharch = Actor("gharch" , (random.randint(100,900) , random.randint(100,600)))
doshman = Actor("doshman" , (50 , 250))
over = Actor("over" , (500 , 350))

speed = 2
speed_2 = 1
score = 0
gameover = False

def update():
    global speed , speed_2 , score , gameover

    if doshman.x >= mario.x:
        doshman.x -= speed_2
    
    if doshman.x <= mario.x:
        doshman.x += speed_2

    if doshman.y >= mario.y:
        doshman.y -= speed_2
    
    if doshman.y <= mario.y:
        doshman.y += speed_2
    

    if gharch.x >= mario.x and gharch.x >= WIDTH - 50:
        gharch.x += 0.5
    
    if gharch.x <= mario.x and gharch.x >= 50:
        gharch.x -= 0.5

    if gharch.y >= mario.y and gharch.y <= HEIGHT - 50:
        gharch.y += 0.5
    
    if gharch.y <= mario.y and gharch.y >= 50:
        gharch.y -= 0.5
    

    if keyboard.up and mario.y >= 50:
        mario.y -= speed
    elif keyboard.down and mario.y <= HEIGHT - 50:
        mario.y += speed
    elif keyboard.right and mario.x <= WIDTH - 50:
        mario.x += speed
    elif keyboard.left and mario.x >= 50:
        mario.x -= speed

    if mario.colliderect(gharch):
        gharch.pos = random.randint(100,900) , random.randint(100,600)
        speed += 1
        speed_2 += 0.2
        score += 1

    if mario.colliderect(doshman):
        gameover = True

def draw():
    screen.fill("white")
    mario.draw()
    gharch.draw()
    doshman.draw()
    screen.draw.text(f"Score : {score}" , topleft = (50 , 50) , fontsize = 50 , color = "black")

    if gameover:
        over.draw()

pgzrun.go()