import pygame
import time, sys

from panel import Dot, Slider, Panel

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# panel
main_panel = Panel(sizex=130, sizey=400)
main_panel.set_right_pos(SCREEN_WIDTH)

# sliders
slider_r = Slider(main_panel.get_left_pos() + 5, 0)
slider_g = Slider(slider_r.get_right_pos() + 5, 0)
slider_b = Slider(slider_g.get_right_pos(), 0)

# dots
dot_r = Dot(color_outer=(250, 150, 0), color_inner=(250, 50, 0))
dot_g = Dot(color_outer=(150, 250, 0), color_inner=(50, 250, 0))
dot_b = Dot()

dot_r.set_center(slider_r.get_bottom())
dot_g.set_center(slider_g.get_bottom())
dot_b.set_center(slider_b.get_bottom())

print(dot_r.rect.center)

surf_red = 255
surf_blue = 255
surf_green = 255

#test
can_move = False
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

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if dot_r.rect.collidepoint(mouse_pos):
                    can_move = True
                    

        elif event.type == pygame.MOUSEBUTTONUP:
            can_move = False


    
    # update
    #dot_red.update(mouse_pos[1])
    #slider_red.update(mouse_pos[1])
    #main_panel.update(mouse_pos[1])
    
    if can_move:
        dot_r.update(mouse_pos[1])
    

    screen.fill((surf_red, surf_green, surf_blue))


    #draw
    main_panel.draw(screen)
    slider_r.draw(screen)
    slider_g.draw(screen)
    slider_b.draw(screen)
    dot_r.draw(screen)
    dot_g.draw(screen)
    dot_b.draw(screen)
    


    #update display
    pygame.display.update()

    #set max FPS to 60
    clock.tick(60)
