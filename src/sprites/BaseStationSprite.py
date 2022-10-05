import pygame
import helpers
import settings as stg

class BaseStationSprite(pygame.sprite.Sprite):
    """Visual representation of a base station"""

    def __init__(self, rgb, rwy, text='Home'):
        super(BaseStationSprite, self).__init__()
        self.rgb = rgb
        self.text = text
        self.rrdist = "Rings: " + str(stg.RR_DIST) + " NM"
        self.range = "Range: " + str(stg.RANGE_NM) + " NM"
        self.screen_h, self.screen_w = helpers.get_screen_dimensions()
        self.coords = str(stg.LAT) + " " + str(stg.LON) + ", " + str(self.screen_h) + "x" + str(self.screen_w)
        self.filter = "Filter: " + str(stg.ALT_FILTER)
        self.rwy = rwy 
        self.create_line_surface()
        self.create_text_surface()

    def create_line_surface(self):
        container_height = 20
        container_width = 3
        line_width = 20
        line_height = 20
        self.surface = pygame.Surface((container_width, container_height), pygame.SRCALPHA)
        pygame.draw.line(self.surface, self.rgb, (0, 0), (0, line_height), 2)
        self.line_surface = pygame.transform.rotate(self.surface, self.rwy)

    def create_text_surface(self):
        """Populates text for sprite"""
        font = pygame.font.SysFont('consolas', stg.BASE_FONT)
        anti_aliasing = True
        self.text_surface = font.render(self.text, anti_aliasing, (255, 255, 255))
        if self.text == "Home":
            self.rr_text_surface = font.render(self.rrdist, anti_aliasing, (255, 255, 255))
            self.range_text_surface = font.render(self.range, anti_aliasing, (255, 255, 255))
            self.ll_text_surface = font.render(self.coords, anti_aliasing, (255, 255, 255))
            self.filt_text_surface = font.render(self.filter, anti_aliasing, (255, 255, 255))

