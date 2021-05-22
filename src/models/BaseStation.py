from sprites.BaseStationSprite import BaseStationSprite
import helpers


class BaseStation():
    """Class for representing a base station"""

    def __init__(self, lat, lng, rrdist, name='Home'):
        self.lat = lat
        self.lng = lng
        self.name = name
        self.rrdist = rrdist
        x_coordinate, y_coordinate = helpers.assign_x_y_from_lat_lon(self.lat, self.lng)
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.rr = self.create_rr(rrdist)
        self.create_sprite()

    def create_rr(self, rrdist):
        """Create range rings"""
        rr = []
        screen_h, screen_w = helpers.get_screen_dimensions()
        # if screen_h = 100 pixels, (rrdist = 50 NM * 2) = 100, conv = 1 pix/NM
        # Change 30 below to the chosen range
        conversion = screen_h / (30 * 2)
        # print(f"Conversion: {conversion}") 

        for i in range (1, 10):
            rr_radius = rrdist * i * conversion
            # print(rr_radius)
            rr.append(int(rr_radius))
        return rr

    def create_sprite(self):
        """Create the sprite for the aircraft"""
        rgb = (84, 170, 232)
        height = 15
        length = 15
        self.sprite = BaseStationSprite(rgb, self.rrdist, self.lat, self.lng)

    def draw(self, screen):
        """Draw the aircraft on the screen"""
        x_pixel_buffer = 10
        screen.blit(self.sprite.point_surface, (self.x_coordinate, self.y_coordinate))
        screen.blit(self.sprite.text_surface,(self.x_coordinate + x_pixel_buffer, self.y_coordinate))
        screen.blit(self.sprite.rr_text_surface, (0, 0))
        screen.blit(self.sprite.ll_text_surface, (0, 22))
