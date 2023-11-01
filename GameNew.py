import pygame,sys
from pygame.locals import *
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
import time
import os

class Player(pygame.sprite.Sprite):
    def __init__(self,groups,obstacles):
        super().__init__()
        
        self.isAnimating = False
        self.sprites = []
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (1).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (2).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (3).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (4).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (5).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (6).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (7).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (8).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (9).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (10).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (11).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (12).png'))
        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]

        self.obstacles = obstacles

        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 400
        self.pos = pygame.math.Vector2(self.rect.topleft)
        
        
        self.degree = "down"
        self.movex = 0
        self.movey = 0
        self.frame = 0
    def animate(self):
        self.isAnimating = True
    #def move(self, x, y):
        #pygame.rect.Rect.move_ip(x,y)

    def move(self, pressed_keys):
        global moving
        if pressed_keys[K_w] and turn == 0 or pressed_keys[K_w] and turn == 10:#up
            moving = True
            if caps_Running == False:
                self.rect.move_ip(2, -2)
                self.degree = "up"
                self.direction(self.degree)
            else:
                self.rect.move_ip(5, -5)
                self.degree = "up-Run"
                self.direction(self.degree)
        if pressed_keys[K_q] and turn == 0 or pressed_keys[K_q] and turn == 10:#up
            moving = True
            if caps_Running == False:
                self.rect.move_ip(-2, 2)
                self.degree = "up-left"
                self.direction(self.degree)
            else:
                self.rect.move_ip(-5, -5)
                self.degree = "up-left-Run"
                self.direction(self.degree)  
        if pressed_keys[K_x] and turn == 0 or pressed_keys[K_x] and turn == 10:#Down
            moving = True
            if caps_Running == False:
                self.rect.move_ip(2, 2)
                self.degree = "down"
                self.direction(self.degree)
            else:
                self.rect.move_ip(5, 5)
                self.degree = "down-Run"
                self.direction(self.degree)
        if pressed_keys[K_a] and turn == 0 or pressed_keys[K_a] and turn == 10:#left
            moving = True
            if caps_Running == False:
                self.rect.move_ip(-2, 0)
                self.degree = "left"
                self.direction(self.degree)
            
            else:
                self.rect.move_ip(-5, 0)
                self.degree = "left-Run"
                self.direction(self.degree)
        if pressed_keys[K_d] and turn == 0 or pressed_keys[K_d] and turn == 10:#right
            moving = True
            if caps_Running == False:
                self.rect.move_ip(2, 0)
                self.degree = "right"
                self.direction(self.degree)
            else:
                self.rect.move_ip(5, 0)
                self.degree = "right-Run"
                self.direction(self.degree)
        if pressed_keys[K_z] and turn == 0 or pressed_keys[K_z] and turn == 10:#down-left
            moving = True
            if caps_Running == False:
                self.rect.move_ip(-2, 2)
                self.degree = "down-left"
                self.direction(self.degree)
            else:
                self.rect.move_ip(-5, 5)
                self.degree = "down-left-Run"
                self.direction(self.degree)

    def direction(self, degree):
        if degree == 'up':
            self.sprites.clear()
            self.sprites.append(pygame.image.load('objects/animations/Walk/0/frame_0_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/0/frame_1_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/0/frame_2_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/0/frame_3_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/0/frame_4_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/0/frame_5_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/0/frame_6_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/0/frame_7_delay-0.1s.png'))
        if degree == "down":
            self.sprites.clear()
            self.sprites.append(pygame.image.load('objects/animations/Walk/2/frame_0_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/2/frame_1_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/2/frame_2_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/2/frame_3_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/2/frame_4_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/2/frame_5_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/2/frame_6_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/2/frame_7_delay-0.1s.png'))
        if degree == "right":
            self.sprites.clear()
            self.sprites.append(pygame.image.load('objects/animations/Walk/1/frame_0_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/1/frame_1_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/1/frame_2_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/1/frame_3_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/1/frame_4_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/1/frame_5_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/1/frame_6_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/1/frame_7_delay-0.1s.png'))
        if degree == "left":
            self.sprites.clear()
            self.sprites.append(pygame.image.load('objects/animations/Walk/3/frame_0_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/3/frame_1_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/3/frame_2_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/3/frame_3_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/3/frame_4_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/3/frame_5_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/3/frame_6_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Walk/3/frame_7_delay-0.1s.png'))
        if degree == "right-Run":
            self.sprites.clear()
            self.sprites.append(pygame.image.load('objects/animations/Run/1/frame_00_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/1/frame_01_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/1/frame_02_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/1/frame_03_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/1/frame_04_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/1/frame_05_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/1/frame_06_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/1/frame_07_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/1/frame_08_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/1/frame_09_delay-0.1s.png'))
        if degree == "left-Run":
            self.sprites.clear()
            self.sprites.append(pygame.image.load('objects/animations/Run/3/frame_00_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/3/frame_01_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/3/frame_02_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/3/frame_03_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/3/frame_04_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/3/frame_05_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/3/frame_06_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/3/frame_07_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/3/frame_08_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/3/frame_09_delay-0.1s.png'))
        if degree == "down-Run":
            self.sprites.clear()
            self.sprites.append(pygame.image.load('objects/animations/Run/2/frame_00_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/2/frame_01_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/2/frame_02_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/2/frame_03_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/2/frame_04_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/2/frame_05_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/2/frame_06_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/2/frame_07_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/2/frame_08_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/2/frame_09_delay-0.1s.png'))
        if degree == "up-Run":
            self.sprites.clear()
            self.sprites.append(pygame.image.load('objects/animations/Run/0/frame_00_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/0/frame_01_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/0/frame_02_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/0/frame_03_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/0/frame_04_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/0/frame_05_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/0/frame_06_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/0/frame_07_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/0/frame_08_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/0/frame_09_delay-0.1s.png'))
        if degree == "down-left-Run":
            self.sprites.clear()
            self.sprites.append(pygame.image.load('objects/animations/Run/4/frame_00_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/4/frame_01_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/4/frame_02_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/4/frame_03_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/4/frame_04_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/4/frame_05_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/4/frame_06_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/4/frame_07_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/4/frame_08_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/4/frame_09_delay-0.1s.png'))
        if degree == "up-left-Run":
            self.sprites.clear()
            self.sprites.append(pygame.image.load('objects/animations/Run/m1/frame_00_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/m1/frame_01_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/m1/frame_02_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/m1/frame_03_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/m1/frame_04_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/m1/frame_05_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/m1/frame_06_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/m1/frame_07_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/m1/frame_08_delay-0.1s.png'))
            self.sprites.append(pygame.image.load('objects/animations/Run/m1/frame_09_delay-0.1s.png'))

    def collision(self):
        collision_sprites = pygame.sprite.spritecollide(self,self.obstacles,False)
        #print(collision_sprites)
        if self.degree == "left" or self.degree == "left-Run":

            for sprite in collision_sprites:
                #if self.rect.left <= sprite.rect.right + 100 and self.old_rect.left >= sprite.old_rect.left:
                if pygame.sprite.collide_mask(sprite,player):
                    #self.rect.left = sprite.rect1.right
                    self.rect.left = self.rect.left + 5
        if self.degree == "right" or self.degree == "right-Run":
    
            for sprite in collision_sprites:
                
                #if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.right:
                if pygame.sprite.collide_mask(sprite,player):
                    #self.rect.right = sprite.rect1.left
                    self.rect.right = self.rect.right - 5
        if self.degree == "down" or self.degree == "down-Run" or self.degree == "down-left" or self.degree == "down-left-Run":
        
            for sprite in collision_sprites:
                #if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.bottom:
                 if pygame.sprite.collide_mask(sprite,player):
                    #self.rect.bottom = sprite.rect1.top
                    self.rect.bottom = self.rect.bottom - 5
        if self.degree == "up" or self.degree == "up-Run" or self.degree == "up-left" or self.degree == "up-left-Run":
            for sprite in collision_sprites:
                #if self.rect.top <= sprite.rect.bottom + 150 and self.old_rect.bottom >= sprite.old_rect.bottom:
                 if pygame.sprite.collide_mask(sprite,player):
                    #self.rect.top = sprite.rect1.bottom
                    self.rect.top = self.rect.top + 5
                    

    def update(self):
        self.old_rect = self.rect.copy()
        if self.isAnimating == True:
            self.currentSprite += 0.1

            if self.currentSprite >= len(self.sprites):
                self.currentSprite = 0
                self.isAnimating = False
            
            self.image = self.sprites[int(self.currentSprite)]
        self.collision()
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
    def shoot():
        global current_weapon
        if current_weapon == 1:
            weapon_damage[0]
            return weapon_damage[0]
        if current_weapon == 3:
            weapon_damage[2]
            return weapon_damage[2]

