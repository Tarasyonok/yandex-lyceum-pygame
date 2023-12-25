from random import choice

import pygame

pygame.init()


class Board:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.board = [[-1] * w for i in range(h)]
        self.left = 10
        self.right = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos):
        x_pos, y_pos = mouse_pos
        x = (x_pos - self.left) // self.cell_size
        y = (y_pos - self.left) // self.cell_size
        if 0 <= x < self.w - 1 and 0 <= y <= self.h - 1:
            return x, y

        return None

    def process_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


class Minesweeper(Board):
    def __init__(self, w, h, mines):
        super().__init__(w, h)

        poses = []
        for i in range(h):
            for j in range(w):
                poses.append((i, j))

        for _ in range(mines):
            pos = choice(poses)
            self.board[pos[0]][pos[1]] = 10
            poses.remove(pos)

    def render(self, screen):
        for y in range(self.h):
            for x in range(self.w):
                if self.board[y][x] == 10:
                    pygame.draw.rect(screen, pygame.Color((255, 0, 0)),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size, self.cell_size))
                elif 0 <= self.board[y][x] <= 9:
                    f = pygame.font.Font(None, 35)
                    sc_text = f.render(str(self.board[y][x]), 1, pygame.Color(0, 255, 0))
                    x_coord = x * self.cell_size + self.cell_size / 2 + self.left
                    y_coord = y * self.cell_size + self.cell_size / 2 + self.top
                    pos = sc_text.get_rect(center=(x_coord, y_coord))
                    screen.blit(sc_text, pos)

                pygame.draw.rect(screen, pygame.Color((190, 190, 190)),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)

    def on_click(self, cell):
        x, y = cell
        if self.board[y][x] == 10:
            return
        around = 0
        if y > 0 and x > 0 and self.board[y - 1][x - 1] == 10:
            around += 1
        if y > 0 and self.board[y - 1][x] == 10:
            around += 1
        if y > 0 and x < self.w - 1 and self.board[y - 1][x + 1] == 10:
            around += 1
        if x > 0 and self.board[y][x - 1] == 10:
            around += 1
        if x < self.w - 1 and self.board[y][x + 1] == 10:
            around += 1
        if y < self.h - 1 and x > 0 and self.board[y + 1][x - 1] == 10:
            around += 1
        if y < self.h - 1 and self.board[y + 1][x] == 10:
            around += 1
        if y < self.h - 1 and x < self.w - 1 and self.board[y + 1][x + 1] == 10:
            around += 1

        self.board[y][x] = around

    def open_cell(self):
        pass


size = 440, 640
screen = pygame.display.set_mode(size)
FPS = 60
clock = pygame.time.Clock()

board = Minesweeper(10, 15, 10)
board.set_view(20, 20, 40)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.process_click(event.pos)

    screen.fill((0, 0, 0))
    board.render(screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
