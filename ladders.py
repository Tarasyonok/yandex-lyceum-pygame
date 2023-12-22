import os
import pygame
from itertools import chain

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = pygame.Surface((20, 20))
        self.image.fill('blue')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        for p in chain(H_platforms, V_platforms):
            if pygame.sprite.collide_mask(self, p):
                break
        else:
            self.rect = self.rect.move(0, 1)


class H_Platform(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = pygame.Surface((50, 10))
        self.image.fill('gray')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class V_Platform(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = pygame.Surface((10, 50))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]


all_sprites = pygame.sprite.Group()

player = Player((1000, 1000))
H_platforms = []
V_platforms = []

clock = pygame.time.Clock()
ctrl = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if ctrl:
                    V_platforms.append(V_Platform(event.pos))
                else:
                    H_platforms.append(H_Platform(event.pos))
            elif event.button == 3:
                player.rect.x, player.rect.y = event.pos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect = player.rect.move(-10, 0)
            if event.key == pygame.K_RIGHT:
                player.rect = player.rect.move(10, 0)
            if event.key == pygame.K_UP:
                for p in V_platforms:
                    if pygame.sprite.collide_mask(player, p):
                        player.rect = player.rect.move(0, -10)
                        break
            if event.key == pygame.K_DOWN:
                for p in V_platforms:
                    if pygame.sprite.collide_mask(player, p):
                        player.rect = player.rect.move(0, 10)
                        break
            if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                ctrl = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                ctrl = False
    screen.fill(pygame.Color("black"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
