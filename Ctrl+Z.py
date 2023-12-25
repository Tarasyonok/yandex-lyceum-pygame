import pygame

pygame.init()

FRAMES_PER_SECOND = 50
clock = pygame.time.Clock()

size = width, height = 500, 400
screen = pygame.display.set_mode(size)

rects = []

running = True
isClicked = False

ctrl = False

rx1 = ry1 = rx2 = ry2 = None

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                isClicked = True
                sx, sy = event.pos
                # rects.append([sx, y, *event.pos])
        elif event.type == pygame.MOUSEMOTION:
            if isClicked:
                rx1, ry1, rx2, ry2 = sx, sy, *event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                isClicked = False
                rx1 = ry1 = rx2 = ry2 = None
                rects.append([sx, sy, *event.pos])
        elif event.type == pygame.KEYDOWN:
            if ctrl and event.key == pygame.K_z and len(rects) > 0:
                rects.pop()
            elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                ctrl = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                ctrl = False

    screen.fill((0, 0, 0))

    if rx1 and ry1 and rx2 and ry2:
        pygame.draw.polygon(screen, pygame.Color(255, 255, 255),
                            [(rx1, ry1), (rx2, ry1), (rx2, ry2), (rx1, ry2)], 4)

    for r in rects:
        x1, y1, x2, y2 = r
        pygame.draw.polygon(screen, pygame.Color(255, 255, 255),
                            [(x1, y1), (x2, y1), (x2, y2), (x1, y2)], 4)

    clock.tick(50)

    pygame.display.flip()

pygame.quit()
