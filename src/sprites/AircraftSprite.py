import pygame
import settings as stg

class AircraftSprite(pygame.sprite.Sprite):
    """Visual representation of the aircraft"""

    def __init__(self, aircraft_obj):
        super(AircraftSprite, self).__init__()
        self.aircraft = aircraft_obj
        # self.create_point_surface()
        self.create_text_surface()

    def create_point_surface(self):
        """Creates a point"""
        point_colour = (228, 242, 70)
        container_height = 8
        container_width = 3
        radius = 2

        surface = pygame.Surface((container_height, container_width), pygame.SRCALPHA) 
        # print(type(self.aircraft.track))

        if type(self.aircraft.track) != float:
            self.point_surface = surface
        else: 
            print("Rotating")
            self.point_surface = pygame.transform.rotate(surface, self.aircraft.track)
        # pygame.draw.circle(self.point_surface, point_colour, (container_height//2, container_width//2), radius)
        pygame.draw.line(self.point_surface, point_colour, (0, 0), (0, container_height), 3)

    def create_text_surface(self):
        """Populates text for sprite"""
        font = pygame.font.SysFont('helvetica', stg.ACFT_FONT)
        anti_aliasing = True
        first_line = self.aircraft.name
        second_line = self.aircraft.get_pretty_altitude().zfill(3) + ' ' + str(self.aircraft.type)
        third_line = str(int(self.aircraft.dist)) + 'NM'
        self.text_surface = font.render(first_line, anti_aliasing, (255, 255, 255))
        self.text_surface2 = font.render(second_line, anti_aliasing, (255, 255, 255))
        self.text_surface3 = font.render(third_line, anti_aliasing, (255, 255, 255))

    def blitRotateCenter(surf, image, topleft, angle):
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

        surf.blit(rotated_image, new_rect.topleft)
