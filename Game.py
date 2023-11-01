import turtle as t 
import os
from os.path import exists

##window config
screen = t.Screen()
screen.tracer(0)
screen.bgcolor('BLACK')

##constants##

##Variables
hp_S = "100"
loc_S = "Aroyo"
toGo = ""
hp = "100"
loc = "Aroyo"
beenSaid = False
playerSpeed = 5
hp_int = 0
playerPosX = 0
playerPosY = 0
months = ["null","jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec","jan"]
year = 2160
day = 25
time_ = 1 #1=1am - 23 = 11pm, 0 = 12am
month = 12
months_c = "dec"
lastLoc = "Aroyo"
L_x = 0
L_y = 0
isTped = False
target= 0

#inventory and weapons
playerEquiped = 0 #0 == unarmed 1 == pistol 2 == 10mm ammo 3 == minigun etcetc 
#slot0 == unarmed slot1 == 10mm slot2 == 10mm rounds slot4 == minigun
weaponDamage = [10,30,0,50] 
#turnBased Sys
turn = 0 #0 == player 1 == first enemy 2 == etc etc

##raider health
r_hp_Max = 70
r_hp_current = 70
r_armor = 1
r_drop = [1,2]

#map etc
isAtMarker = False

##Screen/Gui setup
Date_T = t.Turtle()
Date_T.hideturtle()
arroyo = t.Turtle()
arroyo.color('green')
arroyo.hideturtle()

##Enemy setup
raider = t.Turtle()
raider.color('RED')
raider.shape('square')
#raider.hideturtle()
raider.showturtle()

##Map-Arroyo only
wastewall = t.Turtle()
screen.addshape('villageWall.gif')
wastewall.shape('villageWall.gif')
wastewall.up()
wastewall.goto(0,-200)

floor = t.Turtle()
screen.addshape('floor.gif')
floor.shape('floor.gif')
floor.up()
floor.goto(-200,300)

wall1 = t.Turtle()
screen.addshape('wall.gif')
wall1.shape('wall.gif')
wall1.up()
wall1.goto(-200,260)

roof = t.Turtle()
screen.addshape('roof.gif')
roof.shape('roof.gif')
roof.up()
roof.goto(-200,360)
test = t.Turtle()
test.goto(-170,345)

#Functions
def follow():
    global r_hp_current
    global weaponDamage
    player.setheading(player.towards(raider))
    player.forward(1)

    if raider.distance(player) < 20:  
        r_hp_current -= weaponDamage[0]
    else:
        screen.ontimer(follow, 10)
def shoot(i,j):
    global target
    global r_hp_current
    global weaponDamage
    print('done')
    if target == 1:
        if playerEquiped == 1:
            r_hp_current -= weaponDamage[1]
        elif playerEquiped == 0:
            follow()
                
        elif playerEquiped == 3:
            r_hp_current -= weaponDamage[3]
        if r_hp_current < 1:
            raider.hideturtle()
def lastLocation(last):
    global L_x
    global L_y
    if lastLoc == "Aroyo":
        L_x = arroyo.xcor()
        L_y = arroyo.ycor()
def showLocalMap():
    if loc == 'Aroyo':
        wall1.showturtle()
        floor.showturtle()
        roof.showturtle()

        #npcs/enemies
        #raider.showturtle()
        
        #wastewall.showturtle()
        screen.bgpic('wasteMap.gif')
        if player.distance(wall1) < 100:
            wall1.hideturtle()
        if player.distance(roof) < 100:
            roof.hideturtle()
    if loc == 'worldMap':
        wall1.hideturtle()
        floor.hideturtle()
        roof.hideturtle()
        wastewall.hideturtle()
        screen.bgpic('nopic')
        screen.bgcolor('BROWN')
def hideMap():
    arroyo.hideturtle()
    Date_T.clear()
    Date_T.hideturtle()

def location_Enter():
    global loc
    global isAtMarker
    global toGo
    if player.distance(arroyo) < 1:
        isAtMarker = False
        loc = toGo 
        hideMap()

def m_ar_welcome():
    print('you see a sign made out of junk saying "welcome to Aroyo" and a guard standing nearby')
def deathScreen():
    screen.bgcolor('GREY')
