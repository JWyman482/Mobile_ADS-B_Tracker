from sprites.BaseStationSprite import BaseStationSprite
import helpers
import settings as stg
# from settings import airports

class BaseStation():
    """Class for representing a base station"""

    def __init__(self, airport):
        self.name = airport["Name"]
        self.lat = airport["LAT"]
        self.lon = airport["LON"]
        self.rwy = airport["RWY"]
        if self.name == "Home":
            # stg.SCREENSIZE = helpers.get_screen_dimensions()
            # stg.BAR_WIDTH = int(stg.SCREENSIZE[1] / 5)
            # screen_h, screen_w = stg.SCREENSIZE[0], stg.SCREENSIZE[1]
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
        for i in range (1, 20):
            rr_radius = rrdist * i * conversion
            rr.append(int(rr_radius))
        return rr

    def create_sprite(self):
        """Create the sprite for the base station"""
        rgb = (250, 170, 0)
        self.sprite = BaseStationSprite(rgb, self.rwy * -1, self.name)
        # self.sprite = BaseStationSprite(self.name)

    def draw(self, screen):
        """Draw the base station on the screen"""
        lineRect = self.sprite.line_surface.get_rect(center = (self.x_coordinate, self.y_coordinate))
        # lineRect = self.x_coordinate, self.y_coordinate
        # screen.blit(self.sprite.point_surface, (self.x_coordinate, self.y_coordinate))
        screen.blit(self.sprite.line_surface, lineRect)
        # screen.blit(self.sprite.text_surface, (self.x_coordinate + stg.X_PAD, self.y_coordinate))
        labelRect = self.sprite.text_surface.get_rect(center = (self.x_coordinate, self.y_coordinate))
        screen.blit(self.sprite.text_surface, labelRect)
        if self.name == "Home":
            screen.blit(self.sprite.ll_text_surface, stg.LL_XY)
            screen.blit(self.sprite.rr_text_surface, stg.RR_XY)
            screen.blit(self.sprite.range_text_surface, stg.RANGE_XY)
            screen.blit(self.sprite.filt_text_surface, stg.FILT_XY)
