from rain import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BACKGROUND)
pygame.display.flip()

pygame.mixer.music.load("soft-rain-ambient-111154.mp3")
pygame.mixer.music.play()

rain_drops = [RainDrop() for _ in range(750)]

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)

    for drop in rain_drops:
        drop.fall()
        drop.show(screen)

    pygame.display.flip()

pygame.quit()