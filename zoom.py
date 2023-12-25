import pygame

pygame.init()

FRAMES_PER_SECOND = 50
clock = pygame.time.Clock()

size = width, height = 501, 501
screen = pygame.display.set_mode(size)

running = True

with open('points.txt', 'r', encoding='utf-8') as f:
    str_points = f.read().replace('\n', ' ')
    points = [list(map(float, p[1:-1].replace(',', '.').split(';'))) for p in str_points.split(', ')]

for p in points:
    p[1] = -p[1]

coeff = 10
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEWHEEL:
            coeff += event.precise_y
            if coeff < 1:
                coeff = 1

    screen.fill((0, 0, 0))

    points_for_draw = []
    for p in points:
        points_for_draw.append((p[0] * coeff + 250, p[1] * coeff + 250))
    pygame.draw.polygon(screen, pygame.Color(255, 255, 255), points_for_draw, 1)

    clock.tick(50)

    pygame.display.flip()

pygame.quit()
