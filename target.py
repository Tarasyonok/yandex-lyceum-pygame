import pygame

n = int(input())
k = int(input())
width = k * n * 2
size = (width, width)
screen = pygame.display.set_mode(size)
pygame.init()


def draw(screen):
    screen.fill((0, 0, 0))
    c1 = 255
    c2 = 0
    c3 = 0
    for i in range(k):
        c1 = 255 * (i % 3 == 0)
        c2 = 255 * (i % 3 == 1)
        c3 = 255 * (i % 3 == 2)
        pygame.draw.circle(screen, pygame.Color(c1, c2, c3), (width // 2, width // 2), n * (k - i))


draw(screen)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
