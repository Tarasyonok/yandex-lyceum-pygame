import pygame

width = 300
height = 200
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.init()


def draw(screen):
    screen.fill('white')
    for i in range(width // 30 + 1):
        for j in range(height // 15 + 1):
            x = i * 32
            x -= 16 * (j % 2 == 1)
            y = j * 17
            pygame.draw.rect(screen, 'red', (x, y, 30, 15))


draw(screen)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
