import pygame
import time, sys

from panel import Dot, Slider

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

slider_r = Slider(100, 100)
dot_r = Dot(100, 100)

slider_r.get_top()
dot_r.set_center(slider_r.get_bottom())

surf_red = 255
surf_blue = 255
surf_green = 255

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

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if pygame.mouse.get_pressed()[0]:
        #         if main_panel.get_dot_rect(main_panel.get_sliders()[0]).collidepoint(mouse_pos):
        #             print("yes")
        #             main_panel.update(mouse_pos[1])


    
    # update
    #dot_red.update(mouse_pos[1])
    #slider_red.update(mouse_pos[1])
    #main_panel.update(mouse_pos[1])
    
    

    screen.fill((surf_red, surf_green, surf_blue))


    #draw
    slider_r.draw(screen)
    dot_r.draw(screen)


    #update display
    pygame.display.update()

    #set max FPS to 60
    clock.tick(60)
