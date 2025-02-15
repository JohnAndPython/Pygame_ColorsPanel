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

# variables
surf_red = dot_r.value
surf_green = dot_g.value
surf_blue = dot_b.value

can_move_r = False
can_move_g = False
can_move_b = False

prev_time = time.time()

while True:
    # delta time |alternative: dt = clock.tick(60) / 1000
    dt = time.time() - prev_time
    prev_time = time.time()
    
    mouse_pos = pygame.mouse.get_pos()

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if dot_r.rect.collidepoint(mouse_pos):
                    can_move_r = True
                elif dot_g.rect.collidepoint(mouse_pos):
                    can_move_g = True
                elif dot_b.rect.collidepoint(mouse_pos):
                    can_move_b = True
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            can_move_r = False
            can_move_g = False
            can_move_b = False


    # update
    if can_move_r:
        dot_r.update(mouse_pos[1])
    elif can_move_g:
        dot_g.update(mouse_pos[1])
    elif can_move_b:
        dot_b.update(mouse_pos[1])

    surf_red = dot_r.value
    surf_green = dot_g.value
    surf_blue = dot_b.value
    
    # draw
    screen.fill((surf_red, surf_green, surf_blue))

    main_panel.draw(screen)
    slider_r.draw(screen)
    slider_g.draw(screen)
    slider_b.draw(screen)
    dot_r.draw(screen)
    dot_g.draw(screen)
    dot_b.draw(screen)

    # update display
    pygame.display.update()

    # set max FPS to 60
    clock.tick(60)
