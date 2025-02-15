import pygame
import time, sys

from panel import Dot, Slider, Panel

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


main_panel = Panel(200, 20)


surf_red = main_panel.get_dot_value(main_panel.get_sliders()[0])
surf_green = surf_red = main_panel.get_dot_value(main_panel.get_sliders()[1])
surf_blue = surf_red = main_panel.get_dot_value(main_panel.get_sliders()[2])

print(surf_red, surf_green, surf_blue)

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

        



    # update
    #dot_red.update(mouse_pos[1])
    #slider_red.update(mouse_pos[1])
    main_panel.update(mouse_pos[1])

    surf_red = main_panel.get_dot_value(main_panel.get_sliders()[0])
    print(surf_red)

    # surf_red -= 1
    # if surf_red <= 0:
    #     surf_red = 255

    screen.fill((surf_red, surf_green, surf_blue))


    # surf_green = surf_red = main_panel.get_dot_value(main_panel.get_sliders()[1])
    # surf_blue = surf_red = main_panel.get_dot_value(main_panel.get_sliders()[2])
    
    

    #dot_red.draw(screen)
    #slider_red.draw(screen)
    main_panel.draw(screen)


    #update display
    pygame.display.update()

    #set max FPS to 60
    clock.tick(60)
