import pygame
import colors
import board

# Button dimensions
button_width, button_height = 150, 50
button_y = board.height - button_height - 10
button_x_pause_resume  = 100
button_x_save = 300
button_x_load = 500

def draw_buttons(screen, is_paused):
    draw_pause_resume_button(screen, is_paused)
    draw_save_button(screen)
    draw_load_button(screen)

def draw_pause_resume_button(screen, is_paused):
    pygame.draw.rect(screen, colors.green, (button_x_pause_resume, button_y, button_width, button_height))
    font = pygame.font.Font(None, 36)
    text = font.render("Resume" if is_paused else "Pause", True, colors.black)
    text_rect = text.get_rect(center=(button_x_pause_resume + button_width // 2, button_y + button_height // 2))
    screen.blit(text, text_rect)

def draw_save_button(screen):
    pygame.draw.rect(screen, colors.pink, (button_x_save, button_y, button_width, button_height))
    font = pygame.font.Font(None, 36)
    text = font.render("Save", True, colors.black)
    text_rect = text.get_rect(center=(button_x_save + button_width // 2, button_y + button_height // 2))
    screen.blit(text, text_rect)

def draw_load_button(screen):
    pygame.draw.rect(screen, colors.blue, (button_x_load , button_y, button_width, button_height))
    font = pygame.font.Font(None, 36)
    text = font.render("Load", True, colors.black)
    text_rect = text.get_rect(center=(button_x_load  + button_width // 2, button_y + button_height // 2))
    screen.blit(text, text_rect)
