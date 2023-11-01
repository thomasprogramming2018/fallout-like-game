import pygame

from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
import time
from pygame.time import *
import random as rand
#import main

class Pathfinder:
    def __init__(self, matrix, npc, player):
        self.matrix = matrix
        self.grid = Grid(matrix=matrix)
        self.path = []

        self.ttoBody = pygame.sprite.GroupSingle(npc)
        self.Body = npc
        self.player = player
        self.empty_path()
        
    def empty_path(self):
        self.path = []

    def create_path(self):
        # start
        start_x, start_y = self.ttoBody.sprite.get_coord()
        start_x, start_y = self.Body.get_coord()
        start = self.grid.node(start_x, start_y)

        # end
        mouse_pos = pygame.mouse.get_pos()
        self.amountxx = rand.randint(100,150)
        self.amountx = rand.randint(30,self.amountxx)
        self.amounty = rand.randint(30,80)
        self.minusOrPlus = rand.randint(0,1)
        screen_W = 1320
        screen_H = 920
        if self.Body.isEnemy == True:
            if self.minusOrPlus == 0:
                if not screen_W - 200 < self.Body.rect.x - self.amountx:
                    self.px = self.player.rect.x - self.amountx
            else:
                if not screen_W - 200 < self.Body.rect.x + self.amountx:
                    self.px = self.player.rect.x + self.amountx
            if not screen_H - 200 <= self.Body.rect.y + self.amounty:
                self.py = self.Body.rect.y + self.amounty
            if not 200 >= self.Body.rect.y - self.amounty:
                self.py = self.Body.rect.y - self.amounty
        else:
            if self.minusOrPlus == 0:
                if not 200 > self.Body.rect.x - self.amountx:
                    self.px = self.Body.rect.x - self.amountx
            else:
                if not screen_W - 200 < self.Body.rect.x + self.amountx:
                    self.px = self.Body.rect.x + self.amountx
            if not screen_H - 200 <= self.Body.rect.y + self.amounty:
                self.py = self.Body.rect.y + self.amounty
            if not 200 >= self.Body.rect.y - self.amounty:
                self.py = self.Body.rect.y - self.amounty
        end_x, end_y = self.px // 32, self.py // 32
        end = self.grid.node(end_x, end_y)

        # path
        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        self.path, _ = finder.find_path(start, end, self.grid)
        self.grid.cleanup()
        self.ttoBody.sprite.set_path(self.path)
        self.Body.set_path(self.path)
    def update(self):
        self.ttoBody.update()
    

