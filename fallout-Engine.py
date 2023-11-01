import pygame
from pygame.locals import *
import os

screen = pygame.display.set_mode((1320, 920))
pygame.init()

class Pointer(pygame.sprite.Sprite):
    def __init__(self, x, y, name, id):
        super().__init__()
        self.build_selected = build
        self.rect = self.build_selected.get_rect()
        self.x,self.y = x,y
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        self.exist = True
        self.iid = id
        self.name = name
    def update(self):
        self.pos = pygame.mouse.get_pos()
        #self.rect.x = self.x
        #self.rect.y = self.y
        if self.exist == True:
            screen.blit(self.build_selected, self.rect)
        
            
    def follow(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
    def building(self):
        global count
        
        object_name = Buildit(self.pos[0],self.pos[1], count, count)
        count += 1
        if object_name.build_selected == five:
            floors.append(object_name)
        else:
            objects.append(object_name) 
class item(pygame.sprite.Sprite):
    def __init__(self, image, name):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.name = name


class Buildit(pygame.sprite.Sprite):
    def __init__(self, x, y, name, iid):
        super().__init__()
        
        self.build_selected = build
        self.rect = self.build_selected.get_rect()
        self.x,self.y = x,y
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        self.exist = True
        self.iid = iid
        self.name = name
        self.fontt = pygame.font.Font(None, 36)
        self.text_surface = self.fontt.render(str(self.iid), True, (255, 255, 255))
        
        
    def update(self):
        self.pos = pygame.mouse.get_pos()
        #self.rect.x = self.x
        #self.rect.y = self.y
        if self.exist == True:
            screen.blit(self.build_selected, self.rect)
            screen.blit(self.text_surface, (self.x,self.y))
        
        xxpos = pygame.mouse.get_pos()
            
        if self.rect.collidepoint(xxpos):
            if pygame.mouse.get_pressed()[2] == 1 and self.clicked == False:
                if self.name != 'main':
                    self.exist = False
                print(objects)
                objects.remove(self)
                self.clicked = True
                print(objects)
            if pygame.mouse.get_pressed()[2] == 0:
                self.clicked = False

class building_mode_on(pygame.sprite.Sprite):
    def __init__(self, inv_list):
        super().__init__()
        self.toggled = False
        
        self.inv_list = inv_list
        self.list_position = (1320/2 - 699/2, 920/2 - 577/2)
        self.list_size = (120, 420)
        self.list_font = pygame.font.SysFont(None, 24)
        self.list_item_height = 30
        self.box_position = (1320/2 - 699/2, 920/2 - 577/2)
        self.box_size = (120, 420)
        self.box_color = (255, 255, 255)
        self.box_thickness = 2
        self.clickable_rects = []
        self.list_font = pygame.font.SysFont('fallouty', 24)
        self.clicked1 = False
        self.clicked2 = False
        self.clicked3 = False
        self.clicked4 = False
        self.clicked5 = False
        self.clicked6 = False
        self.clicked7 = False
        self.clicked8 = False
        self.clicked9 = False
        self.button1down = False
        self.button2down = False
        self.search_ammo = False
        self.isOnUsing = False
        self.isOnInv = False
        self.cooldown = 500
        self.display_use = False
        self.display_use2 = False
        self.item_id = 1
        self.item_is = None
        self.ammo_name = None
        self.weapon_ammo_need = None
        self.item_reload = None
        
    def toggle_on(self):
        #self.invbox = pygame.transform.scale(pygame.image.load('objects/ui/inv/inv.png'), (899,777))
        #self.rect = self.invbox.get_rect()
        #self.rect.x = 1320/2 - 899/2
        #self.rect.y = 920/2 - 777/2
        
        #manager = pygame_gui.UIManager(screen_size)
        #cont = manager.get_root_container() 
        #self.button_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screen_W/2-199, screen_H/2-163), (100, 50)),
         #                               text='exit', manager=manager,
          #                              container=cont,
           #                             anchors={'bottom': 'bottom',
            #                                     'top': 'top'})

        # Calculate the visible items within the box
              # New list to store clickable regions

        x, y = 1320/2 - 699/2 - 30, 920/2 - 577/2 + 450
        x2,y2 = 1320/2 - 699/2 + 200, 920/2 - 577/2 + 530
        global current_page 
        global itemsList
        global inventory_width
        global inventory_height
        global using_item
        item_spacing = 10
        item_count = len(itemsList)
        start_index = current_page * inventory_width * inventory_height
        end_index = min(start_index + (inventory_width * inventory_height), item_count)

        for i in range(start_index, end_index):
            item = itemsList[i]
            item_rect = item.image.get_rect().move(x, y)
            
            screen.blit(item.image, (x, y))

            if item_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked1 == False:
                    
                    #self.cooldown = 0
                    #if self.cooldown == 0:
                     #   pass
                    #self.displayoptionsonmouse(item)
                    self.handle_item_click(item)
                    self.clicked1 = True
                if pygame.mouse.get_pressed()[0] == 0:
                    #self.cooldown = 500
                    self.clicked1 = False
            if item_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[2] == 1 and self.clicked4 == False:
                    self.cooldown -= 100
                    if self.cooldown <= 0:
                        self.item_id = i
                        self.item_is = item
                        self.display_use = True
                        self.displayoptionsonmouse(item)
                        self.clicked4 = True
                if pygame.mouse.get_pressed()[2] == 0:
                    self.display_use = False
                    self.cooldown = 500
                    self.clicked4 = False
                    
            x += item.image.get_width() + item_spacing
            if (i + 1) % inventory_width == 0:
                x -= 140
                y += item.image.get_height() + item_spacing

        # Draw navigation buttons
        if self.button1down == True:
            self.invupout = pygame.image.load('objects/ui/inv/INVDNIN.png')
        else:
            self.invupout = pygame.image.load('objects/ui/inv/INVDNOUT.png')
        next_button_rect = self.invupout.get_rect()
        next_button_rect.x = 1320/2 - 699/2 - 130
        next_button_rect.y = 920/2 - 577/2 + 250 + 250
        screen.blit(self.invupout, next_button_rect)
        if self.button2down == True:
            self.invdownout = pygame.image.load('objects/ui/inv/INVUPIN.png')
        else:
            self.invdownout = pygame.image.load('objects/ui/inv/INVUPDS.png')
        prev_button_rect = self.invupout.get_rect()
        prev_button_rect.x = 1320/2 - 699/2 - 130
        prev_button_rect.y = 920/2 - 577/2 + 200 + 250
        screen.blit(self.invdownout, prev_button_rect)
        #next_button_rect = pygame.Rect(700, 500, 80, 40)
        #pygame.draw.rect(screen, (255, 0, 0), next_button_rect)
        #pygame.draw.rect(screen, (0, 0, 0), next_button_rect, 3)
        #pygame.draw.polygon(screen, (0, 0, 0), ((720, 515), (720, 525), (730, 520)))
        #prev_button_rect = pygame.Rect(700, 420, 80, 40)
        #pygame.draw.rect(screen, (255, 0, 0), prev_button_rect)
        #pygame.draw.rect(screen, (0, 0, 0), prev_button_rect, 3)
        #pygame.draw.polygon(screen, (0, 0, 0), ((720, 445), (720, 435), (710, 440)))

        # Check for button clicks
        if next_button_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked2 == False:
                self.clicked2 = True
                self.button1down = True
                if item_count > 1:
                    current_page = (current_page + 1) % ((item_count - 1) // (inventory_width * inventory_height) + 1)
            if pygame.mouse.get_pressed()[0] == 0:
                self.button1down = False
                self.clicked2 = False
        elif prev_button_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked3 == False:
                self.button2down = True
                self.clicked3 = True
                if item_count > 1:
                    current_page = (current_page - 1) % ((item_count - 1) // (inventory_width * inventory_height) + 1)
            if pygame.mouse.get_pressed()[0] == 0:
                self.button2down = False
                self.clicked3 = False
    def handle_item_click(self, item):
        global build
        if item.name == 1:
            
            build = one
        elif item.name == 2:
            build = two
        elif item.name == 3:
            build = three
        elif item.name == 4:
            build = fore
        elif item.name == 5:
            build = five
        elif item.name == 6:
            build = six




# Open the file in write mode and write the content

count = 0
file_path = os.path.join(os.getcwd(), 'map'+ str(count)+ '.py')
object_name = 'object' + str(count)
start = 'import main \n'
screen_W = 1320
screen_H = 920

floor = pygame.Surface((1000, 900))
walls = pygame.Surface((1000, 900))

one = pygame.image.load('objects/tiles/walls/junk_walls/junk_wall1.png')
two = pygame.image.load('objects/tiles/walls/junk_walls/metal_door_frame.png')
three = pygame.image.load('objects/tiles/walls/junk_walls/metal_wall.png')
fore = pygame.image.load('objects/tiles/walls/junk_walls/junk_wall1b.png')
five = pygame.image.load('objects/tiles/Floors/Main/Floor1.png')
six = pygame.image.load('objects/tiles/walls/scenery/car_junk.png')
build = one
floors = []
objects = [Buildit(227, 380, 'wh', -2)]


main = Pointer(0,0, 'main', -1)
running = True
prefab = ''
prList = []
clicked = False
showWall = True
control = False
question = ''
objectsList = []
objectlist = f'objects = {str(objectsList)}'
building_mode = True
item1 = item('objects/tiles/walls/junk_walls/junk_wall1.png', 1)
item2 = item('objects/tiles/walls/junk_walls/metal_door_frame.png', 2)
item3 = item('objects/tiles/walls/junk_walls/metal_wall.png', 3)
item4 = item('objects/tiles/walls/junk_walls/junk_wall1b.png', 4)
item5 = item('objects/tiles/Floors/Main/Floor1.png', 5)
item6 = item('objects/tiles/walls/scenery/car_junk.png', 6)

itemsList = [item1,item2,item3,item4,item5,item6]
current_page = 0

inventory_width = 10
inventory_height = 1

bmo = building_mode_on(itemsList)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                build = one
                main.build_selected = build
            if event.key == pygame.K_2:
                build = two
                main.build_selected = build
            if event.key == pygame.K_3:
                build = three
                main.build_selected = build
            if event.key == pygame.K_4:
                build = fore
                main.build_selected = build
            if event.key == pygame.K_5:
                build = five
                main.build_selected = build
            if event.key == pygame.K_LCTRL:
                control = True
            if event.key == pygame.K_s and control == True:
                question = str(input('save as {name}:'))
                file_path = os.path.join(os.getcwd(), question + str(count)+ '.py')
                with open(file_path, "w") as file:
                    objectlist = f'objects = {str(objectsList)}'
                    file.writelines(start)
                    for object in prList:
                        line = f'{object}\n'
                        file.writelines(line)
                    file.writelines(objectlist)
                    print(objectsList)
                    control = False 
            if event.key == pygame.K_b:
                if building_mode == False:
                    building_mode = True
                else:
                    building_mode = False
         
            if event.key == pygame.K_F6:
                if showWall == True:
                    showWall = False
                else:
                    showWall = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LCTRL:
                control = False
    
        if pygame.mouse.get_pressed()[0] == 1 and clicked == False and building_mode == True:
            
            
            main.building()
            prList.append(prefab)
            objectsList.append('wall_' + str(count))
            clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            clicked = False
            #with open(file_path, "w") as file:
             #   file.write(str(prList))
        #if event.type == pygame.MOUSEBUTTONDOWN
    main.build_selected = build  
    screen.blit(pygame.image.load('objects/wasteMap.png'),(0,0))
    for object in objects:
        object.update()
    if building_mode:
        main.update()
        main.follow()
    if build == one:
        prefab = f'''wall_{str(count)} = main.Collision_Tile((main.all_sprites, main.collision_sprites), {str(main.pos)}, "objects/tiles/walls/junk_walls/junk_wall1.png","objects/tiles/walls/junk_walls/junk_wall_mask.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
                '''
    elif build == two:
        prefab = f'''wall_{str(count)} = main.none_Collision_Tile((main.all_sprites, main.none_collision_sprites), {str(main.pos)}, "objects/tiles/walls/junk_walls/metal_door_frame.png")
                '''
    elif build == three:
        prefab = f'''wall_{str(count)} = main.Collision_Tile((main.all_sprites, main.collision_sprites), {str(main.pos)}, "objects/tiles/walls/junk_walls/metal_wall.png","objects/tiles/walls/junk_walls/metal_wall_mask.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
                '''

    elif build == fore:
        prefab = f'''wall_{str(count)} = main.Collision_Tile((main.all_sprites, main.collision_sprites), {str(main.pos)}, "objects/tiles/walls/junk_walls/junk_wall1b.png","objects/tiles/walls/junk_walls/junk_wall_mask_b.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
                '''
    elif build == five:
        prefab = f'''wall_{str(count)} = main.none_Collision_Tile((main.all_sprites, main.none_collision_sprites), {str(main.pos)}, "objects/tiles/Floors/Main/Floor1.png")
                '''
    elif build == six:
        prefab = f'''wall_{str(count)} = main.none_Collision_Tile((main.all_sprites, main.none_collision_sprites), {str(main.pos)}, "objects/tiles/walls/scenery/car_junk.png")
                '''
                
    for floor in floors:
        screen.blit(floor.build_selected,floor.rect)
    for object in objects:
        if showWall != False:
            screen.blit(object.build_selected, object.rect)
            screen.blit(object.text_surface, (object.x,object.y))
    if showWall == False:
        for object in objects:
            object.exist = False
    else:
        for object in objects:
            object.exist = True

    bmo.toggle_on()
    bmo.update()
    pygame.display.flip()
        