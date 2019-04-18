import sys
import pygame

def run_game():
    pygame.init()
    screem = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('sdasdadsa')

    bg_color = (230, 230, 230)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screem.fill(bg_color)
        pygame.display.flip()

run_game()