import pygame
import random

# --- CONFIGURATION & CONSTANTS ---
pygame.init() # Initializes all Pygame modules. Returns (successes, failures).

# Colors are defined as tuples of Red, Green, Blue (0-255).
BLACK = (0, 0, 0)       # Absence of color
GRAY = (128, 128, 128)  # Mid-point intensity
YELLOW = (255, 255, 0)  # Red + Green = Yellow

# Screen dimensions in pixels.
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

# Size of one "living" square in pixels.
CELL_SIZE = 5

# Calculate how many cells fit in the screen. 
# Floor division (//) ensures we get a whole number (integer).
COLUMNS = SCREEN_WIDTH // CELL_SIZE 
ROWS = SCREEN_HEIGHT // CELL_SIZE  

# Frames Per Second: How fast the game loop cycles.
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def draw_grid(inhabited_niches):
    """
    Draws the living cells and the grid lines on the screen.
    inhabited_niches: A set of tuples (x, y) representing grid coordinates.
    """
    
    # 1. Draw the Living Cells
    for niche in inhabited_niches:
        col_num, row_num = niche
        
        # To draw a rectangle, Pygame needs a tuple of 4 numbers: (x, y, width, height).
        # We multiply the column/row index by CELL_SIZE to convert "Grid Coordinates" (e.g., Col 5)
        # into "Pixel Coordinates" (e.g., Pixel 25).
        top_left_x = col_num * CELL_SIZE
        top_left_y = row_num * CELL_SIZE
        
        # The arguments are: Surface, Color, (x, y, width, height)
        rect_definition = (top_left_x, top_left_y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, YELLOW, rect_definition)

    # 2. Draw the Grid Lines (Optional: Can be commented out for performance on large grids)
    # Draw horizontal lines
    for row in range(ROWS):
        # Line from (0, y) to (Screen_Width, y)
        y = row * CELL_SIZE
        pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))

    # Draw vertical lines
    for col in range(COLUMNS):
        # Line from (x, 0) to (x, Screen_Height)
        x = col * CELL_SIZE
        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))


def get_neighbors(position):
    """
    Returns a list of the 8 neighbors around a specific (x, y) position.
    """
    x, y = position
    neighbors = []
    
    # Check offsets: -1 (left/up), 0 (same), 1 (right/down)
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            # Skip the cell itself (0, 0)
            if dx == 0 and dy == 0:
                continue
            
            # Create the neighbor coordinate
            neighbor_x = x + dx
            neighbor_y = y + dy

            # Check boundaries so we don't look outside the screen
            if 0 <= neighbor_x < COLUMNS and 0 <= neighbor_y < ROWS:
                neighbors.append((neighbor_x, neighbor_y))
                
    return neighbors


def adjust_grid(current_living_cells):
    """
    Calculates the next generation based on Conway's Rules.
    Returns a NEW set of living cells.
    """
    # A set allows us to avoid duplicates automatically.
    potential_births = set()
    next_generation = set()

    # PART 1: Check currently living cells (Survival Rule)
    for cell in current_living_cells:
        neighbors = get_neighbors(cell)
        potential_births.update(neighbors) # Add neighbors to list of candidates for birth
        
        # Count how many neighbors are currently alive
        alive_neighbors_count = 0
        for n in neighbors:
            if n in current_living_cells:
                alive_neighbors_count += 1

        # Rule: Survive if 2 or 3 neighbors
        if alive_neighbors_count == 2 or alive_neighbors_count == 3:
            next_generation.add(cell)

    # PART 2: Check empty spots near living cells (Reproduction Rule)
    for cell in potential_births:
        # We only care about dead cells here (live ones were checked above)
        if cell in current_living_cells:
            continue
            
        neighbors = get_neighbors(cell)
        alive_neighbors_count = 0
        for n in neighbors:
            if n in current_living_cells:
                alive_neighbors_count += 1
        
        # Rule: Dead cell becomes alive if exactly 3 neighbors
        if alive_neighbors_count == 3:
            next_generation.add(cell)

    return next_generation


def create_random_cells(number_of_cells):
    """Generates a random set of starting positions."""
    new_set = set()
    for _ in range(number_of_cells):
        # random.randrange(Start, Stop)
        # Note: We must use COLUMNS/ROWS, not SCREEN_WIDTH/HEIGHT
        x = random.randrange(0, COLUMNS)
        y = random.randrange(0, ROWS)
        new_set.add((x, y))
    return new_set


def main():
    executing = True
    time_passing = False # Start paused so we can draw
    
    # State variable: Tracks if the mouse is currently held down
    is_dragging = False 
    
    # The set that holds our data. (x, y) tuples.
    inhabited_niches = set()

    while executing:
        # 1. Control Speed
        clock.tick(FPS)
        
        # 2. Window Title
        state_msg = "Playing" if time_passing else "Paused (Space to Play, C to Clear, G to Generate)"
        pygame.display.set_caption(f"Game of Life - {state_msg}")

        # 3. Input Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executing = False

            # KEYBOARD EVENTS
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    time_passing = not time_passing # Toggle pause
                
                if event.key == pygame.K_c: # C for Clear
                    inhabited_niches = set()
                    time_passing = False
                
                if event.key == pygame.K_g: # G for Generate
                    # Generate ~10% fill rate
                    inhabited_niches = create_random_cells(int(COLUMNS * ROWS * 0.1))

            # MOUSE EVENTS (Drawing)
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_dragging = True # Start drawing
                # Draw the first pixel immediately
                x, y = pygame.mouse.get_pos()
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                inhabited_niches.add((col, row))
            
            if event.type == pygame.MOUSEBUTTONUP:
                is_dragging = False # Stop drawing

            if event.type == pygame.MOUSEMOTION:
                if is_dragging:
                    x, y = pygame.mouse.get_pos()
                    col = x // CELL_SIZE
                    row = y // CELL_SIZE
                    inhabited_niches.add((col, row))

        # 4. Game Logic (Update)
        # Only calculate next frame if the game is unpaused
        if time_passing:
            # We must save the result back into our variable!
            inhabited_niches = adjust_grid(inhabited_niches)

        # 5. Drawing (Render)
        screen.fill(GRAY) # Wipe the screen
        draw_grid(inhabited_niches) # Draw new state
        pygame.display.update() # Flip the buffer to show the user

    pygame.quit()


if __name__ == "__main__":
    main()