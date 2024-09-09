# Write your code here :-)
WIDTH = 800
HEIGHT = 600

import random
import time

rocket = Actor("rocket.png")
rocket.x = 400
rocket.y = 432

clouds = Actor("clouds.png")
clouds.x = 400
clouds.y = 20
clouds2 = Actor("clouds.png")
clouds2.x = 400
clouds2.y = -600

slider = Actor("slider")
slider.x = 30
slider.y = 250
slider.angle = 90

stage = "playscreen"

groundy = 450
speed = 0
tilt = 0
slideSpeed = 300
slideMove = 8

fall = [random.randrange(0, 800), -20]

hail = Actor("hail")
hail.x = random.randrange(0, 800)
hail.y = -20

score = 0
time = 0

plane = Actor("playership1_red.png")
plane.angle = 270
plane.x = 820
plane.y = 400

playscreen = Actor("playscreen.png")
playscreen.x = 400
playscreen.y = 300

space = [Actor("space.jpg"), Actor("space.jpg"), Actor("space.jpg"), Actor("space.jpg")]

playbutton_color = (245, 155, 64)
instructions_color = (151, 186, 35)

asteroid = Actor("asteroid.png")
asteroid.x = random.randrange(0, 800)
asteroid.y = -20

space[1].y= 300

skycolor = 216

powerup = Actor("powerup")

powerup.x = random.randrange(0, 800)
powerup.y = -60

powerups = 0

powerDown = False

usepower = False

powerTime = 0

instructions = False

for i in range (len(space)):
    space[i].x = 400
    space[i].y = space[i-1].y - 500

stars = []

for i in range(100):
    stars.append(Actor("star.png"))

for i in range (len(stars)):
    stars[i].x = random.randrange(0, 800)
    stars[i].y = random.randrange(-200, 0)

def draw():

    global stage, speed, hail, time, space, asteroid, skycolor

    if stage == "takeoff" or "flight":
        screen.fill((22, skycolor, 250))
        clouds.draw()
        clouds2.draw()

        ground = screen.draw.filled_rect(Rect(0, groundy, 800, 100), color="yellowgreen")
        ground = screen.draw.filled_rect(Rect(0, groundy+50, 800, 100), color="brown")
        slider.draw()

        screen.draw.filled_rect(Rect(15, slideSpeed, 30, 4), color = "white")

        textcolor = "black"

        if stage == "takeoff":
            screen.draw.text("P r e s s  's p a c e '  t o  l a u n c h ", (150, 150), color = "black", fontsize = 40)

    if stage == "flight":
        hail.draw()

        hail.y += speed+2

        if hail.y > 600:
            hail.y = -20
            hail.x = random.randrange(0, 800)

        if time%2000 in range (1200, 2000):
            plane.draw()
            plane.x -= 2
            plane.y += 0.5
            if plane.x < 20:
                plane.y = 820

    if stage == "levelup":
        if 50 < score < 51:
            textcolor = "white"
            screen.draw.text("LEVEL 2!", (400, 300), color = "white", fontsize = 100)
            screen.draw.text("+100 speed!", (400, 375), color = "white", fontsize = 85)
            #speed = speed + 100

    if stage == "level2":
        screen.fill((20, 54, 128))
        for i in stars:
            i.draw()
        asteroid.draw()
        powerup.draw()

    screen.draw.text("Speed: " + str(round(speed*1000, 2)) + " mph", (20, 50), color = textcolor)
    screen.draw.text("Distance: " + str(round(score, 3)) + " miles", (20, 30), color = textcolor)
    rocket.draw()

    #if stage == "gameover":
     #   screen.fill("black")
      #  screen.draw.text("GAME OVER", (400, 300), color = "white", fontsize = 100)
       # screen.draw.text("score: " + str(score), (400, 400), color = "white", fontsize = 100)
        #time.sleep()

    if stage == "playscreen":
        playscreen.draw()
        screen.draw.filled_rect(Rect(275, 275, 250, 100), color = playbutton_color)
        screen.draw.text("Play", (350, 300), color = "white", fontsize = 75)
        screen.draw.filled_rect(Rect(275, 400, 250, 100), color = instructions_color)
        screen.draw.text("Instructions", (290, 430), color = "white", fontsize = 55)

    if instructions == True:
        screen.draw.filled_rect(Rect(100, 20, 600, 350), color = "white")
        screen.draw.text("How to play:", (200, 50), color = "black", fontsize = 40)
        screen.draw.text("Level 1: \n - The slider determines your starting speed \n - Dodge the grey dots \n - If you go below a certain speed, you lose \n - Your score is determined by the total distance you travel", (200, 100), color = "black")
        screen.draw.text("Level 2: \n - When you get to 50 miles, you reach level 2\n - Dodge the asteroids \n - Collect the power ups \n - To use a power up, press the space key", (200, 225), color = "black")
