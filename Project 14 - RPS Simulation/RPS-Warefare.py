from time import time

import pygame

from setup import *

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(BLACK)
clock = pygame.time.Clock()
pygame.display.set_caption("RPS Warfare")
pygame.display.flip()

Rock.generate_objects(20)
Paper.generate_objects(20)
Scissor.generate_objects(20)

r = Sprite("rock", (250, 250))

running = True
prev_time = time()

while running:

    dt = time() - prev_time
    prev_time = time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    r.update(screen)
    # Rock.show_all(screen)
    # Paper.show_all(screen)
    # Scissor.show_all(screen)

    # Rock.draw_centroid(screen)
    # Paper.draw_centroid(screen)
    # Scissor.draw_centroid(screen)

    # Rock.update_all(dt)
    # Paper.update_all(dt)
    # Scissor.update_all(dt)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()