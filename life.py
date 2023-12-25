import pygame


class Board:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.board = [[0] * w for i in range(h)]
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
        if 0 <= x < self.w and 0 <= y < self.h:
            return x, y

        return None

    def on_click(self, cell):
        x, y = cell
        self.board[y][x] = not self.board[y][x]

    def process_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


class Life(Board):

    def render(self, screen):
        for y in range(self.h):
            for x in range(self.w):
                if self.board[y][x] == 0:
                    pygame.draw.rect(screen, pygame.Color((190, 190, 190)),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size, self.cell_size), 1)
                elif self.board[y][x] == 1:
                    pygame.draw.rect(screen, pygame.Color((0, 190, 0)),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size, self.cell_size))

    def next_move(self):
        new_board = []
        for row in self.board:
            new_board.append(row[:])
        for i in range(self.h):
            for j in range(self.w):
                cells_around = 0
                if i > 0 and j > 0 and self.board[i - 1][j - 1] == 1:
                    cells_around += 1
                if i > 0 and self.board[i - 1][j] == 1:
                    cells_around += 1
                if i > 0 and j < self.w - 1 and self.board[i - 1][j + 1] == 1:
                    cells_around += 1

                if j > 0 and self.board[i][j - 1] == 1:
                    cells_around += 1
                if j < self.w - 1 and self.board[i][j + 1] == 1:
                    cells_around += 1

                if i < self.h - 1 and j > 0 and self.board[i + 1][j - 1] == 1:
                    cells_around += 1
                if i < self.h - 1 and self.board[i + 1][j] == 1:
                    cells_around += 1
                if i < self.h - 1 and j < self.w - 1 and self.board[i + 1][j + 1] == 1:
                    cells_around += 1
                if self.board[i][j] == 1 and cells_around != 2 and cells_around != 3:
                    new_board[i][j] = 0
                elif self.board[i][j] == 0 and cells_around == 3:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = self.board[i][j]

        self.board = []
        for row in new_board:
            self.board.append(row[:])


pygame.init()
size = 620, 620
screen = pygame.display.set_mode(size)
gameFPS = 10
FPS = 60
clock = pygame.time.Clock()

board = Life(30, 30)
board.set_view(10, 10, 20)
board.next_move()
run = True
stop = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and stop:
                board.process_click(event.pos)
            elif event.button == 3:
                stop = not stop
                if stop:
                    FPS = 60
                else:
                    FPS = gameFPS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stop = not stop
                if stop:
                    FPS = 60
                else:
                    FPS = gameFPS
        if event.type == pygame.MOUSEWHEEL:
            if event.precise_y > 0:
                gameFPS += 1
                gameFPS = min(100, gameFPS)
            else:
                gameFPS -= 1
                gameFPS = max(1, gameFPS)
            if stop:
                FPS = 60
            else:
                FPS = gameFPS

    screen.fill((0, 0, 0))
    if not stop:
        board.next_move()
    board.render(screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
