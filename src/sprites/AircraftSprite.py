import pygame
import settings as stg

class AircraftSprite(pygame.sprite.Sprite):
    """Visual representation of the aircraft"""

    def __init__(self, aircraft_obj):
        super(AircraftSprite, self).__init__()
        self.aircraft = aircraft_obj
        self.color = (72, 245, 66)
        if self.aircraft.track:
            self.surface = self.create_line_surface()
        else:
            self.surface = self.create_point_surface()
        self.create_text_surface()
        self.rect = self.surface.get_rect(center=(aircraft_obj.x_coordinate, self.aircraft.y_coordinate))
        self.aircraftSprite = (self.surface, self.rect)

    def create_point_surface(self):
        """Creates a point"""
        point_colour = (228, 242, 70)
        container_height = 8
        container_width = 3
        radius = 2

        surface = pygame.Surface((container_height, container_width), pygame.SRCALPHA) 
        # print(type(self.aircraft.track))
        pygame.draw.circle(surface, self.color, (container_height//2, container_width//2), radius)
        # pygame.draw.line(self.point_surface, point_colour, (0, 0), (0, container_height), 3)
        return surface
    
    def create_line_surface(self):
        line_width = 10
        line_height = 3
        
        lineSurf = pygame.Surface((line_width, line_height), pygame.SRCALPHA)
        pygame.draw.line(lineSurf, self.color, (0,0), (line_width, 0), 3)
        return pygame.transform.rotate(lineSurf, self.aircraft.track * -1)
        # rect = rotSurf.get_rect(center=(self.x_coordinate, self.y_coordinate))
        

    def create_text_surface(self):
        """Populates text for sprite"""
        x_pixel_buffer = 5
        y_pixel_buffer = 5

        font = pygame.font.SysFont('helvetica', stg.ACFT_FONT)
        anti_aliasing = True
        first_line = self.aircraft.name
        second_line = self.aircraft.get_pretty_altitude().zfill(3) + ' ' + str(self.aircraft.type)
        third_line = str(int(self.aircraft.dist)) + 'NM'
        self.text_surface = font.render(first_line, anti_aliasing, (255, 255, 255))
        self.text_surface2 = font.render(second_line, anti_aliasing, (255, 255, 255))
        self.text_surface3 = font.render(third_line, anti_aliasing, (255, 255, 255))
        

    # def blitRotateCenter(surf, image, topleft, angle):
    #     rotated_image = pygame.transform.rotate(image, angle)
    #     new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    #     surf.blit(rotated_image, new_rect.topleft)
