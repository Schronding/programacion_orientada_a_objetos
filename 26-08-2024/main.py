import pygame
import sys

# Initialize Pygame
pygame.init()

# Dimensions of the screen
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Colors
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Super Mario Example")

# Class for the background
class Background:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self):
        screen.blit(self.image, (0, 0))

# Class for Mario
class Mario:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5
        self.fall_speed = 0
        self.jump_height = -10
        self.max_fall_speed = 9.81  # Maximum fall speed
        self.on_ground = False

        # Define screen boundaries
        self.min_x = 0
        self.max_x = SCREEN_WIDTH - self.rect.width
        self.min_y = 0
        self.max_y = SCREEN_HEIGHT - (self.rect.height * 2.5)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.rect.x = max(self.min_x, self.rect.x)  # Ensure Mario stays within the left boundary
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.rect.x = min(self.max_x, self.rect.x)  # Ensure Mario stays within the right boundary

    def jump(self, keys):
        if keys[pygame.K_SPACE] and self.on_ground:
            self.fall_speed = self.jump_height
            self.on_ground = False

    def apply_gravity(self):
        if not self.on_ground:
            self.fall_speed += 0.5
            # Limit fall speed
            self.fall_speed = min(self.fall_speed, self.max_fall_speed)
        else:
            self.fall_speed = 0

    def update(self):
        # Ensure Mario stays within the top and bottom boundaries
        self.rect.y = min(self.max_y, self.rect.y)
        self.rect.y = max(self.min_y, self.rect.y + self.fall_speed)
        print("Y screen rect", self.rect.y)
        print("Y miny", self.max_y - 25)
        if self.rect.y == self.max_y:
            self.on_ground = True

    def draw(self):
        screen.blit(self.image, self.rect.topleft)
# Function for the main game loop

def main():
    # Create an instance of Background and Mario
    background = Background('/Users/uolivares/CLionProjects/sprites/background.jpg')  # Replace with the path to your background image
    mario = Mario('mario.png', 100, 100)  # Replace with the path to your Mario sprite

    clock = pygame.time.Clock()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        mario.move(keys)
        mario.jump(keys)
        mario.apply_gravity()
        mario.update()

        # Draw on the screen
        background.draw()
        mario.draw()

        pygame.display.flip()
        clock.tick(60)  # Limit the game to 60 FPS

# Call the main function to start the game
if __name__ == "__main__":
    main()