import pygame
from punkt import punkt

def sirkel(display, radius = 1, punkter = 360, s_x = 0, s_y = 0):
    hopp = 360 / punkter

    for i in range(punkter):
        vinkel = hopp * i
        x, y = punkt(vinkel, radius)
        for_x, for_y = punkt(vinkel - hopp, radius)

        pygame.draw.line(display, (255, 255, 255), (x + s_x, y + s_y), (for_x + s_x, for_y + s_y))

if __name__ == "__main__":
    display = pygame.display.set_mode([500, 500])
    sirkel(display, radius = 250, s_y = 250, s_x = 250)
    stop = False

    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True
                pygame.quit()
                quit()

        pygame.display.update()