from sprites.AircraftSprite import AircraftSprite
import helpers
from settings import setting


class Aircraft():
    """Class for representing an aircraft on-screen"""

    def __init__(self, aircraft_dict):
        self.normalize_inputs(aircraft_dict)
        if self.should_draw:
            self.dist = helpers.get_distance(self.lat, self.lng)
            self.type = aircraft_dict.get('type')
            self.create_sprite()
            x_coordinate, y_coordinate = helpers.assign_x_y_from_lat_lon(self.lat, self.lng)
            self.x_coordinate = x_coordinate
            self.y_coordinate = y_coordinate
            self.check_aircraft_bounds()

    def normalize_inputs(self, aircraft_dict):
        """Normalizes ever changing inputs from aircraft_dict"""
        self.name = 'Unknown'
        self.lat = None
        self.lng = None
        self.squawk = None
        self.alt = None
        self.track = None
        self.should_draw = True

        name_retrieved = aircraft_dict.get('flight')
        lat_retrieved = aircraft_dict.get('lat')
        lng_retrieved = aircraft_dict.get('lon')
        squawk_retrieved = aircraft_dict.get('squawk')
        alt_retrieved = aircraft_dict.get('alt_baro')
        track_retrieved = aircraft_dict.get('track')

        if name_retrieved:
            self.name = name_retrieved.strip()
        if lat_retrieved:
            self.lat = float(lat_retrieved)
        else:
            self.should_draw = False
        if lng_retrieved:
            self.lng = float(lng_retrieved)
        else:
            self.should_draw = False
        if squawk_retrieved:
            if type(squawk_retrieved) == tuple:
                self.squawk = int(squawk_retrieved[0])
            else:
                self.squawk = int(squawk_retrieved)
        if alt_retrieved:
            if type(alt_retrieved) == tuple:
                self.alt = int(alt_retrieved[0])
            else:
                if alt_retrieved == "ground":
                    self.alt = 0
                else: 
                    self.alt = int(alt_retrieved)
        if track_retrieved:
            if type(track_retrieved) == tuple:
                self.track = int(track_retrieved[0])
            else:
                self.track = int(track_retrieved)

    def check_aircraft_bounds(self):
        """Determines if the aircraft is within reporting bounds"""
        bb = helpers.get_bounding_box_coordinates()
        if not bb['lat_min'] < float(self.lat) < bb['lat_max']:
            self.is_in_bounds = False
        if not bb['lon_min'] < float(self.lng) < bb['lon_max']:
            self.is_in_bounds = False
        self.is_in_bounds = True

    def create_sprite(self):
        """Create the sprite for the aircraft"""
        self.sprite = AircraftSprite(self)

    def get_pretty_altitude(self):
        if self.alt:
            if self.alt == "ground":
                self.alt = 0 
            pretty_alt = int(self.alt/100)
            return f'{pretty_alt}'
        return 'XXX'

    def update_position(self, lat, lng):
        """Updates the position of the aircraft"""
        pass

    def draw(self, screen):
        """Draw the aircraft on the screen"""
        x_pixel_buffer = 10
        if self.should_draw:
            if self.is_in_bounds:
                screen.blit(self.sprite.point_surface, (self.x_coordinate, self.y_coordinate))
                screen.blit(
                    self.sprite.text_surface,
                    (self.x_coordinate + x_pixel_buffer, self.y_coordinate)
                )
                screen.blit(
                    self.sprite.text_surface2,
                    (self.x_coordinate + x_pixel_buffer, self.y_coordinate + setting["ACFT_FONT"])
                )
                screen.blit(
                    self.sprite.text_surface3,
                    (self.x_coordinate + x_pixel_buffer, self.y_coordinate + (2*setting["ACFT_FONT"]))
                )
