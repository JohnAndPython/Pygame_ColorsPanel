import pygame

class Dot(pygame.sprite.Sprite):
    def __init__(self, posx: int=0, posy: int=0, size: int=20, color_outer: tuple[int, int, int]=(0, 255, 250), color_inner: tuple[int, int, int]=(0, 0, 250), offset: int=0) -> None:
        super().__init__()

        self.posx = posx
        self.posy = posy
        self.size = size
        self.color_outer = color_outer
        self.color_inner = color_inner
        self.offset = offset
        self.cur_posy = 0

        self.image = pygame.surface.Surface((self.size * 2 + 5, self.size * 2 + 5), pygame.SRCALPHA)
        #self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect(centerx=posx, centery=posy)

    def update(self, posy: int, miny: int=0, maxy: int=255) -> None:
        self.rect.centery = posy

        if self.rect.centery < miny:
            self.rect.centery = miny
        elif self.rect.centery > maxy:
            self.rect.centery = maxy

        self.cur_posy = 255 - (self.rect.centery - self.offset)
        #print(self.cur_posy)


    def get_positiony(self) -> int:
        return self.cur_posy
    

    def get_dot_rect(self) -> pygame.Rect:
        return self.rect


    def draw(self, root_surf: pygame.Surface) -> None:
        #self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, self.color_outer, (self.size + 5 // 2, self.size + 5 // 2), self.size)
        pygame.draw.circle(self.image, (0, 0, 0), (self.size + 5 // 2, self.size + 5 // 2), self.size, width=1)
        pygame.draw.circle(self.image, self.color_inner, (self.size + 5 // 2, self.size + 5 // 2), self.size - 5)
        pygame.draw.circle(self.image, (0, 0, 0), (self.size + 5 // 2, self.size + 5 // 2), self.size - 5, width=1)

        root_surf.blit(self.image, self.rect)


class Slider(pygame.sprite.Sprite):
    def __init__(self, posx: int=0, posy: int=0, color_panel: tuple[int, int, int]=(200, 200, 200), color_dot_outer: tuple[int, int, int]=(0, 255, 250), color_dot_inner: tuple[int, int, int]=(0, 0, 250)):
        super().__init__()

        self.posx = posx
        self.posy = posy
        self.color_panel = color_panel
        self.color_dot_outer = color_dot_outer
        self.color_dot_inner = color_dot_inner

        self.offsetx = 10
        self.offsety = 20
        self.width = 20 
        self.height = 255
        self.dot = Dot(self.width // 2 + self.offsetx, self.height + self.offsety, size=15, color_outer=self.color_dot_outer, color_inner=self.color_dot_inner, offset=self.offsety)

        self.image = pygame.surface.Surface((self.width + self.offsetx * 2, 300), pygame.SRCALPHA)
        self.rect = self.image.get_rect(left=self.posx, top=self.posy)
        
    def get_width(self) -> int:
        return self.rect.width
    

    def get_height(self) -> int:
        return self.rect.height
    

    def set_position(self, posx: int, posy: int) -> None:
        self.rect.left = posx
        self.rect.top = posy


    def get_dot_positiony(self) -> int:
        return self.dot.get_positiony()
    

    def get_dot_rect(self) -> pygame.Rect:
        return self.dot.get_dot_rect()


    def update(self, posy: int=256) -> None:
        self.dot.update(posy, miny=self.offsety, maxy=self.height + self.offsety)


    def draw(self, root_surf: pygame.Surface) -> None:
        self.image.fill((0, 0, 0, 0))
        pygame.draw.rect(self.image, self.color_panel, (self.offsetx, self.offsety, self.width, self.height), border_radius=10)
        pygame.draw.rect(self.image, (0, 0, 0, 0), (self.offsetx + 4, self.offsety + 4, 12, self.height - 8), border_radius=10)
        self.dot.draw(self.image)

        root_surf.blit(self.image, self.rect)


class Panel(pygame.sprite.Sprite):
    def __init__(self, posx: int=0, posy: int=0, color: tuple[int, int, int]=(50, 200, 50)):
        super().__init__()

        self.posx = posx
        self.posy = posy
        self.color = color

        # slider initial position
        sliderposx = 20
        sliderposy = 0
        offset = 5

        self.slider_red = Slider(color_dot_outer=(250, 150, 0), color_dot_inner=(250, 0, 0))
        self.slider_green = Slider(color_dot_outer=(150, 250, 0), color_dot_inner=(0, 250, 0))
        self.slider_blue = Slider()
        
        self.slider_red.set_position(sliderposx, sliderposy)
        self.slider_width = self.slider_red.get_width()
        self.slider_green.set_position(sliderposx + self.slider_width + offset, sliderposy)
        self.slider_blue.set_position(sliderposx + self.slider_width * 2 + offset * 2, sliderposy)

        self.slider_lst = (self.slider_red, self.slider_green, self.slider_blue)

        surf_width = sliderposx * 2 + self.slider_width * 3 + offset * 2
        surf_height = self.slider_red.get_height()

        self.image = pygame.surface.Surface((surf_width, surf_height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(left=posx, top=self.posy)

    def update(self, posy: int) -> None:
        self.slider_red.update(posy)


    def get_sliders(self) -> tuple[Slider, Slider, Slider]:
        return self.slider_lst

    def get_dot_value(self, slider: Slider) -> int:
        return slider.get_dot_positiony()
    

    def get_dot_rect(self, slider: Slider) -> pygame.Rect:
        return slider.get_dot_rect()


    def draw(self, root_surf: pygame.Surface) -> None:
        self.image.fill((0, 0, 0, 0))

        pygame.draw.rect(self.image, self.color, (0, 0, self.rect.width, self.rect.height), border_radius=10)
        self.slider_red.draw(self.image)
        self.slider_green.draw(self.image)
        self.slider_blue.draw(self.image)


        root_surf.blit(self.image, self.rect)
