import pygame

class Dot(pygame.sprite.Sprite):
    def __init__(self, posx: int=0, posy: int=255, size: int=20, color_outer: tuple[int, int, int]=(0, 255, 250), color_inner: tuple[int, int, int]=(0, 0, 250)) -> None:
        super().__init__()

        self.posx = posx
        self.posy = posy
        self.size = size
        self.color_outer = color_outer
        self.color_inner = color_inner
        self.cur_posy = 0

        self.image = pygame.surface.Surface((self.size * 2 + 5, self.size * 2 + 5), pygame.SRCALPHA)
        self.rect = self.image.get_rect(centerx=posx, centery=posy)

        self.offset = self.rect.centery - 255
        self.miny = self.offset
        self.maxy = self.rect.centery

        assert self.posy >= 255, f"The Center of the Object must be >= 255. posy = {self.posy}"

    def update(self, posy: int) -> None:
        self.rect.centery = posy

        if self.rect.centery < self.miny:
            self.rect.centery = self.miny
        elif self.rect.centery > self.maxy:
            self.rect.centery = self.maxy

        self.cur_posy = 255 - self.rect.centery + self.offset
        print(self.cur_posy)


    def set_center(self, posxy: tuple[int, int]) -> None:
        self.rect.center = posxy
        self.offset = self.rect.centery - 255
        self.miny = self.offset
        self.maxy = self.rect.centery


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
    

    def get_right_pos(self) -> int:
        return self.rect.right
    

    def get_top(self) -> tuple[int, int]:
        return (self.rect.midtop[0], self.rect.midtop[1] + self.offsety)
        

    def get_bottom(self) -> tuple[int, int]:
        return (self.rect.midtop[0], self.rect.midtop[1] + self.height + self.offsety)
    
    
    def set_topleft_position(self, posx: int, posy: int) -> None:
        self.rect.left = posx
        self.rect.top = posy


    def draw(self, root_surf: pygame.Surface) -> None:
        self.image.fill((0, 0, 0, 0))
        pygame.draw.rect(self.image, self.color_slider, self.slider_rect, border_radius=10)
        pygame.draw.rect(self.image, (0, 0, 0, 0), (self.offsetx + self.offset_inner, self.offsety + self.offset_inner, self.offsetx * 2 - 2 * self.offset_inner, self.height - self.offset_inner * 2), border_radius=10)

        root_surf.blit(self.image, self.rect)


class Panel(pygame.sprite.Sprite):
    def __init__(self, posx: int=0, posy: int=0, sizex: int=100, sizey: int=100, color: tuple[int, int, int]=(50, 200, 50)):
        super().__init__()

        self.posx = posx
        self.posy = posy
        self.sizex = sizex
        self.sizey = sizey
        self.color = color

        self.image = pygame.surface.Surface((self.sizex, self.sizey), pygame.SRCALPHA)
        self.rect = self.image.get_rect(left=posx, top=self.posy)


    def get_left_pos(self) -> int:
        return self.rect.left


    def set_right_pos(self, pos_right: int) -> None:
        self.rect.right = pos_right


    def draw(self, root_surf: pygame.Surface) -> None:
        self.image.fill((0, 0, 0, 0))
        pygame.draw.rect(self.image, self.color, (0, 0, self.rect.width, self.rect.height), border_radius=10)
        root_surf.blit(self.image, self.rect)