class Npc(pygame.sprite.Sprite):
    def __init__(self, group, rx, ry, image_location, weapon, empty_path, id):
        super().__init__()
        self.did = 2
        self.direction = "right-down"
        
        self.isAnimating = False
        self.sprites = []
        for i in range(1,13):
          self.sprites.append(pygame.image.load(f"{image_location}/{self.did}/playerIdle ({i}).png"))
        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]

        self.clicked = False

        self.turn = False

        self.id = id

        self.rhp = 100

        self.speed = 3

        self.direction2 = pygame.math.Vector2(0,0)
        
        self.path = []
        self.collision_rects = []
        self.empty_path = empty_path

        self.moving = False

        self.rect = self.image.get_rect()

        self.rxx = rx
        self.ryy = ry
        self.rect.x = rx
        self.rect.y = ry

        self.isEnemy = False
        
        self.pos = self.rect.center
        
        self.empty_path = empty_path

        self.path_index = 0
        
        self.degree = "down"
        self.frame = 0
        self.weapon = weapon
        self.damage = 3
        self.dead = False
        self.collision_rects = []
        self.empty_path = empty_path
        self.isShot = True
    def shoot(self):
        if self.weapon == "shotgun":
            self.damage = 10
            return self.damage
    def isDead(self):
        for i in range(1,13):
            self.sprites.append(pygame.image.load("objects/animations/Dead/dead.png"))
        self.dead = True
    def animate(self):
        self.isAnimating = True

    def get_coord(self):
        col = self.rect.centerx // 32
        row = self.rect.centery // 32
        return (col,row)

    def set_path(self,path):
        self.path = path
        self.path_index = 0
        self.create_collision_rects()
        self.get_direction()

    def create_collision_rects(self):
        if self.path:
            self.collision_rects = []
            for point in self.path:
                x = (point[0] * 32) + 16
                y = (point[1] * 32) + 16
                rect = pygame.Rect((x - 2,y - 2),(4,4))
                self.collision_rects.append(rect)

    def get_direction(self):
            if self.collision_rects:
                start = pygame.math.Vector2(self.pos)
                end = pygame.math.Vector2(self.collision_rects[0].center)
                self.direction2 = (end - start).normalize()
            else:
                self.direction2 = pygame.math.Vector2(0,0)
                self.path = []

    def check_collisions(self):
        if self.collision_rects:
            for rect in self.collision_rects:
                if rect.collidepoint(self.pos):
                    del self.collision_rects[0]
                    self.get_direction()
        else:
            if self.empty_path == None:
                pass
            else:
                self.empty_path
    def direction_apply(self):
        
        if self.degree == 'right' and self.moving == True and self.rhp >= 0:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/1/frame_0{i}_delay-0.1s.png"))
        elif self.degree == 'down-Right' and self.moving == True and self.rhp >= 1:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/2/frame_0{i}_delay-0.1s.png"))
        elif self.degree == 'up-Right' and self.moving == True and self.rhp >= 1:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/0/frame_0{i}_delay-0.1s.png"))
        elif self.degree == 'down-Left' and self.moving == True and self.rhp >= 1:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/3/frame_0{i}_delay-0.1s.png"))
        elif self.degree == 'up-Left' and self.moving == True and self.rhp >= 1:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/m1/frame_0{i}_delay-0.1s.png"))
        elif self.degree == 'left' and self.moving == True and self.rhp >= 1:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/3/frame_0{i}_delay-0.1s.png"))
        elif self.moving == False and self.rhp >= 1:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load("objects/animations/playerIdleSprites/2/playerIdle (1).png"))
                
    def direction_check(self):
        if self.dx > 0:
            if self.dy > 0:
                self.degree = 'down-Right'
            elif self.dy < 0:
                self.degree = 'up-Right'
            else:
                self.degree = 'right'
        if self.dx < 0:
            if self.dy > 0:
                self.degree = 'down-Left'
            elif self.dy < 0:
                self.degree = 'up-Left'
            else:
                self.degree = 'left'
             
    def update(self):
        self.old_rect = self.rect.copy()
        self.didit = False
        if self.rect.x > 700 or self.rect.x < 100 or self.rect.y > 700 or self.rect.y < 100:
            self.rect.x = 500
            self.rect.y = 500
        if self.rhp != 100:
            self.isEnemy = True
            

        if self.isAnimating == True:
            self.currentSprite += 0.3

            if self.currentSprite >= len(self.sprites):
                self.currentSprite = 0
                self.isAnimating = False
        self.image = self.sprites[int(self.currentSprite)]
        self.pos += self.direction2 * self.speed
        new_pos = self.pos
        self.check_collisions()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
        self.rect.x = self.pos.x 
        self.rect.y = self.pos.y

        self.currentX = self.rect.x
        self.currentY = self.rect.y
        self.oldX = self.old_rect.x
        self.oldy = self.old_rect.y
        self.dx = self.currentX - self.oldX
        self.dy = self.currentY - self.oldy 
        if self.currentX - self.oldX == 0:
            self.moving = False
        else:
            self.moving = True
        self.direction_check()
        self.direction_apply()
        global gotAtPos
        if self.path == []:
            
            gotAtPos = True
        else:
            gotAtPos = False
        
        
        #print(self.rect.x, self.rect.y)
        if  new_pos.x <= 0 or new_pos.x > 1320 or new_pos.y <= 0 or new_pos.y > 920:
            self.pos.x = 300
            self.pos.y = 300
        
        pos = pygame.mouse.get_pos()
        global clicked
        action2 = False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                global enemyid
                #global clicked
                clicked = True
                self.isShot = True
                action2 = True
                self.drawit() 
                enemyid = self.id
                self.clicked = True
                
                
                return action2
        if pygame.mouse.get_pressed()[0] == 0:
            #if pygame.mouse.get_pressed()[0] and self.clicked == True:
            self.clicked = False
            enemyid = self.id
            self.drawit()
            self.isShot = False
            clicked = False
            action2 = False
        
        
            return action2
            
    def drawit(self):
        if self.clicked == True:
            global enemyid
            print('clicked!!!!')
            enemyid = self.id
            global clicked
            clicked = False
            return True
        else:
            return False