def dead():
    isExisting = file_exists = exists("/saves/hpsave.txt")
    if isExisting == True:
        file1 = open("saves/hpsave.txt","r")
        hp_S = file1.readlines()
        file1.close()
    isExisting2 = file_exists = exists("/saves/loc.txt")
    if isExisting2 == True:
        file1.close()
        file1 = open("saves/loc.txt", "r")
        loc_S = file1.readlines()
        file1.close()


##Saves Check
isExisting = file_exists = exists("/saves/hpsave.txt")
if isExisting == True:
    file1 = open("saves/hpsave.txt","r")
    hp_S = file1.readlines()
    file1.close()
isExisting2 = file_exists = exists("/saves/loc.txt")
if isExisting2 == True:
    file1.close()
    file1 = open("saves/loc.txt", "r")
    loc_S = file1.readlines()
    file1.close()

##player setup
player = t.Turtle()
player.color('WHITE')
screen.addshape('playerIdle-0.gif')
screen.addshape('playerIdle-1.gif')
screen.addshape('playerIdle-2.gif')
screen.addshape('playerIdle-3.gif')
screen.addshape('playerIdle-4.gif')
screen.addshape('playerIdle-5.gif')
screen.addshape('walkUnarmed-0.gif')
screen.addshape('walkUnarmed-1.gif')
screen.addshape('walkUnarmed-2.gif')
screen.addshape('walkUnarmed-3.gif')
screen.addshape('walkUnarmed-4.gif')
screen.addshape('walkUnarmed-5.gif')
player.shape('playerIdle-0.gif')
player.penup()
player.direction = "Stop"

##Movement Function 

def movetoDirection(speed):
    global time_
    global playerEquiped
    if player.direction == "up":
        y = player.ycor()
        player.sety(y+speed)
        if playerEquiped == 0:
            player.shape('walkUnarmed-0.gif')
        elif playerEquiped == 1:
            player.shape('walkPistol-0.gif')#todo add minigun
        if loc == "worldMap":
            time_ += 1
    if player.direction == "down":
        y = player.ycor()
        player.sety(y-speed)
        if playerEquiped == 0:
            player.shape('walkUnarmed-3.gif')
        elif playerEquiped == 1:
            player.shape('walkPistol-3.gif')#todo add minigun
        if loc == "worldMap":
            time_ += 1
    if player.direction == "left":
        x = player.xcor()
        player.setx(x-speed)
        if playerEquiped == 0:
            player.shape('walkUnarmed-4.gif')
        elif playerEquiped == 1:
            player.shape('walkPistol-4.gif')#todo add minigun
        if loc == "worldMap":
            time_ += 1
    if player.direction == "right":
        x = player.xcor()
        player.setx(x+speed)
        if playerEquiped == 0:
            player.shape('walkUnarmed-1.gif')
        elif playerEquiped == 1:
            player.shape('walkPistol-1.gif')#todo add minigun
        if loc == "worldMap":
            time_ += 1

def goup():
    if player.direction != "down":
        player.direction = "up"
        movetoDirection(playerSpeed)
 
def godown():
    if player.direction != "up":
        player.direction = "down"
        movetoDirection(playerSpeed)
 
def goleft():
    if player.direction != "right":
        player.direction = "left"
        movetoDirection(playerSpeed)
 
def goright():
    if player.direction != "left":
        player.direction = "right"
        movetoDirection(playerSpeed)
##KeyBindings
screen.listen()
screen.onkeypress(goleft, 'Left')
screen.onkeypress(goright, 'Right')
screen.onkeypress(goup, 'Up')
screen.onkeypress(godown, 'Down')
target = 1
raider.onclick(shoot, 1)

