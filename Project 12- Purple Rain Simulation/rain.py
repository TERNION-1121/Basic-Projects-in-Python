import random
import pygame

PURPLE = (186, 84, 255)
BACKGROUND = (230, 200, 255)

WIDTH = 768
HEIGHT = 432

class RainDrop:
    def __init__(self) -> None:
        self.x = WIDTH * random.random()    # random x coordinate in range [0, WIDTH]
        self.y = random.randint(-500, -50)  # random y coordinate outside the screen

        self.length = 20 * random.random()  # random length in range [0, 20]
        
        self.yspeed = self.length * 0.1   # yspeed is proportional to the length
    
    def fall(self) -> None:
        self.y += self.yspeed
        self.yspeed += self.yspeed * 0.01   # more the speed, more the acceleration (correlates to line 17)
        
        if self.y > WIDTH:  # drop falls below the screen
            self.x = WIDTH * random.random()    # reset the    
            self.y = random.randint(-500, -50)  # position
            
            self.yspeed = self.length * 0.1

    def show(self, screen: pygame.Surface) -> None:
        stroke_width = 1 if self.length // 6 == 0 else int(self.length) // 6
        pygame.draw.line(screen, PURPLE, (self.x, self.y), (self.x, self.y + self.length), stroke_width)
