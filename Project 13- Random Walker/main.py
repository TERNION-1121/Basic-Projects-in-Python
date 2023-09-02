from setup import *

window = pygame.display.set_mode((SCREEN_DIM, SCREEN_DIM))
window.fill(BLUE)
pygame.display.flip()

pygame.display.set_caption("Random Walker")

random_walker = Walker()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    random_walker.show(window)
    random_walker.update_position()

    pygame.display.flip()

pygame.quit()