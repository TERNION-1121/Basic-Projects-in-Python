from time import time
import pygame
from setup import *

def main():

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen.fill(BG)

    clock = pygame.time.Clock()

    pygame.display.set_caption("RPS Warfare")
    pygame.display.flip()

    Rock.init_image("images/rock.png")
    Paper.init_image("images/paper.png")
    Scissor.init_image("images/scissor.png")

    Rock.init_sound("sfx/rock_hit.mp3")
    Paper.init_sound("sfx/paper_crumple.mp3")
    Scissor.init_sound("sfx/scissor_slice.mp3")

    Rock.generate_objects(30)
    Paper.generate_objects(30)
    Scissor.generate_objects(30)


    running = True
    prev_time = time()

    while running:

        dt = time() - prev_time
        prev_time = time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BG)
        
        Rock.GROUP.update(screen, dt)
        Paper.GROUP.update(screen, dt)
        Scissor.GROUP.update(screen, dt)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()