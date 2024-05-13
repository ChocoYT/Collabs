import configparser
import pygame
import sys, os

pygame.init()

if __name__ == '__main__':
    # Path
    path = f"{os.getcwd()}\\Collabs\\Python\\Top Down Game\\"

    # Configparser setup
    defaults = configparser.ConfigParser()
    defaults.read(f"{path}defaults.ini")

    # Setup variables
    screenWidth = int(defaults['screen']['width'])
    screenHeight = int(defaults['screen']['height'])
    FPS = int(defaults['screen']['FPS'])

    # Screen Setup
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Top Down Game")
    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((0, 0, 0))

        pygame.display.update()
        clock.tick(FPS)

# End of file
pygame.quit()
sys.exit()