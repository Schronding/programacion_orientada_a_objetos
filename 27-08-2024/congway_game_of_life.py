# Rules
## 1. Underpopulation: A live cell with less than two (D if C < 2) live neighboors dies.
## 2. Overpopulation: A live cell with more than three (D if C > 3) live neighboors dies.
## 3. Survival: A live cell with two or three live neighboors remains alive (A if C == 2 || C == 3)
## 4. Reproduction: Each square adjacent to exactly three pieces gives birth to a new piece (A if C == 3)

# To import the library of pygame
import pygame
import random
import logging

# What does this exactly? Why is there a tuple of two integers inside the parentheses but I never provide anything?
pygame.init()

# This is a variable that provides a tuple of 3 zeroes, normally this would be meaningless, but as in 'pygame' we can represent colors by their numbers in ...
# ... "RGB" (Red, Green and Blue), this zeroes actually tell pygame that we have absence in all the three colors, which is the same as to saying black (the color without color).
BLACK = (0, 0, 0)

# We do the same with the color gray. It is written in uppercase because it is a global variable that is both global and constant. As 'BLACK' is the absence of all color ...
# ... and white is the presence of every color, we can safely assume that gray (the combination of 'BLACK' and white is halfway through). As the maximum value of each  ...
# ... parameter of the tuple of colors is 255 (not 256, as it is zero-indexed), half of that is about 128. 
GRAY = (128, 128, 128)

# 'YELLOW' is created by the maximum value of both red and green, but "empty" in blue. 
YELLOW = (255, 255, 0)

# These two variables are meant to represent the size of my screen. 
# It is intended that in later versions this are not constant but rather detect the size of the screen of the user that is playing. 
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

# As we intend to make the game as large as possible, we went with 5 pixels, as it is a good aproximate of both, a cell large enough to be seen, and small enough to allow ...
# ... the screen to include a lot of them. 
CELL_SIZE = 5

# We initialize both the total amount of 'COLUMS' and 'ROWS' simply by dividing the variables of our 'SCREEN_WIDTH' and 'SCREEN_HEIGHT' by the 'CELL_SIZE'. 
# As our cell is a square in the screen, in 'COLUMS' we are representing its length in the "x" axis, while in 'ROWS' its height in the "y" axis. 
# While we are using the "rounded-down" division to obtain an integer and not a float, it is not really necessary, as the divisor divides the dividend perfectly. 
# It is however a good practice, as the screen size might change, posibly breaking the functioning and/or style of our game. 
COLUMS = SCREEN_WIDTH // CELL_SIZE # 'COLUMS' = 1600 / 5 = 320
ROWS = SCREEN_HEIGHT // CELL_SIZE  # 'ROWS' = 900 / 5 = 180 

# 'FPS' refers to frame per seconds. This is a variable that can subject to a lot of change, so its value might be modified later. 
FPS = 60

# Here we initialize our screen to contain the tuple of our 'SCREEN_WIDTH' and 'SCREEN_HEIGHT', in the "x" and "y" axis respectively. 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# We initialize a variable 'clock', that it is an object of the class 'Clock'. Realize how our variable is written in lower case while at the right of our assigment sign ...
# ... (=) we have the first letter in uppercase (C) followed by parentheses ( () ). 
clock = pygame.time.Clock()

