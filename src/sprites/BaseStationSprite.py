import pygame
import helpers
from settings import setting, airports

class BaseStationSprite(pygame.sprite.Sprite):
    """Visual representation of a base station"""

    def __init__(self, rgb, text='Home'):
        super(BaseStationSprite, self).__init__()
        self.rgb = rgb
        self.text = text
        self.rrdist = "Range Rings: " + str(setting["RR_DIST"]) + "NM, Range: " + str(setting["RANGE_NM"]) + "NM"
        self.screen_h, self.screen_w = helpers.get_screen_dimensions()
        self.coords = str(setting["LAT"]) + " " + str(setting["LON"]) + ", " + str(self.screen_h) + "x" + str(self.screen_w)
        self.filter = str("Filter: " + setting['Filter'])
        self.create_point_surface()
        self.create_text_surface()

    def create_point_surface(self):
        """Creates a point"""
        container_height = 6
        container_width = 6
        # line_width = 20
        # line_height = 20
        radius = 3
        self.point_surface = pygame.Surface((container_height, container_width))
        # self.line_surface = pygame.Surface((line_height, line_width))
        pygame.draw.circle(self.point_surface, self.rgb, (container_height//2, container_width//2), radius)
        # pygame.draw.aaline(self.line_surface, self.rgb, (0, 0), (line_width, 0), 3)
        # pygame.transform.rotate(self.line_surface, 90)

    def create_text_surface(self):
        """Populates text for sprite"""
        font = pygame.font.SysFont('helvetica', setting["BASE_FONT"])
        anti_aliasing = True
        self.text_surface = font.render(self.text, anti_aliasing, (255, 255, 255))
        if self.text == "Home":
            self.rr_text_surface = font.render(self.rrdist, anti_aliasing, (255, 255, 255))
            self.ll_text_surface = font.render(self.coords, anti_aliasing, (255, 255, 255))
            self.filt_text_surface = font.render(self.filter, anti_aliasing, (255, 255, 255))
