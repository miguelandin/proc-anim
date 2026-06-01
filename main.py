import pygame
from chain import Chain
from math import pi

init_pos = pygame.Vector2(640, 360)
reach_pos: pygame.Vector2 = init_pos.copy()
chain = Chain(init_pos, 3, 50, 2*pi/3)
hold: bool = True

pygame.init()
screen = pygame.display.set_mode((1280, 720))
surface = pygame.Surface(screen.get_size())
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            hold = not hold

    if hold:
        reach_pos = pygame.Vector2(pygame.mouse.get_pos())
        chain.fabrik_resolve(reach_pos)
        print(chain.get_coords())

    surface.fill("black")
    chain.display_lines(surface)
    screen.blit(surface)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