def draw_grid(inhabited_niches):
    # As each value 'niche' in 'inhabited_niches' is a tuple containing the position of the cell (in the respective number of columns and rows, not of pixels).
    # While the name 'niche' only describes a position, as the whole set 'inahbited_niches' only contains USED niches, we assume each 'niche' already has a living cell.
    # The name 'inhabit_niche', in singular, could have been used but I didn't liked how similar the variables looked in the name; it could have lead to confusion. 
    for niche in inhabited_niches:
        # As we will be adding the 'niche' with the coordinates of the point in the corner at top left, we need both a position for "x" and "y" coordinates. 
        # In the set 'inhabited_niches' we make sure we provide that structure of a tuple within the specified parameters by our screen; 0 <= x <= 'SCREEN_WIDTH' (1600 px) and ...
        # 0 <= y <= 'SCREEN_HEIGHT' (900 px). As our version works with a "manual" drawing of the cell, going outside the parameters isn't likely ... at least until we consider ...
        # ... that cells can move (entities known as gliders) so it is quite possible that a cell goes out of the screen, causing unnecessary computation and other unpredictable ...
        # ... problems. That verification will be done (if necessary) while adding cells to the set. 
        # On other subject, we can decompose the tuple 'niche' to store in which 'column_number' and 'row_number' any given cell is located. 
        column_number, row_number = niche
        # While in pygame we draw objects from its top-left point, to draw a rectangle we need the size of each 4 lines. That doesn't makes much sense to me, as by definition ...
        # ... a rectangle has 2 pairs of 2 lines of equal size, especifying how large is each size becomes redundant. In the documentation I found that ...
        # ... "rect (Rect) -- rectangle to draw, position and dimensions", it does make sense that 'upper_west_lines' are enough to draw the rectangle, but that would mean ...
        # ... that both "position" and "dimension" are equal to 'CELL_SIZE'. In fact, the definition of "position" and "dimension" are very vague to me, as I don't understand ...
        # ... what they actually mean. 
        upper_west_lines = (column_number * CELL_SIZE, row_number * CELL_SIZE)
        # The asterisk (*) operator serves as a way to separate each value of 'upper_west_lines' and provide it as arguments to the '.rect()' method. 
        # What I don't know is how those values are passed, intuition tells me that inside the tuple of 'rect' they are separated by commas; 'column_number * CELL_SIZE' being ...
        # ... "rectangle to draw" and 'row_number * CELL_SIZE' being position. That doesn't make sense to me either. 
        # The way it makes sense however, is 'upper_west_lines' are not actually lines, but points. That would make so we have in the tuple the arguments of ...
        # ... (position, width, height), the problem with that is that if that is true, then why we multiplied the number of the columns and rows by the 'CELL_SIZE'? ...
        # ... Because our cell is not 1px, but 5!. As we are talking with pixels, the number of the row or column lacks substance on their own, it is not until we multiply ...
        # ... them by 'CELL_SIZE' that we actually get the desired coordinate!
        pygame.draw.rect(screen, YELLOW, (*upper_west_lines, CELL_SIZE, CELL_SIZE))
    # Here 'row_index' simply refers to the "number" of the line we are drawing. As we are using the 'range()' function, 'row_index' can only be an integer that goes from ...
    # ... zero, to our total amount of 'ROWS', which is 180 (not inclusive). 
    for row_index in range(ROWS):
        # The use of this function is very telling: it draws lines. The arguments however are a little bit more complex. Enumerating them we have that:
        #   0. surface: Where will we draw those lines. In this case we use our 'screen'.
        #   1. color: Which color will those lines be. In this case we use 'BLACK'. 
        #   2. start_pos: Where will our lines start. In this case we start at 0 (which is our "origin", at the upper left corner of our screen). What I don't understand ...
        #      ... however is what is the second value in the tuple 'row_index * CELL_SIZE' means. It seems that the tuple draws the line both in the "x" and "y" coordinates ...
        #      ... which makes sense. On the left of our tuple we have the "true" beginning and end of our screen (0 to 'SCREEN_WIDTH') while on the right we have how spaced out ...
        #      ... our lines will be, having 5 pixels of difference between them; the first line will be in pixel 5, then 10, 15 ... and so on until 1600. 
        #   3. end_pos: Where will our lines end. In this case we finish at 'SCREEN_WIDTH' which is 1600. 
        pygame.draw.line(screen, BLACK, (0, row_index * CELL_SIZE), (SCREEN_WIDTH, row_index * CELL_SIZE))

    # We do exactly the same with a minor twist: we leave our "x" coordinates in a constant separation while on the "y" axis we start from zero to the 'SCREEN_HEIGHT'. 
    # Why we didn't put the entire drawing in a single 'for' loop? Because the amount of rows we have is different to the amount of columns ('COLUMS' != 'ROWS'). 
    # If we joined these in a single loop, we would be limited by the minimum of 'ROWS' and 'COLUMS'. 
    for column_index in range(COLUMS):
        pygame.draw.line(screen, BLACK, (column_index * CELL_SIZE, 0), (column_index * CELL_SIZE, SCREEN_HEIGHT))

