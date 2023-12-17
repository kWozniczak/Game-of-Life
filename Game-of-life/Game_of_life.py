import pygame
import numpy as np
import time
import pickle
import buttons
import colors
import board

is_paused = False
running = True
file_name = "saved_game_state"

# Initialize Pygame
pygame.init()
 
screen = pygame.display.set_mode((board.width, board.height))
 
# Game state
game_state = np.random.choice([0, 1], size=(board.n_cells_x, board.n_cells_y), p=[0.8, 0.2])
 
def next_generation():
    global game_state
    new_state = np.copy(game_state)
 
    for y in range(board.n_cells_y):
        for x in range(board.n_cells_x):
            n_neighbors = game_state[(x - 1) % board.n_cells_x, (y - 1) % board.n_cells_y] + \
                          game_state[(x)     % board.n_cells_x, (y - 1) % board.n_cells_y] + \
                          game_state[(x + 1) % board.n_cells_x, (y - 1) % board.n_cells_y] + \
                          game_state[(x - 1) % board.n_cells_x, (y)     % board.n_cells_y] + \
                          game_state[(x + 1) % board.n_cells_x, (y)     % board.n_cells_y] + \
                          game_state[(x - 1) % board.n_cells_x, (y + 1) % board.n_cells_y] + \
                          game_state[(x)     % board.n_cells_x, (y + 1) % board.n_cells_y] + \
                          game_state[(x + 1) % board.n_cells_x, (y + 1) % board.n_cells_y]
 
            if game_state[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                new_state[x, y] = 0
            elif game_state[x, y] == 0 and n_neighbors == 3:
                new_state[x, y] = 1
 
    game_state = new_state

# Save game state
def save_game_state(game_state, file_name):
    try:
        with open(file_name, 'wb') as file:
            pickle.dump(game_state, file)
            print("Game state saved successfully.")
    except IOError:
        print("Error: Unable to save game state.")

# Load game state
def load_game_state(file_name):
    try:
        with open(file_name, 'rb') as file:
            global game_state
            game_state = pickle.load(file)
            print("Game state loaded successfully.")
            return game_state
    except (IOError, pickle.UnpicklingError):
        print("Error: Unable to load game state.")

while running:
    screen.fill(colors.white)
    board.draw_grid(screen)
    board.draw_cells(game_state, screen)
    buttons.draw_buttons(screen, is_paused)
    pygame.display.flip()
    if not is_paused:
        next_generation()
        time.sleep(1)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttons.button_x_pause_resume <= event.pos[0] <= buttons.button_x_pause_resume + buttons.button_width and buttons.button_y <= event.pos[1] <= buttons.button_y + buttons.button_height:
                is_paused = not is_paused
            elif buttons.button_x_save <= event.pos[0] <= buttons.button_x_save + buttons.button_width and buttons.button_y <= event.pos[1] <= buttons.button_y + buttons.button_height:
                save_game_state(game_state, file_name)
            elif buttons.button_x_load <= event.pos[0] <= buttons.button_x_load + buttons.button_width and buttons.button_y <= event.pos[1] <= buttons.button_y + buttons.button_height:
                load_game_state(file_name)
                board.draw_cells(game_state, screen)
            else:
                x, y = event.pos[0] // board.cell_width, event.pos[1] // board.cell_height
                game_state[x, y] = not game_state[x, y]
 
pygame.quit()
 
 