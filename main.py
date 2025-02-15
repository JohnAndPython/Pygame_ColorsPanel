import pygame
import time, sys

from panel import Dot, slider

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

dot_red = Dot()
slider_red = slider(100,10)

#test

#test end

prev_time = time.time()

while True:
    #delta time |alternative: dt = clock.tick(60) / 1000
    dt = time.time() - prev_time
    prev_time = time.time()
    
    mouse_pos = pygame.mouse.get_pos()

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update
    dot_red.update(mouse_pos[1])

    screen.fill((255, 255, 255))

    dot_red.draw(screen)
    slider_red.draw(screen)


    #update display
    pygame.display.update()

    #set max FPS to 60
    clock.tick(60)
