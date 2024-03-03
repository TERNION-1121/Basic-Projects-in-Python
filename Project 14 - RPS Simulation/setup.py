from math import cos, sin, pi
from random import random, uniform

import pygame 
from pygame import Vector2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_SIZE = (500, 500)
SCREEN_MID = Vector2(0, 0)

class Mover():
    COLOR = WHITE
    objects = list()

    def __init__(self, pos = None) -> None:
        if not pos:
            self.position = Mover.rand_pos(SCREEN_SIZE)
        else:
            self.position = Vector2(pos)

        self.velocity = Mover.random_vector() * 25

    def update(self, dt: int) -> None:
        self.acceleration = Mover.random_vector()

        enemy_position = Vector2(GRAPH[self.__class__.__name__].get_nearest_vector(self.position))
        self.acceleration += (enemy_position - self.position)

        self.acceleration.scale_to_length(5)

        self.position += self.velocity * dt
        self.limit_velocity()
        self.check_screen_bounds(SCREEN_SIZE)
        self.velocity += self.acceleration * dt

    def limit_velocity(self) -> None:
        if self.velocity.magnitude() > 50:
            self.velocity.scale_to_length(50)

    def check_screen_bounds(self, screen_dim: tuple):
        width, height = screen_dim

        if self.position.x <= 0 or self.position.x > width:
            self.velocity.x *= -1
        if self.position.y <= 0 or self.position.y > height:
            self.velocity.y *= -1

    def show(self, screen) -> None:
        pygame.draw.circle(screen, self.COLOR, self.position, 5)

    @staticmethod
    def random_vector() -> Vector2:
        angle = uniform(0, 2 * pi)
        return Vector2(cos(angle), sin(angle))

    @staticmethod
    def rand_pos(screen_dim: tuple[int, int]) -> Vector2:
        return Vector2(random() * (screen_dim[0] - 10), random() * (screen_dim[1] - 10))

    @classmethod
    def show_all(cls, screen) -> None:
        for obj in cls.objects:
            obj.show(screen)

    @classmethod
    def update_all(cls, dt: int) -> None:
        for obj in cls.objects:
            obj.update(dt)

    @classmethod
    def generate_objects(cls, n: int) -> None:
        for _ in range(n):
            cls()

    @classmethod
    def get_nearest_vector(cls, v: Vector2) -> Vector2:
        min_distance = Vector2(SCREEN_SIZE).length()
        to_return = v
        for obj in cls.objects:
            if (current_distance := v.distance_to(obj.position)) < min_distance:
                min_distance = current_distance 
                to_return = obj.position
        return to_return
    
    @classmethod
    def get_centroid(cls) -> Vector2:
        return Vector2(sum([obj.position for obj in cls.objects], start= Vector2()) / len(cls.objects))
    
    @classmethod
    def draw_centroid(cls, screen) -> None:
        pygame.draw.circle(screen, cls.COLOR, cls.get_centroid(), 10)

class Rock(Mover):
    COLOR = RED
    objects = list()
    
    def __init__(self, pos = None) -> None:
        super().__init__(pos)
        Rock.objects.append(self)

    @classmethod
    def show_all(cls, screen) -> None:
        super(Rock, cls).show_all(screen)

    @classmethod
    def generate_objects(cls, n: int) -> None:
        super(Rock, cls).generate_objects(n)

    @classmethod
    def get_centroid(cls) -> Vector2:
        return super(Rock, cls).get_centroid()
    
    @classmethod
    def draw_centroid(cls, screen) -> None:
        super(Rock, cls).draw_centroid(screen)

class Paper(Mover):
    COLOR = GREEN
    objects = list()

    def __init__(self, pos = None) -> None:
        super().__init__(pos)
        Paper.objects.append(self)
    
    @classmethod
    def show_all(cls, screen) -> None:
        super(Paper, cls).show_all(screen)

    @classmethod
    def generate_objects(cls, n: int) -> None:
        super(Paper, cls).generate_objects(n)

    @classmethod
    def get_centroid(cls) -> Vector2:
        return super(Paper, cls).get_centroid()
    
    @classmethod
    def draw_centroid(cls, screen) -> None:
        super(Paper, cls).draw_centroid(screen)

class Scissor(Mover):
    COLOR = BLUE
    objects = list()

    def __init__(self, pos = None) -> None:
        super().__init__(pos)
        Scissor.objects.append(self)

    @classmethod
    def show_all(cls, screen) -> None:
        super(Scissor, cls).show_all(screen)

    @classmethod
    def generate_objects(cls, n: int) -> None:
        super(Scissor, cls).generate_objects(n)

    @classmethod
    def get_centroid(cls) -> Vector2:
        return super(Scissor, cls).get_centroid()
    
    @classmethod
    def draw_centroid(cls, screen) -> None:
        super(Scissor, cls).draw_centroid(screen)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, path: str, position) -> None:
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(f"{path}.png").convert_alpha(), (20, 20))
        self.position = position
        self.rect = self.image.get_rect(center=self.position)
    
    def update(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
        

GRAPH = {"Rock": Scissor, "Paper": Rock, "Scissor": Paper, "Mover": Mover}