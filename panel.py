import pygame

class Dot(pygame.sprite.Sprite):
    def __init__(self, posx: int=0, posy: int=0, size: int=20, color_outer: tuple[int, int, int]=(0, 255, 250), color_inner: tuple[int, int, int]=(0, 0, 250)) -> None:
        super().__init__()

        self.posx = posx
        self.posy = posy
        self.size = size
        self.color_outer = color_outer
        self.color_inner = color_inner
        self.cur_posy = 0

        self.image = pygame.surface.Surface((self.size * 2 + 5, self.size * 2 + 5), pygame.SRCALPHA)
        self.rect = self.image.get_rect(centerx=posx, centery=posy)


    def update(self, posy: int, miny: int=0, maxy: int=255) -> None:
        self.rect.centery = posy

        if self.rect.centery < miny:
            self.rect.centery = miny
        elif self.rect.centery > maxy:
            self.rect.centery = maxy

        self.cur_posy = 255 - (self.rect.centery - self.offset)
        #print(self.cur_posy)


    def set_center(self, posxy: tuple[int, int]) -> None:
        self.rect.center = posxy


    def draw(self, root_surf: pygame.Surface) -> None:
        #self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, self.color_outer, (self.size + 5 // 2, self.size + 5 // 2), self.size)
        pygame.draw.circle(self.image, (0, 0, 0), (self.size + 5 // 2, self.size + 5 // 2), self.size, width=1)
        pygame.draw.circle(self.image, self.color_inner, (self.size + 5 // 2, self.size + 5 // 2), self.size - 5)
        pygame.draw.circle(self.image, (0, 0, 0), (self.size + 5 // 2, self.size + 5 // 2), self.size - 5, width=1)

        root_surf.blit(self.image, self.rect)


class Slider(pygame.sprite.Sprite):
    def __init__(self, posx: int=0, posy: int=0, width:int=20, height: int=255, color_slider: tuple[int, int, int]=(200, 200, 200)):
        super().__init__()

        self.posx = posx
        self.posy = posy
        self.color_slider = color_slider
        self.width = width 
        self.height = height

        self.offsetx = 10
        self.offsety = 20
        self.offset_inner = 4

        self.image = pygame.surface.Surface((self.width + self.offsetx * 2, self.height + 45), pygame.SRCALPHA)
        self.rect = self.image.get_rect(left=self.posx, top=self.posy)
        self.slider_rect = pygame.rect.Rect(self.offsetx, self.offsety, self.width, self.height)


    def get_width(self) -> int:
        return self.rect.width
    

    def get_top(self) -> tuple[int, int]:
        return (self.rect.midtop[0], self.rect.midtop[1] + self.offsety)
        

    def get_bottom(self) -> tuple[int, int]:
        print(self.slider_rect.midbottom[1] + self.offsety)
        return (self.rect.midtop[0], self.rect.midtop[1] + self.height + self.offsety)
    
    
    def set_topleft_position(self, posx: int, posy: int) -> None:
        self.rect.left = posx
        self.rect.top = posy


    def draw(self, root_surf: pygame.Surface) -> None:
        self.image.fill((0, 0, 0, 0))
        pygame.draw.rect(self.image, self.color_slider, self.slider_rect, border_radius=10)
        pygame.draw.rect(self.image, (0, 0, 0, 0), (self.offsetx + self.offset_inner, self.offsety + self.offset_inner, self.offsetx * 2 - 2 * self.offset_inner, self.height - self.offsetx * 2), border_radius=10)

        root_surf.blit(self.image, self.rect)


# class Panel(pygame.sprite.Sprite):
#     def __init__(self, posx: int=0, posy: int=0, color: tuple[int, int, int]=(50, 200, 50)):
#         super().__init__()

#         self.posx = posx
#         self.posy = posy
#         self.color = color

#         # slider initial position
#         sliderposx = 20
#         sliderposy = 0
#         offset = 5

#         self.slider_red = Slider(color_dot_outer=(250, 150, 0), color_dot_inner=(250, 0, 0))
#         self.slider_green = Slider(color_dot_outer=(150, 250, 0), color_dot_inner=(0, 250, 0))
#         self.slider_blue = Slider()
        
#         self.slider_red.set_position(sliderposx, sliderposy)
#         self.slider_width = self.slider_red.get_width()
#         self.slider_green.set_position(sliderposx + self.slider_width + offset, sliderposy)
#         self.slider_blue.set_position(sliderposx + self.slider_width * 2 + offset * 2, sliderposy)

#         self.slider_lst = (self.slider_red, self.slider_green, self.slider_blue)

#         surf_width = sliderposx * 2 + self.slider_width * 3 + offset * 2
#         surf_height = self.slider_red.get_height()

#         self.image = pygame.surface.Surface((surf_width, surf_height), pygame.SRCALPHA)
#         self.rect = self.image.get_rect(left=posx, top=self.posy)

#     def update(self, posy: int) -> None:
#         self.slider_red.update(posy)


#     def get_sliders(self) -> tuple[Slider, Slider, Slider]:
#         return self.slider_lst

#     def get_dot_value(self, slider: Slider) -> int:
#         return slider.get_dot_positiony()
    

#     def get_dot_rect(self, slider: Slider) -> pygame.Rect:
#         return slider.get_dot_rect()


#     def draw(self, root_surf: pygame.Surface) -> None:
#         self.image.fill((0, 0, 0, 0))

#         pygame.draw.rect(self.image, self.color, (0, 0, self.rect.width, self.rect.height), border_radius=10)
#         self.slider_red.draw(self.image)
#         self.slider_green.draw(self.image)
#         self.slider_blue.draw(self.image)


#         root_surf.blit(self.image, self.rect)
