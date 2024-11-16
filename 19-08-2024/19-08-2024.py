import pygame

pygame.init()

pantalla = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Mi asombroso juego de Pygame!")

pygame.mixer.init()
pygame.mixer.music.load("/home/schronding/repos/programacion_orientada_a_objetos/19-08-2024/roblox-death-sound_1.mp3")

ejecutando = True
x0, y0 = 1600, 900 / 2
x1, y1 = 0, 900 / 2
velocidad = 2


while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    rec1 = pygame.draw.rect(pantalla, (200, 200, 200), (x0, y0, 75, 75))
    rec2 = pygame.draw.rect(pantalla, (100, 100, 100), (x1, y1, 75, 75))

    x0 -= velocidad
    x1 += velocidad

    if rec1.colliderect(rec2):
        pygame.mixer.music.play()
        print("Too bad, the rectangles crashed :'c")
        

    pygame.display.update()

pygame.quit()