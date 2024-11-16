import pygame
WIDTH = 1000
HEIGHT = 900

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
FPS = 60
PLAYABLE_SIZE = (80, 80)
CASTED_AWAY_SIZE = (40, 40)

pygame.display.set_caption("Chess")

COLUMNS = ["A", "B", "C", "D", "E", "F", "G", "H"]
ROWS = [str(number) for number in range(1, 9)]

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

white_locations = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
                   (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

black_locations = [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8),
                   (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]

captured_pieces_white = []
captured_pieces_black = []
# 0 - white's turn, no selection. 1 - white's turn, piece selected
# 2 - black's turn, no selection. 3 - black's turn, piece selected
turn_step = 0
selection = 10000
valid_moves = []

# Pieces images

white_pieces_images_raw_size = []

white_rook = pygame.image.load('images/white_rook.png')
white_knight = pygame.image.load('images/white_knight.png')
white_queen = pygame.image.load('images/white_queen.png')
white_king = pygame.image.load('images/white_king.png')
white_bishop = pygame.image.load('images/white_bishop.png')
white_pawn = pygame.image.load('images/white_pawn.png')

white_pieces_images_raw_size.extend(    [white_rook, white_knight, white_queen, white_king, white_bishop, white_pawn]   )

def scale_pieces(image_list, desired_size, scaled_image_list):
    if desired_size == 'playable':
        for item in image_list:
            item = pygame.transform.scale(item, PLAYABLE_SIZE)
            scaled_image_list.append(item)
    elif desired_size == 'casted':
        for item in image_list:
            item = pygame.transform.scale(item, CASTED_AWAY_SIZE)
            scaled_image_list.append(item)

white_pieces_images_playable_size = []
white_pieces_images_casted_size = []
scale_pieces(white_pieces_images_raw_size, 'playable', white_pieces_images_playable_size)
scale_pieces(white_pieces_images_raw_size, 'casted', white_pieces_images_casted_size)

black_pieces_images_raw_size = []

black_rook = pygame.image.load('images/black_rook.png')
black_knight = pygame.image.load('images/black_knight.png')
black_queen = pygame.image.load('images/black_queen.png')
black_king = pygame.image.load('images/black_king.png')
black_bishop = pygame.image.load('images/black_bishop.png')
black_pawn = pygame.image.load('images/black_pawn.png')

black_pieces_images_raw_size.extend(    [black_rook, black_knight, black_queen, black_king, black_bishop, black_pawn]   )

black_pieces_images_playable_size = []
black_pieces_images_casted_size = []
scale_pieces(black_pieces_images_raw_size, 'playable', black_pieces_images_playable_size)
scale_pieces(black_pieces_images_raw_size, 'casted', black_pieces_images_casted_size)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

piece_list = ['rook', 'knight', 'queen', 'king', 'bishop', 'pawn']

class Piece:
    def __init__(self, image, position):
        self.image = image
        self.position = position
    def available_movements(self):
        pass
    def movement(self):
        pass
    def draw(self):
        pass

class Square:
    def __init__(self, position_id, color):
        self.position_id = position_id
        self.color = color
        self.height = HEIGHT // 16
        self.width = self.height

class Bishop(Piece):
    def __init__(self, image, position):
        super().__init__(image, position)
        self.value = 3

class Knight(Piece):
    def __init__(self, image, position):
        super().__init__(image, position)
        self.value = 3

class Rook(Piece):
    def __init__(self, image, position):
        super().__init__(image, position)
        self.value = 5

class Queen(Piece):
    def __init__(self, image, position):
        super().__init__(image, position)
        self.value = 9

class King(Piece):
    def __init__(self, image, position):
        super().__init__(image, position)

def draw_table(rows, columns):
    squares = []
    for index in range(max(len(rows), len(columns))):
        position_id = columns[index] + rows[index]
        if index % 2 == 0:
            color = BLACK
        else:
            color = WHITE
        squares.append(Square(position_id, color))
    return squares

def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
        status_text = ["White: Select a Piece to Move!", "White: Select a Destination!", 
                      "Black: Select a Piece to Move!", "Black: Select a Destination!"]
        # We will be looping over and over over this 'status_text' as the nature of chess is a cyclical back and forth; turn based game. 
        screen.blit(    big_font.render(    status_text[turn_step], True, BLACK), (20, 820))
        for index in range(9):
            pygame.draw.line(screen, BLACK, (0, 100 * index), (800, 100 * index), 2)
            pygame.draw.line(screen, BLACK, (100 * index, 0), (100 * index, 800), 2)
def draw_pieces():
    for i in range(len( white_pieces )):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == "pawn":
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
            # The 22 is just a offset value
        else:
            screen.blit(white_pieces_images_playable_size[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))

        for i in range(len( black_pieces )):
            index = piece_list.index(black_pieces[i])
            if black_pieces[i] == "pawn":
                screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
                # The 22 is just a offset value
            else:
                screen.blit(black_pieces_images_playable_size[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))

run = True
while run:
    timer.tick(FPS)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()