class Floor1(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        if loc == 'Aroyo':
            self.wall3 = pygame.image.load('objects/tiles/Floors/Main/Floor1.png').convert_alpha()
        
            self.rect = self.wall3.get_rect()

            self.rect.x = 225 
            self.rect.y = 400
    def update(self):
        if loc == 'Aroyo':
            self.wall3 = pygame.image.load('objects/tiles/Floors/Main/Floor1.png').convert_alpha()
 
            self.rect = self.wall3.get_rect()

            self.rect.x = 225 
            self.rect.y = 366
class Collision_Tile(pygame.sprite.Sprite):
    def __init__(self,groups, rx, ry, image, mask, collision_rect):
        super().__init__(groups)
        self.wall1 = pygame.image.load('objects/tiles/walls/junk_walls/junk_wall1.png').convert_alpha()
        self.mask1 = pygame.image.load('objects/tiles/walls/junk_walls/junk_wall_mask.png').convert_alpha()
        self.mask2 = pygame.image.load('objects/tiles/walls/junk_walls/junk_wall_collision_rect.png').convert_alpha()
        self.rect = self.wall1.get_rect()
        
        self.mask = pygame.mask.from_surface(self.mask1)
        self.rect1 = self.mask2.get_rect()
        self.rxx = rx
        self.ryy = ry

        self.rect.x = rx#387 
        self.rect.y = ry#420
        self.rect1.x = rx#387 
        self.rect1.y = ry#420
    def update(self):
        self.old_rect = self.rect.copy()

class none_Collision_Tile(pygame.sprite.Sprite):
    def __init__(self,groups, rx, ry, image):
        super().__init__(groups)
        if loc == 'Aroyo':
            self.wall3 = pygame.image.load(image).convert_alpha()

            self.rect = self.wall3.get_rect()
            self.rxx = rx
            self.ryy = ry 
            self.rect.x = rx#320
            self.rect.y = ry
    def update(self):
        if loc == 'Aroyo':
            self.wall3 = pygame.image.load('objects/tiles/walls/junk_walls/metal_door_frame.png').convert_alpha()
 
            self.rect = self.wall3.get_rect()

            self.rect.x = self.rxx 
            self.rect.y = self.ryy

#pause menu
class PauseMenu():
    def __init__(self):
        if paused == True:
            self.menu()
        self.clicked = False

    def menu(self):
        self.p = pygame.draw.rect(screen, (0,225,100), pygame.Rect(580, 300, 295, 95))
    def update(self):
        if paused == True:   
            self.menu()
            resume_btn.update()
            exit_btn.update()
            if resume_btn.draw():
                self.clicked = True
                self.resume()
            if exit_btn.draw():
                return True
        else:
            if self.clicked == True:
                self.clicked = False
    def resume(self):
        if self.clicked == True:
            print("true")
            return True
        

class Btn(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image2 = image
        self.rx = x
        self.ry = y
        self.clicked = False
        if paused == True:
            self.menu()
    def menu(self):
        self.btn = pygame.image.load(self.image2).convert_alpha()
        self.rect = self.btn.get_rect()
        self.rect.x = self.rx
        self.rect.y = self.ry
        screen.blit(self.btn,self.rect)
        
    def update(self):
        if paused == True:
            self.menu()
        else:
            pass
    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                action = True
                self.cliked = True

            if pygame.mouse.get_pressed()[0] and self.clicked == True:
                self.cliked = False
            return action
class Pathfinder:
    def __init__(self, matrix, toBody):
        self.matrix = matrix
        self.grid = Grid(matrix=matrix)
        self.path = []

        self.ttoBody = pygame.sprite.GroupSingle(toBody)
        self.Body = toBody
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
        self.px = player.rect.x
        self.py = player.rect.y 
        end_x, end_y = self.px // 32, self.py // 32#mouse_pos[0] // 32, mouse_pos[1] // 32
        end = self.grid.node(end_x, end_y)

        # path
        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        self.path, _ = finder.find_path(start, end, self.grid)
        self.grid.cleanup()
        self.ttoBody.sprite.set_path(self.path)
        self.Body.set_path(self.path)
        # Move the rect instead of the sprite
        self.Body.rect.x = self.path[0][0]
        self.Body.rect.y = self.path[0][1]
    def update(self):
        self.ttoBody.update()
    

class Enemy(pygame.sprite.Sprite):
    def __init__(self, group, rx, ry, image_location, weapon, empty_path, id):
        super().__init__()
        self.did = 2
        self.direction = "right-down"
        
        self.isAnimating = False
        self.sprites = []
        self.sprites.append(pygame.image.load(f'{image_location}/{str(self.did)}/playerIdle (1).png'))
        self.sprites.append(pygame.image.load(f'{image_location}/{str(self.did)}/playerIdle (2).png'))
        self.sprites.append(pygame.image.load(f'{image_location}/{str(self.did)}/playerIdle (3).png'))
        self.sprites.append(pygame.image.load(f'{image_location}/{str(self.did)}/playerIdle (4).png'))
        self.sprites.append(pygame.image.load(f'{image_location}/{str(self.did)}/playerIdle (5).png'))
        self.sprites.append(pygame.image.load(f'{image_location}/{str(self.did)}/playerIdle (6).png'))
        self.sprites.append(pygame.image.load(f'{image_location}/{str(self.did)}/playerIdle (7).png'))
        self.sprites.append(pygame.image.load(f'{image_location}/{str(self.did)}/playerIdle (8).png'))
        self.sprites.append(pygame.image.load(f'{image_location}/{str(self.did)}/playerIdle (9).png'))
        self.sprites.append(pygame.image.load(f'{image_location}/{str(self.did)}/playerIdle (10).png'))
        self.sprites.append(pygame.image.load(f'{image_location}/{str(self.did)}/playerIdle (11).png'))
        self.sprites.append(pygame.image.load(f'{image_location}/{str(self.did)}/playerIdle (12).png'))
        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]

        self.clicked = False

        self.id = id

        self.rhp = 100

        self.speed = 3

        self.direction2 = pygame.math.Vector2(0,0)

        self.path = []
        self.collision_rects = []
        self.empty_path = empty_path

        self.rect = self.image.get_rect()
        self.pos = self.rect.center
        self.rxx = rx
        self.ryy = ry
        #self.rect.x = rx
        #self.rect.y = ry
        self.empty_path = empty_path

        self.path_index = 0
        
        self.degree = "down"
        self.frame = 0
        self.weapon = weapon
        self.damage = 3
        self.collision_rects = []
        self.empty_path = empty_path
        self.isShot = True
    def shoot(self):
        if self.weapon == "shotgun":
            self.damage = 10
            return self.damage
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
    def update(self):
        self.old_rect = self.rect.copy()
        self.didit = False

        if self.isAnimating == True:
            self.currentSprite += 0.1

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
        screen.blit(self.image,self.rect)
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
                self.isShot = True
                self.drawit()
                clicked = True
                action2 = True
                enemyid = self.id
                self.clicked = True
                
                return action2
        if pygame.mouse.get_pressed()[0] == 0:
            #if pygame.mouse.get_pressed()[0] and self.clicked == True:
            self.clicked = False
            enemyid = self.id
            self.drawit()
            clicked = False
            action2 = False
        
        
            return action2
            
    def drawit(self):
        if self.clicked == True:
            global enemyid
            enemyid = self.id
            global clicked
            clicked = False
            return True
        else:
            return False

matrix = [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


#tiles building
doorframe_img = 'objects/tiles/walls/junk_walls/metal_door_frame.png'

##screen setup
caps_Running = False
moveAmount = 10
moveX = 0
moveY = 0
screen_W = 1320
screen_H = 920
back = pygame.display.set_mode((screen_W,screen_H))
player = pygame.display.set_mode((screen_W,screen_H))
screen = pygame.display.set_mode((screen_W,screen_H))

pygame.display.set_caption('Fallout')

#pause menu
paused = False

#Gui gfx
pm = PauseMenu()
resume_img = "objects/Resume_Btn.png"
exit_img = "objects/Exit_Btn.png"
resume_btn = Btn(580, 300, resume_img) 
exit_btn = Btn(580, 400, exit_img) 

#location management
loc = 'Aroyo' 
#Group
all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()
item_sprites = pygame.sprite.Group()
npc_sprites = pygame.sprite.Group()
none_collision_sprites = pygame.sprite.Group()
player_g = pygame.sprite.Group()

#set Player to player
player = Player((player_g), (collision_sprites))




#Arroyo
floor_1 = none_Collision_Tile((all_sprites, none_collision_sprites), 225, 400, 'objects/tiles/Floors/Main/Floor1.png')

wall_one = Collision_Tile((all_sprites, collision_sprites), 387, 420, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

wall_two = Collision_Tile((all_sprites, collision_sprites), 227, 380, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

door_frame = none_Collision_Tile((all_sprites, none_collision_sprites), 320, 400, doorframe_img)


#worldMap


#sprite grouping
#player(all_sprites, collision_sprites)

#initialize and other shit
##Game Setup/Game Setup Variables
pygame.init()
clock = pygame.time.Clock()
bg = pygame.image.load('objects/wasteMap.png')
##Variables
#Sprites
movingSprites = pygame.sprite.Group()
#vazei ton pexti sto group-Join the player into the sprites group
clicked = False
#is running?
running = True
#location

#health
max_hp = 100
Current_hp = 100

movingSprites.add(player)
raider = Enemy((player_g), 100, 100, 'objects/animations/playerIdleSprites', 'shotgun', [],1)
movingSprites.add(raider)
pathfinder = Pathfinder(matrix, raider)
raider = Enemy((player_g), 100, 100, 'objects/animations/playerIdleSprites', 'shotgun', pathfinder.empty_path(),1)

raider2 = Enemy((player_g), 100, 100, 'objects/animations/playerIdleSprites', 'shotgun', [],2)
movingSprites.add(raider2)
pathfinder2 = Pathfinder(matrix, raider2)
raider2 = Enemy((player_g), 1000, 100, 'objects/animations/playerIdleSprites', 'shotgun', pathfinder2.empty_path(),2)
raider.id = 1
raider2.id = 2 
inCombat = False
turn = 10
ap = 10
max_ap = 10
ap_cost = 1
hp = 100
max_hp = 100
shot = False
moving = False
current_weapon = 1#1 shotgun
weapons_id = [1,2,3,4]#1shotgun, sg shells, pistol, 10mm ammo
ammount = [1,1,1,1]
weapon_damage = [30,0,10,0]
inventory = [1,2] 
inventory_amount = [1,30]
enemies_a = [raider,raider2]
enemies_b = [None, raider,raider2]
pathfinder_list = [None, pathfinder, pathfinder2]
enemies = 1
enemy_counter = 0
isFirst = True
enemyid = 0
x = (screen_W * 0.95)
y = (screen_H * 0.5)
test_var = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving = False
                player.sprites.clear()
                player.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/playerIdle (1).png'))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving = False
                player.sprites.clear()
                player.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/1/playerIdle (1).png'))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                moving = False
                player.sprites.clear()
                player.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/0/playerIdle (1).png'))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_x:
                moving = False
                player.sprites.clear()
                player.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (1).png'))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                moving = False
                player.sprites.clear()
                player.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/playerIdle-5.png'))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                moving = False
                player.sprites.clear()
                player.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/playerIdle-3.png'))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_CAPSLOCK and caps_Running == False:
                caps_Running = True
            elif event.key == pygame.K_CAPSLOCK and caps_Running == True:
                caps_Running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE and paused == False:
                paused = True
            else:
                paused = False
    raider.update()
    if loc == 'Aroyo':
        back.blit(bg, (0,0))
        enemies = 2
    #if hp == 0:
     #   running = False

    #when player clicks an enemy
    if turn == 0:
        if clicked == True:
        
            for enemy in enemies_a:
            
                if clicked == True:
                    print(shot)
                    if shot == False:
                        print('Works')
                        print('enemyid: ' + str(enemyid))
                        print('enemy.id: ' + str(enemy.id))
                        #find who he is from list
                        if enemy.id == enemyid  and enemy.clicked == True:
                            print("enemyid == enemy.id: Clicked?: " + str(enemy.clicked))
                            #is the one who got clicked?
                            #if enemy.clicked == True:
                            print("SHOT " + str(enemy.id))
                                #what weapon does the player used to shoot him?
                            if current_weapon == 1:
                                try: 
                                    enemies_b[enemyid].rhp -= weapon_damage[0]
                                    print(str(enemy.rhp))
                                    print("Clicked 111: " + str(enemy.clicked))
                                    enemy.clicked = False
                                    print("Clicked 222: " + str(enemy.clicked))
                                    clicked = False
                                except IndexError:
                                    pass
                            if enemy.rhp <= 0:
                                print(str(enemy) + 'Died')
                                enemy.sprites.clear()
                                enemy.sprites.append(pygame.image.load('objects/tiles/walls/junk_walls/junk_wall1.png'))
                                #raider.kill()
                                print(enemy)
                                print(len(enemies_a))
                                enemies_a.remove(enemies_b[enemyid])
                                enemies_b.remove(enemies_b[enemyid])
                                print(len(enemies_a))
                                inCombat = False
                                turn = 10
                                
                            ap - 5
                            shot = True
                    elif shot == True:
                        shot = False
            
    #if clicked == True:
    if bool(enemies_a):
        for enemy in enemies_a:
            pass
            #if enemy.rhp <= 0:
             #   print(str(enemy) + 'Died')
              #  enemy.sprites.clear()
               # enemy.sprites.append(pygame.image.load('objects/tiles/walls/junk_walls/junk_wall1.png'))
            #    #raider.kill()
             #   print(enemy)
             #   print(len(enemies_a))
              #  enemies_a.remove(enemy)
       #         print(len(enemies_a))
        #        inCombat = False
         #       turn = 10
          #      break
    if not bool(enemies_a):
        inCombat = False
        turn = 10
    player.animate()
    if not inCombat:
        if bool(enemies_a):
            for enemy in enemies_a:
                if enemy_counter >= len(enemies_a) - 1:
                    enemy_counter = 0
                distancex = enemies_a[enemy_counter].rect.x - player.rect.x 
                enemy_counter += 1
                if distancex < 1000 and inCombat == False:
                    inCombat = True
                    turn = 1
                    break
    if inCombat:
        if turn == 1:
            enemy_counter = 0
            isFirst = True
            for enemy in enemies_b:
                if enemy_counter >= len(enemies_a):
                    turn = 0 
                    break
                else:

                    enemy_counter += 1
                if isFirst:
                    time.sleep(.1)
                    if turn == enemy_counter:
                        pathfinder_list[enemy_counter].create_path()

                        test = raider.shoot()
                        hp -= test
                        print('did damage: ' + str(test)) 
                        print('your hp is:'+ str(hp))
                        turn = enemy_counter
                        ap = max_ap
                        isFirst = False
                else:
                    if turn == enemy_counter:
                        pathfinder_list[enemy_counter].create_path()
                        test = raider.shoot()
                        hp -= test
                        print('did damage: ' + str(test)) 
                        print('your hp is:'+ str(hp))
                        turn = enemy_counter -1
                        ap = max_ap
        if turn == 0:
        
            if moving == True:
                if ap >= ap_cost:
                    ap -= ap_cost
                else:
                    turn = 1
            if ap == 0:
                turn = 1

    pathfinder2.update()
    pathfinder.update()
    raider2.update()
    raider.animate()
    raider2.animate()
    
    player.update()
    for shack in player_g:
        player.blit(player.sprites, player.rect)
        player.blit(raider.sprites, raider.rect)
    if pm.update():
        running = False
    if pm.resume():
        print('Close')
        paused = False

    if loc != 'wordmp':
        s = pygame.Surface((400,1750))  # the size of your rect
        s.set_alpha(58)                # alpha level
        s.fill((0,155,0))           # this fills the entire surface
        screen.blit(s, (1000,0))    # (0,0) are the top-left coordinates
    if player.rect.x >= 1000:
        print('exit')
    #y += moveY
    #x += moveX
    #player.move(x,y)

    wall_one.update()
    wall_two.update()
    door_frame.update()

    pressed_keys = pygame.key.get_pressed()
    player.move(pressed_keys)
    
    for shack in all_sprites:
        if loc == 'Aroyo':
            screen.blit(floor_1.wall3, floor_1.rect)

    movingSprites.draw(screen)
    movingSprites.update()
    all_sprites.update()


    for shack in all_sprites:
        if loc == 'Aroyo':
 
            screen.blit(wall_one.wall1, wall_one.rect)
            screen.blit(wall_two.wall1, wall_two.rect)
            screen.blit(door_frame.wall3, door_frame.rect)
    

    PauseMenu().update()
    clock.tick(60)
    #raider.update()
    pygame.display.flip()
pygame.quit()
sys.exit()
        
    