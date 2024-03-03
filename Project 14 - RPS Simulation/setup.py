from math import cos, sin, pi
from random import random, uniform

import pygame 
from pygame import Vector2

# colors
WHITE = (255, 255, 255)
BG = (25, 25, 25)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_SIZE = (500, 500)

SPRITE_SIZE = (20, 20)

class Mover(pygame.sprite.Sprite):
    COLOR = WHITE
    GROUP = pygame.sprite.Group()

    def __init__(self, path: str, pos = None) -> None:
        super().__init__()

        self.position = Vector2(pos) if pos else Mover.rand_pos(SCREEN_SIZE)
        self.velocity = Mover.random_vector() * 20
        self.acceleration = Mover.random_vector() * 10

        self.image = pygame.transform.scale(pygame.image.load(f"{path}.png").convert_alpha(), SPRITE_SIZE)

    def update(self, screen: pygame.Surface, dt: int) -> None:
        self.position += self.velocity * dt
        self.check_screen_bounds(SCREEN_SIZE)

        enemy_position = Vector2(GRAPH[self.__class__.__name__].get_nearest_vector(self.position))
        self.acceleration += (enemy_position - self.position)
        Mover.limit_vector(self.acceleration, 20)

        self.velocity += self.acceleration * dt
        Mover.limit_vector(self.velocity, 40)

        screen.blit(self.image, self.image.get_rect(center=self.position))

    def check_screen_bounds(self, screen_dim: tuple):
        width, height = screen_dim

        if self.position.x <= 10 or self.position.x > width - 10:
            self.velocity.x *= -1
        if self.position.y <= 10 or self.position.y > height - 10:
            self.velocity.y *= -1
    
    @staticmethod
    def limit_vector(vector: Vector2, length) -> None:
        if vector.magnitude() > length:
            vector.scale_to_length(length)

    @staticmethod
    def random_vector() -> Vector2:
        angle = uniform(0, 2 * pi)
        return Vector2(cos(angle), sin(angle))

    @staticmethod
    def rand_pos(screen_dim: tuple[int, int]) -> Vector2:
        return Vector2(random() * (screen_dim[0] - 10), random() * (screen_dim[1] - 10))

    @classmethod
    def generate_objects(cls, n: int) -> None:
        for _ in range(n):
            cls()

    @classmethod
    def get_nearest_vector(cls, v: Vector2) -> Vector2:
        min_distance = Vector2(SCREEN_SIZE).length()
        to_return = v

        for sprite in cls.GROUP:
            if (current_distance := v.distance_to(sprite.position)) < min_distance:
                min_distance = current_distance 
                to_return = sprite.position
        return to_return

class Rock(Mover):
    COLOR = RED
    GROUP = pygame.sprite.Group()
    
    def __init__(self, pos = None) -> None:
        super().__init__("rock", pos)
        Rock.GROUP.add(self)

    @classmethod
    def generate_objects(cls, n: int) -> None:
        super(Rock, cls).generate_objects(n)

class Paper(Mover):
    COLOR = GREEN
    GROUP = pygame.sprite.Group()

    def __init__(self, pos = None) -> None:
        super().__init__("paper", pos)
        Paper.GROUP.add(self)

    @classmethod
    def generate_objects(cls, n: int) -> None:
        super(Paper, cls).generate_objects(n)

class Scissor(Mover):
    COLOR = BLUE
    GROUP = pygame.sprite.Group()

    def __init__(self, pos = None) -> None:
        super().__init__("scissor", pos)
        Scissor.GROUP.add(self)

    @classmethod
    def generate_objects(cls, n: int) -> None:
        super(Scissor, cls).generate_objects(n)
        
GRAPH = {"Rock": Scissor, "Paper": Rock, "Scissor": Paper, "Mover": Mover}