from sprites.BaseStationSprite import BaseStationSprite
import helpers
from settings import setting, airports

class BaseStation():
    """Class for representing a base station"""

    def __init__(self, airport):
        self.name = airport["Name"]
        self.lat = airport["LAT"]
        self.lon = airport["LON"]
        if self.name == "Home":
            print("in Home")
            screen_h, screen_w = helpers.get_screen_dimensions()
            x_coordinate = screen_w / 2
            y_coordinate = screen_h / 2
            self.rr = self.create_rr(setting["RR_DIST"])
        else: 
            x_coordinate, y_coordinate = helpers.assign_x_y_from_lat_lon(self.lat, self.lon)
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.create_sprite()

    def create_rr(self, rrdist):
        rr = []

        conversion = helpers.NM_per_pixel()

        for i in range (1, 10):
            rr_radius = rrdist * i * conversion
            rr.append(int(rr_radius))
        return rr


    def create_sprite(self):
        """Create the sprite for the base station"""
        rgb = (84, 170, 232)
        self.sprite = BaseStationSprite(rgb, self.name)

    def draw(self, screen):
        """Draw the base station on the screen"""
        x_pixel_buffer = 10
        screen.blit(self.sprite.point_surface, (self.x_coordinate, self.y_coordinate))
        # screen.blit(self.sprite.line_surface, (self.x_coordinate, self.y_coordinate))
        screen.blit(self.sprite.text_surface, (self.x_coordinate + x_pixel_buffer, self.y_coordinate))
        if self.name == "Home":
            screen.blit(self.sprite.rr_text_surface, (0, 0))
            screen.blit(self.sprite.ll_text_surface, (0, setting["BASE_FONT"] + 2))
