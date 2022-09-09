from sprites.BaseStationSprite import BaseStationSprite
import helpers
import settings as stg

class BaseStation():
    """Class for representing a base station"""

    def __init__(self, airport):
        self.name = airport["Name"]
        self.lat = airport["LAT"]
        self.lon = airport["LON"]
        if self.name == "Home":
            screen_h, screen_w = helpers.get_screen_dimensions()
            x_coordinate = int(screen_w / 2)
            y_coordinate = int(screen_h / 2)
            self.rr = self.create_rr(stg.RR_DIST)
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
        x_pixel_buffer = stg.X_PAD
        y_pixel_buffer = stg.Y_PAD
        screen.blit(self.sprite.point_surface, (self.x_coordinate, self.y_coordinate))
        # screen.blit(self.sprite.line_surface, (self.x_coordinate, self.y_coordinate))
        screen.blit(self.sprite.text_surface, (self.x_coordinate + x_pixel_buffer, self.y_coordinate))
        if self.name == "Home":
            screen.blit(self.sprite.rr_text_surface, (stg.BAR_WIDTH + x_pixel_buffer, 0))
            screen.blit(self.sprite.range_text_surface, (stg.BAR_WIDTH + stg.X_PAD, stg.BASE_FONT + stg.Y_PAD))
            screen.blit(self.sprite.ll_text_surface, (0, stg.BASE_FONT * 2 + y_pixel_buffer))
            screen.blit(self.sprite.filt_text_surface, (0, stg.BASE_FONT * 3 + y_pixel_buffer))
