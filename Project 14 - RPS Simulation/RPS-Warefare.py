from time import time

import pygame

from setup import *

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(BG)

clock = pygame.time.Clock()

pygame.display.set_caption("RPS Warfare")
pygame.display.flip()

Rock.generate_objects(2)
Paper.generate_objects(2)
Scissor.generate_objects(2)


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