##Main Menu
while True:
    command = str(input('>'))
    if command == "resume":
        loc_S = loc
        hp_S = hp
    elif command == "start":
        ##Game start
        while True:
            if time_ > 23:
                time_ = 0 
                day += 1
            #elif month > 12:
            #    day = 1
            #    month = 1
            #    time_ = 0
            #    months_c = months[month]
            #    year += 1
            elif day > 31:
                day = 1
                if month == 12:
                    day = 1
                    year += 1
                    month = 1
                    time_ = 0
                    print(month)
                    months_c = months[month]
                    
                else:                     
                    month += 1  
                    months_c = months[month]


            screen.update()
            #Todo na vallw to wall sto if loc == arroyo
            if loc == "Aroyo":
                if player.xcor() < -700 or player.xcor() > 700:
                    loc = "worldMap"
                    beenSaid = False 
                elif player.ycor() < -700 or player.ycor() > 700:
                    loc = "worldMap"
                    beenSaid = False

            hp_int = int(hp)
            if hp_int < 1:
                deathScreen()
                dead()
            if loc == "Aroyo":
                ##screen.bgcolor('YELLOW')
                hideMap()
                if beenSaid == False:
                    m_ar_welcome()
                beenSaid = True
                lastLoc = "Aroyo"
                isTped = False

                if player.direction == 'down':
                    player.shape('playerIdle-3.gif')
                elif player.direction == 'up':
                    player.shape('playerIdle-0.gif')
                elif player.direction == 'left':
                    player.shape('playerIdle-4.gif')
                elif player.direction == 'right':
                    player.shape('playerIdle-1.gif')
                if player.xcor() < -65 and player.xcor() > -200 and player.ycor() > 220 and player.ycor() < 230:
                            #player.goto(player.xcor(),player.ycor() - 10)
                    if player.direction == "up":
                        player.goto(player.xcor(),player.ycor() - 5)
                    if player.direction == "down":
                        player.goto(player.xcor(),player.ycor() + 5)
                    if player.direction == "right":
                        player.goto(player.xcor() - 5,player.ycor())
                    if player.direction == "left":
                        player.goto(player.xcor() + 5,player.ycor())
                if player.xcor() < -230 and player.xcor() > -300 and player.ycor() > 220 and player.ycor() < 230:
                            #player.goto(player.xcor(),player.ycor() - 10)
                    if player.direction == "up":
                        player.goto(player.xcor(),player.ycor() - 5)
                    if player.direction == "down":
                        player.goto(player.xcor(),player.ycor() + 5)
                    if player.direction == "right":
                        player.goto(player.xcor() - 5,player.ycor())
                    if player.direction == "left":
                        player.goto(player.xcor() + 5,player.ycor())
                if player.xcor() < -55 and player.xcor() > -700 and player.ycor() < -240 and player.ycor() > -250:
                        #player.goto(player.xcor(),player.ycor() - 10)
                    if player.direction == "up":
                        player.goto(player.xcor(),player.ycor() - 5)
                    if player.direction == "down":
                        player.goto(player.xcor(),player.ycor() + 5)
                    if player.direction == "right":
                        player.goto(player.xcor() - 5,player.ycor())
                    if player.direction == "left":
                        player.goto(player.xcor() + 5,player.ycor())
                if (player.xcor() < -55 and player.xcor() > -700 or player.xcor() > -5 and player.xcor() < 700) and player.ycor() < -160 and player.ycor() > -245:
                        #player.goto(player.xcor(),player.ycor() - 10)
                        wastewall.hideturtle()
                else:
                    wastewall.showturtle()
                if player.xcor() > -5 and player.xcor() < 700 and player.ycor() < -240 and player.ycor() > -250:
                            #player.goto(player.xcor(),player.ycor() - 10)
                    if player.direction == "up":
                        player.goto(player.xcor(),player.ycor() - 5)
                    if player.direction == "down":
                        player.goto(player.xcor(),player.ycor() + 5)
                    if player.direction == "right":
                        player.goto(player.xcor() - 5,player.ycor())
                    if player.direction == "left":
                        player.goto(player.xcor() + 5,player.ycor())

            ##Map
            
            elif loc == "worldMap":
                arroyo.penup()
                arroyo.shape('circle')
                
                #arroyo.turtlesize(5)
                arroyo.goto(-100,100)
                arroyo.turtlesize(5)
                lastLocation(lastLoc)
                if isTped == False:
                    player.goto(L_x,L_y)
                    isTped = True
                arroyo.showturtle()
                screen.bgcolor('BROWN')
                Date_T.penup()
                Date_T.goto(400,400)
                Date_T.showturtle()
                Date_T.clear()
                Date_T.write(f'{day} {months_c} {year} {time_}:00', align="right", font=("terminal", 20, "normal"))
                if beenSaid == False:
                    print('welcome to the world map move around and press m while you in the green circle(means the location is been discovered or is about to) to get to the location')
                    ##m_ar_welcome()
                beenSaid = True
                if player.distance(arroyo) < 0.1:
                    print("in")
                    isAtMarker = True
                    toGo = "Aroyo"
                    screen.listen()
                    screen.onkeypress(location_Enter, 'm')
                if player.distance(arroyo) > 0.1:
                    print("out")
                    isAtMarker = False
            showLocalMap()



                
                
                
    

