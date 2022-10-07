import pygame
import settings as stg
from haversine import haversine, Unit

def get_screen_dimensions():
    """Returns dimensions in pixels of the current screen"""
    return (pygame.display.Info().current_h, pygame.display.Info().current_w)

def NM_per_pixel():
    screen_h, screen_w = get_screen_dimensions()
    # If screen_h is 600 pixels and stg.RANGE_NM is 30 NM, conv = 10 pix/NM
    return screen_h / (stg.RANGE_NM * 2)

def get_degrees_from_NM(nm, type):
    if type == "lat":
        return nm / stg.NM_PER_DEGREE_LAT
    if type == "lon":
        return nm / stg.NM_PER_DEGREE_LON

def get_NM_from_degrees(deg, type):
    if type == "lat":
        return deg * stg.NM_PER_DEGREE_LAT
    if type == "lon":
        return deg * stg.NM_PER_DEGREE_LON

def get_bounding_box_coordinates():
    """Get the lat,lon coordinates of the bounding box"""
    screen_h, screen_w = get_screen_dimensions()
    total_screen_w_in_NM = screen_w / NM_per_pixel()
    lat_max = stg.LAT + get_degrees_from_NM(stg.RANGE_NM, "lat")
    lat_min = stg.LAT - get_degrees_from_NM(stg.RANGE_NM, "lat")
    lon_max = stg.LON - get_degrees_from_NM(total_screen_w_in_NM / 2, "lon")
    lon_min = stg.LON + get_degrees_from_NM(total_screen_w_in_NM / 2, "lon")
    return {
        'lat_max': lat_max,
        'lat_min': lat_min,
        'lon_max': lon_max,
        'lon_min': lon_min,
    }

def assign_x_y_from_lat_lon(lat, lng):
    # Get base coords and base degrees.
    # Get difference in degrees from base to target
    # Multiply differences in degrees lat/lng by NM/lat, NM/LON to get NM diff X, NM diff Y
    # Multiply NM_diff_x and NM_diff_y by NM_per_pixel for each
    # Add result to base coords(x) and base coords(y) for position.
    screen_h, screen_w = get_screen_dimensions()
    conversion = NM_per_pixel()

    # Assume screen is 500 x 500
    # Assume Home lon = -120, lat = 40
    # Assume passed lng, lat = -119, 39

    # base_x, y = 250, 250
    base_x, base_y = screen_w / 2, screen_h / 2

    # base_lng = -120, base_lat = 40
    base_lng, base_lat = stg.LON, stg.LAT

    # deg_diff_lng = -119 - -120 = 1 (one degree 'right' or East)
    # deg_diff_lat = 39 - 40 = -1 (one degree 'down' or South)
    deg_diff_lng, deg_diff_lat = lng - base_lng, lat - base_lat

    # NM_diff_x = 1 (one degree 'right') * NM/degree longitude, basically how many NM left/right from the base is it
    # we'll say 40 for lng
    # NM_diff_y = -1 (one degree 'down') * NM/degree latitude, basically how many NM up/down from the base is it
    # we'll say 60 for lat
    NM_diff_x, NM_diff_y = get_NM_from_degrees(deg_diff_lng, "lon"), get_NM_from_degrees(deg_diff_lat, "lat")

    # px_diff_x = horizontal difference in NM from the tgt to base * screen height in (px) / vertical range of the screen (NM)
    px_diff_x, px_diff_y = NM_diff_x * conversion, NM_diff_y * conversion

    tgt_x, tgt_y = base_x + px_diff_x, base_y + px_diff_y * -1
    # tgt_x, tgt_y = px_diff_x - base_x,

    #TODO Check this -1
    return tgt_x, tgt_y

def get_distance(lat, lng):
    base = stg.LAT, stg.LON
    dist = haversine(base, (lat, lng), unit=Unit.NAUTICAL_MILES)
    return dist