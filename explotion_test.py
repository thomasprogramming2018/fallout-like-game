import pygame
from pygame.locals import *

class explotion(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.isAnimating = False
        self.sprites = []
        for i in range(1,10):
            self.sprites.append(pygame.image.load(f"objects/cut_scene01/000{i}.png"))
        for r in range(10,100):
            self.sprites.append(pygame.image.load(f"objects/cut_scene01/00{r}.png"))
        for r in range(100,150):
            self.sprites.append(pygame.image.load(f"objects/cut_scene01/0{r}.png"))
        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]
        self.rect = self.image.get_rect()
    def animate(self):
        self.isAnimating = True
    def update(self):
        self.old_rect = self.rect.copy()
            

        if self.isAnimating == True:
            self.currentSprite += 0.04

            if self.currentSprite >= len(self.sprites):
                self.currentSprite = 0
                self.isAnimating = False
        self.image = self.sprites[int(self.currentSprite)]

screen = pygame.display.set_mode((700,700))

pygame.init()

ex = explotion()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
    ex.update()
    ex.animate()
    screen.blit(ex.image, ex.rect)
    pygame.display.flip()