import pygame

class Dot(pygame.sprite.Sprite):
    def __init__(self, posx: int=0, posy: int=0, size: int=20, color_outer: tuple[int, int, int]=(0, 255, 250), color_inner: tuple[int, int, int]=(0, 0, 250)) -> None:
        super().__init__()

        self.posx = posx
        self.posy = posy
        self.color_outer = color_outer
        self.color_inner = color_inner
        self.size = size

        self.image = pygame.surface.Surface((self.size * 2 + 5, self.size * 2 + 5), pygame.SRCALPHA)
        #self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect(centerx=posx, centery=posy)


    def update(self, posy: int, miny: int=0, maxy: int=250) -> None:
        self.rect.centery = posy


    def draw(self, root_surf: pygame.Surface) -> None:
        #self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, self.color_outer, (self.size + 5 // 2, self.size + 5 // 2), self.size)
        pygame.draw.circle(self.image, (0, 0, 0), (self.size + 5 // 2, self.size + 5 // 2), self.size, width=1)
        pygame.draw.circle(self.image, self.color_inner, (self.size + 5 // 2, self.size + 5 // 2), self.size - 5)
        pygame.draw.circle(self.image, (0, 0, 0), (self.size + 5 // 2, self.size + 5 // 2), self.size - 5, width=1)

        root_surf.blit(self.image, self.rect)


class slider(pygame.sprite.Sprite):
    def __init__(self, posx: int, posy: int):
        super().__init__()

        self.posx = posx
        self.posy = posy

        self.image = pygame.surface.Surface((30, 300), pygame.SRCALPHA)
        self.rect = self.image.get_rect(left=self.posx, top=self.posy)
        
        self.offset = 5
        self.width = 20
        self.height = 256
        self.dot = Dot(self.width // 2 + self.offset, self.height, size=15)

    def update(self) -> None:
        pass


    def draw(self, root_surf: pygame.Surface) -> None:
        
        slider_rect = pygame.draw.rect(self.image, (200, 200, 200), (self.offset, self.offset, self.width, self.height), border_radius=10)
        self.dot.draw(self.image)

        root_surf.blit(self.image, self.rect)