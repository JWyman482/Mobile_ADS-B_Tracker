import pygame
from settings import setting

class AircraftSprite(pygame.sprite.Sprite):
    """Visual representation of the aircraft"""

    def __init__(self, aircraft_obj):
        super(AircraftSprite, self).__init__()
        self.aircraft = aircraft_obj
        self.create_point_surface()
        self.create_text_surface()

    def create_point_surface(self):
        """Creates a point"""
        point_colour = (228, 242, 70)
        container_height = 8
        container_width = 8
        radius = 2
        self.point_surface = pygame.Surface((container_height, container_width))
        pygame.draw.circle(self.point_surface, point_colour, (container_height//2, container_width//2), radius)

    def create_text_surface(self):
        """Populates text for sprite"""
        font = pygame.font.SysFont('helvetica', setting["ACFT_FONT"])
        anti_aliasing = True
        first_line = self.aircraft.name
        second_line = self.aircraft.get_pretty_altitude().zfill(3) + ' ' + str(self.aircraft.type)
        third_line = str(int(self.aircraft.dist)) + 'NM'
        self.text_surface = font.render(first_line, anti_aliasing, (255, 255, 255))
        self.text_surface2 = font.render(second_line, anti_aliasing, (255, 255, 255))
        self.text_surface3 = font.render(third_line, anti_aliasing, (255, 255, 255))