def update():
    global stage, groundy, speed, tilt, slideSpeed, slideMove, time, hail, score, space, playbutton_color, asteroid, skycolor, usepower, powerups, powerDown, powerTime

    if stage == "takeoff":
        slideSpeed -= slideMove
        if slideSpeed < 185 or slideSpeed > 310:
            slideMove = -slideMove

        if keyboard.space:
            speed = (400-slideSpeed)/20
            rocket.image = "rocketfly.png"
            rocket.y -= speed
            stage = "flight"

    if stage == "flight" or stage == "levelup":
        slider.y = 800
        slideSpeed = 800
        groundy += speed
        clouds.y += speed
        clouds2.y += speed

        if abs(rocket.x - plane.x) < 20 and abs(plane.y - rocket.y) < 10:
            stage = "gameover"

        if clouds.y > 1000:
            clouds.x = random.randint(100, 700)
            clouds.y = -350

        if clouds2.y > 1000:
            clouds2.x = random.randint(100, 700)
            clouds2.y = -350

        if rocket.colliderect(hail):
            speed -= 0.1
            hail.y = 800

        if 50 < score < 52:
            stage = "levelup"
            skycolor -= 0.75
            speed += 0.00083

        if score > 52:
            stage = "level2"

        if speed < 5:
            stage = "gameover"

    if stage == "level2":
        for i in range (len(stars)):
            stars[i].y += speed
            if stars[i].y > 600:
                stars[i].y = random.randrange(-200, 0)

        if time % 900 == 0:
            powerDown = True
        if powerDown == True:
            powerup.y += speed+5
        if powerup.y > 600 or powerups > 0:
            powerup.y = -20
            powerDown = False

        if rocket.colliderect(asteroid):
            speed -= 0.1
            asteroid.y = 800

        if rocket.colliderect(powerup):
            powerups += 1
            powerup.y = -20

        if keyboard.space and powerups > 0:
            usepower = True

        if usepower == True:
            powerups -= 1
            speed += 5
            rocket.image = "rocketfly2"
            powerTime += 1/60
            usepower = False

        if powerTime > 5:
            rocket.image = "rocketfly.png"
            speed -= 5
            powerTime = 0


        asteroid.y += speed+4

        if asteroid.y > 600:
            asteroid.y = -20
            asteroid.x = random.randrange(0, 800)
            asteroid.angle = random.randrange(0, 180)

        if speed < 5:
            stage = "gameover"

    if stage != "takeoff" and stage != "playscreen":
        time += 1
        score = (speed*time)/1080
        rocket_move()

    #if keyboard.up:
    #    stage = "level2"

def on_mouse_move(pos):
    global stage, playbutton_color, instructions, instructions_color
    if stage == "playscreen" and 275<pos[0]<525 and 275<pos[1]<375:
        playbutton_color = (242, 191, 97)

    else:
        playbutton_color = (245, 155, 64)

    if stage == "playscreen" and 275<pos[0]<525 and 400<pos[1]<500:
        instructions_color = (176, 201, 89)
        instructions = True
    else:
        instructions_color = (151, 186, 35)
        instructions = False

def on_mouse_down(pos):
    global stage
    if stage == "playscreen" and 275<pos[0]<525 and 275<pos[1]<400:
        stage = "takeoff"

def rocket_move():
    global tilt, time
    if keyboard.left:
        tilt = -1
    if keyboard.right:
        tilt = 1
    if tilt == -1 and 20 < rocket.x:
        rocket.angle = 3
        rocket.x -= 1.5
    if tilt == 1 and rocket.x < 780:
        rocket.angle = -3
        rocket.x += 1.5
#level 1:
#make rocket go up and down when flying
#fix airplane
#add 'press space to launch' text
#fix gameover screen
#don't let rocket leave boundary

#level 2:
#fix level 2 text
#add powerups
