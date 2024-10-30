# maze.py

import random

# Grid dimensions
GRID_SIZE = 20  # Size of each cell
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
ROWS = SCREEN_HEIGHT // GRID_SIZE
COLS = SCREEN_WIDTH // GRID_SIZE

# Constants for the cell types
BRICK = 1
PATH = 0

def initialize_grid():
    """Initialize a grid with all cells as bricks."""
    return [[BRICK for _ in range(COLS)] for _ in range(ROWS)]

def create_random_path(grid):
    """Generate a random path on the grid."""
    x, y = random.randint(0, COLS - 1), random.randint(0, ROWS - 1)  # Start point
    grid[y][x] = PATH  # Set start cell as path

    # Randomly create a path
    for _ in range(200):  # Adjust for desired path length
        direction = random.choice(["up", "down", "left", "right"])
        if direction == "up" and y > 0:
            y -= 1
        elif direction == "down" and y < ROWS - 1:
            y += 1
        elif direction == "left" and x > 0:
            x -= 1
        elif direction == "right" and x < COLS - 1:
            x += 1
        grid[y][x] = PATH  # Mark cell as part of the path
