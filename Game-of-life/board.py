import pygame
import colors

# Screen dimensions
width, height = 800, 600

# Grid dimensions
n_cells_x, n_cells_y = 40, 30
cell_width = width // n_cells_x
cell_height = height // n_cells_y

def draw_grid(screen):
    for y in range(0, height, cell_height):
        for x in range(0, width, cell_width):
            cell = pygame.Rect(x, y, cell_width, cell_height)
            pygame.draw.rect(screen, colors.gray, cell, 1)

def draw_cells(game_state, screen):
    for y in range(n_cells_y):
        for x in range(n_cells_x):
            cell = pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height)
            if game_state[x, y] == 1:
                pygame.draw.rect(screen, colors.black, cell)