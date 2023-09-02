import pygame
import random

SCREEN_DIM = 500
BLUE = (115, 170, 235)
GREEN = (140, 235, 60)

class Walker:
    def __init__(self) -> None:
        self.position = pygame.math.Vector2(SCREEN_DIM / 2, SCREEN_DIM / 2)

    def update_position(self) -> None:
        if not 0 < self.position.x < SCREEN_DIM or not 0 < self.position.y < SCREEN_DIM:
            self.position.x = SCREEN_DIM / 2
            self.position.y = SCREEN_DIM / 2

        self.position.x += random.uniform(-1, 1)
        self.position.y += random.uniform(-1, 1)
    
    def show(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, GREEN, self.position, 1)