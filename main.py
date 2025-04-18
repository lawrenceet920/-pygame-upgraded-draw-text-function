# Ethan Lawrence 
# Feb 12 2025
# Pygame template ver 2

import pygame
import sys
import config
import random

def init_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events(x1, y1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return x1, y1, False
    
    # Move keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                y1 -=10
            if keys[pygame.K_DOWN]:
                y1 +=10
            if keys[pygame.K_LEFT]:
                x1 -=10
            if keys[pygame.K_RIGHT]:
                x1 +=10
    return x1, y1, True
def main():
    screen = init_game()
    clock = pygame.time.Clock()
    running = True

    #  FONT
    basic_fontname = 'FreeMono.ttf'
    custom_fontname = 'PixelifySans-VariableFont_wght.ttf'
    fsize_normal = 36
    fsize_italic = 30
    fsize_custom = 48

    fpos1 = (random.randint(0, 400), random.randint(0, 300))
    fpos2 = (random.randint(0, 400), random.randint(200, 500))
    x1, y1 = (random.randint(200, 600), random.randint(200, 500))
    
    while running:
        x1, y1, running = handle_events(x1, y1)
        screen.fill(config.WHITE)

        draw_text(screen, 'Regular Text', fsize_normal, config.BLACK, fpos1)
        draw_text(screen, 'Oddish', fsize_italic, config.CYAN, fpos2, font_name=basic_fontname, bold=True, italic=True)
        draw_text(screen, 'Abnormal', fsize_custom, config.PURPLE, (x1, y1), custom_fontname, rotation=50)

        # Next frame
        pygame.display.flip()
        clock.tick(config.FPS)
    pygame.quit()
    sys.exit()

# Nonstandard Functions

def draw_text(screen, text, font_size, color, position, font_name='FreeMono.ttf', antianiased=True, bold=False, italic=False, rotation=0):
    font = pygame.font.Font(font_name, font_size)
    font.set_bold(bold)
    font.set_italic(italic)

    textsurface = font.render(text, antianiased, color)
    textsurface = pygame.transform.rotate(textsurface, rotation)
    screen.blit(textsurface, position)


if __name__ == '__main__':
    main()