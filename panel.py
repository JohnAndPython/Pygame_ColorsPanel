import pygame

class Dot(pygame.sprite.Sprite):
    def __init__(self, posx: int=0, posy: int=255, size: int=20, color_outer: tuple[int, int, int]=(0, 255, 250), color_inner: tuple[int, int, int]=(0, 0, 250)) -> None:
        super().__init__()

        self.__posx = posx
        self.__posy = posy
        self.__size = size
        self.__color_outer = color_outer
        self.__color_inner = color_inner
        self.value = 0

        self.__image = pygame.surface.Surface((self.__size * 2 + 5, self.__size * 2 + 5), pygame.SRCALPHA)
        self.rect = self.__image.get_rect(centerx=self.__posx, centery=self.__posy)

        self.__offset = self.rect.centery - 255
        self.__miny = self.__offset
        self.__maxy = self.rect.centery

        assert self.__posy >= 255, f"The Center of the Object must be >= 255. posy = {self.__posy}"

    def update(self, posy: int) -> None:
        self.rect.centery = posy

        if self.rect.centery < self.__miny:
            self.rect.centery = self.__miny
        elif self.rect.centery > self.__maxy:
            self.rect.centery = self.__maxy

        self.value = 255 - self.rect.centery + self.__offset


    def set_center(self, posxy: tuple[int, int]) -> None:
        self.rect.center = posxy
        self.__offset = self.rect.centery - 255
        self.__miny = self.__offset
        self.__maxy = self.rect.centery


    def draw(self, root_surf: pygame.Surface) -> None:
        self.__image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.__image, self.__color_outer, (self.__size + 5 // 2, self.__size + 5 // 2), self.__size)
        pygame.draw.circle(self.__image, (0, 0, 0), (self.__size + 5 // 2, self.__size + 5 // 2), self.__size, width=1)
        pygame.draw.circle(self.__image, self.__color_inner, (self.__size + 5 // 2, self.__size + 5 // 2), self.__size - 5)
        pygame.draw.circle(self.__image, (0, 0, 0), (self.__size + 5 // 2, self.__size + 5 // 2), self.__size - 5, width=1)

        root_surf.blit(self.__image, self.rect)


class Slider(pygame.sprite.Sprite):
    def __init__(self, posx: int=0, posy: int=0, width:int=20, height: int=255, color_slider: tuple[int, int, int]=(200, 200, 200)):
        super().__init__()

        self.__posx = posx
        self.__posy = posy
        self.__color_slider = color_slider
        self.__width = width 
        self.__height = height

        self.__offsetx = 10
        self.__offsety = 20
        self.__offset_inner = 4

        self.__image = pygame.surface.Surface((self.__width + self.__offsetx * 2, self.__height + 45), pygame.SRCALPHA)
        self.rect = self.__image.get_rect(left=self.__posx, top=self.__posy)
        self.__slider_rect = pygame.rect.Rect(self.__offsetx, self.__offsety, self.__width, self.__height)


    def get_width(self) -> int:
        return self.rect.width
    

    def get_right_pos(self) -> int:
        return self.rect.right
    

    def get_top(self) -> tuple[int, int]:
        return (self.rect.midtop[0], self.rect.midtop[1] + self.__offsety)
        

    def get_bottom(self) -> tuple[int, int]:
        return (self.rect.midtop[0], self.rect.midtop[1] + self.__height + self.__offsety)
    
    
    def set_topleft_position(self, posx: int, posy: int) -> None:
        self.rect.left = posx
        self.rect.top = posy


    def draw(self, root_surf: pygame.Surface) -> None:
        self.__image.fill((0, 0, 0, 0))
        pygame.draw.rect(self.__image, self.__color_slider, self.__slider_rect, border_radius=10)
        pygame.draw.rect(self.__image, (0, 0, 0, 0), (self.__offsetx + self.__offset_inner, self.__offsety + self.__offset_inner, self.__offsetx * 2 - 2 * self.__offset_inner, self.__height - self.__offset_inner * 2), border_radius=10)

        root_surf.blit(self.__image, self.rect)


class Panel(pygame.sprite.Sprite):
    def __init__(self, posx: int=0, posy: int=0, sizex: int=100, sizey: int=100, color: tuple[int, int, int]=(50, 200, 50)):
        super().__init__()

        self.__posx = posx
        self.__posy = posy
        self.__sizex = sizex
        self.__sizey = sizey
        self.__color = color

        self.__image = pygame.surface.Surface((self.__sizex, self.__sizey), pygame.SRCALPHA)
        self.rect = self.__image.get_rect(left=posx, top=self.__posy)


    def get_left_pos(self) -> int:
        return self.rect.left


    def set_right_pos(self, pos_right: int) -> None:
        self.rect.right = pos_right


    def draw(self, root_surf: pygame.Surface) -> None:
        self.__image.fill((0, 0, 0, 0))
        pygame.draw.rect(self.__image, self.__color, (0, 0, self.rect.width, self.rect.height), border_radius=10)
        root_surf.blit(self.__image, self.rect)
