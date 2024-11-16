class Cat: 
    def __init__ (self, health, x, y, picture_path):
        self.health = health
        self.x = x
        self.y = y
        self.picture = pygame.image.load(picture_path)
        self.rect = self.picture.get_rect()
        self.rect.topleft = (x, y) 
        self.hit_box = (75, 75)

    def instance(self, pantalla):
        pantalla.blit(self.picture, self.rect)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


class MageCat(Cat):
    def __init__(self, health, mana, x, y, picture):
        super().__init__(health, x, y, picture)
        self.mana = mana


class WarriorCat(Cat): 
    def __init__(self, health, attack, x, y, picture):
        super().__init__(health, x, y, picture)
        self.attack = attack

import pygame
pygame.init()
pantalla = pygame.display.set_mode((1600, 900))

pygame.display.set_caption("Cat Legacy")


ejecutando = True
velocidad = 1

michu = Cat(100, 50, 50, "20-08-2024/images/defaultCat.png")
Ragnar = WarriorCat(100, 10, 100, 100, "20-08-2024/images/warriorCat.png")
Jeneffer = MageCat(100, 100, 600, 600, "20-08-2024/images/mageCat.png")



while ejecutando:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        michu.move(-5, 0)

    if keys[pygame.K_RIGHT]:
        michu.move(5, 0)

    if keys[pygame.K_UP]:
        michu.move(0, -5)

    if keys[pygame.K_DOWN]:
        michu.move(0, 5)

    if keys[pygame.K_ESCAPE]:
        pygame.QUIT()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    michu.instance(pantalla)
    #Ragnar.instance(pantalla)
    #Jeneffer.instance(pantalla)

    pygame.display.flip()

pygame.quit()