def adjust_grid(positions):
    all_neighboors = set()
    new_positions = set()

    for position in positions:
        neighbors = get_neighboors(position)
        all_neighboors.update(neighbors)

        neighbors = list(filter( lambda x: x in positions, neighbors))

        if len(neighbors) in [2, 3]:
            new_positions.add(position)

    for position in all_neighboors:
        neighbors = get_neighboors(position)
        neighbors = list(filter( lambda x: x in positions, neighbors))

        if len(neighbors) == 3:
            new_positions.add(position)

    return new_positions

def get_neighboors(position):
    x, y = position
    neighboors = []
    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx > SCREEN_WIDTH:
            continue

        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy > SCREEN_HEIGHT:
                continue
            if dx == 0 and dy == 0:
                continue

            neighboors.append((x + dx, y + dy))

    return neighboors

def create_cells(number):
    return set(  [  (random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT)) for _ in range(number)  ]  )

def main():
    executing = True
    time_passing = True
    count = 0
    update_frequency = 120

    # As we have 320 'COLUMS' and 180 'ROWS', we have about 57,600 positions in which any given cell can inhabit. Checking if each of those positions or 'inhabited_niches' ...
    # ... is occupied could be really inefficient. By making use of a set we reduce the time in which we encounter any alive cell from n (or the size of input) to ...
    # ... k, or constant time. 
    inhabited_niches = set()

    while executing:
        # As the speed of the computers might change the time of execution of our game, we use the variable 'FPS' in the method 'tick' to limit the amount of actions ...
        # ... that can be executed in a single iteration of the entire 'while' loop. 
        # In other words, we can only execute 'FPS' (60) actions in a single lap of our loop. 
        # This effectively standarizes the game regardless of the speed of any given computer. 
        # Note that this doesn't means it will always run at 'FPS' speed, it can actually go lower if the computer is really slow. 
        # This limit is therefore only an upperbound. 
        clock.tick(FPS)

        if time_passing: 
            count += 1

        if count >= update_frequency:
            count = 0
            positions = adjust_grid(inhabited_niches)

        pygame.display.set_caption("Playing" if time_passing else "Paused")

        # In pygame "events" are just actions that the user does, for example pressing a key or moving the mouse. Some of those actions will be relevant to our game while ...
        # ... others will not. For that pygame creates a "queue" which follows the "FIFO" behavior; First In, First Out.  This means that actions are processed in the order ...
        # ... they arrived before being descarded. Our variable 'event' is simply the one used to represent which of all those events is currently being "observed". 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # In case the event refers to the user desire to quit, we change the boolean state of our executing variable to 'False' effectively putting and end to ...
                # ... the infinite 'while' loop above. 
                executing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                column_number = x // CELL_SIZE
                row_number = y // CELL_SIZE
                niche = (column_number, row_number)

                if niche in inhabited_niches:
                    inhabited_niches.remove(niche)
                else:
                    inhabited_niches.add(niche)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    time_passing = not time_passing

                if event.key == pygame.K_c:
                    inhabited_niches = set()
                    time_passing = False
                    count = 0

                if event.key == pygame.K_g:
                    inhabited_niches = create_cells(random.randrange(2, 10) * SCREEN_WIDTH)

        # Here we do the updating in our screen. First we fill the 'screen' with the color 'GRAY' and then we draw the lines on top of it. 
        # The order is important, if we write them in reverse, everything would be lost on the entirety of a 'GRAY' screen. 
        screen.fill(GRAY)
        draw_grid(inhabited_niches)

        # We use the method 'update()' to refresh our screen constantly. What I wander is what 'display' is; It doesn't look like a method, nor a class, nor an object. 
        # I suspect it is a public attribute of the pygame module... but what is a module in the first place? 
        pygame.display.update()

    pygame.quit()

# As python is an interpreter, it runs as "it reads". That means that if we were to import this python file into another one, it would execute it directly. 
# Why is that? I assume because when importing, python assumes you want to use the functionalities in that file, so it runs them in order to have their components ready ...
# ... and available for use. By writing the '__main__' function below, we make sure it only executes when it is run directly from the current file. 
if __name__ == "__main__":
    main()