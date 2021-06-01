import os
import pygame
from settings import setting
from haversine import haversine, Unit

def get_screen_dimensions():
    """Returns dimensions in pixels of the current screen"""
    return (pygame.display.Info().current_h, pygame.display.Info().current_w)

def NM_per_pixel():
    screen_h, screen_w = get_screen_dimensions()
    # If screen_h is 600 pixels and RANGE_NM is 30 NM, conv = 10 pix/NM
    return screen_h / (setting["RANGE_NM"] * 2)

def get_degrees_from_NM(nm, type):
    #type = "lat" or "lon"
    if type == "lat":
        return nm / setting["NM_PER_DEGREE_LAT"]
    if type == "lon":
        return nm / setting["NM_PER_DEGREE_LON"]

def get_NM_from_degrees(deg, type):
    if type == "lat":
        return deg * setting["NM_PER_DEGREE_LAT"]
    if type == "lon":
        return deg * setting["NM_PER_DEGREE_LON"]

def get_bounding_box_coordinates():
    """Get the lat,lon coordinates of the bounding box"""
    screen_h, screen_w = get_screen_dimensions()
    total_screen_w_in_NM = screen_w / NM_per_pixel()
    lat_max = setting["LAT"] + get_degrees_from_NM(setting["RANGE_NM"], "lat")
    lat_min = setting["LAT"] - get_degrees_from_NM(setting["RANGE_NM"], "lat")
    lon_max = setting["LON"] - get_degrees_from_NM(total_screen_w_in_NM / 2, "lon")
    lon_min = setting["LON"] + get_degrees_from_NM(total_screen_w_in_NM / 2, "lon")
    return {
        'lat_max': lat_max,
        'lat_min': lat_min,
        'lon_max': lon_max,
        'lon_min': lon_min,
    }


def assign_x_y_from_lat_lon(lat, lng):
    """Assign x and y coordinates of the sprite from lat and long"""
    screen_height, screen_width = get_screen_dimensions()
    bb_coordinates = get_bounding_box_coordinates()
    lat_percent = (lat - bb_coordinates['lat_min']) / (bb_coordinates['lat_max'] - bb_coordinates['lat_min'])
    lng_percent = (lng - bb_coordinates['lon_min']) / (bb_coordinates['lon_max'] - bb_coordinates['lon_min'])
    x_coordinate = int((1 - lng_percent) * screen_width)
    y_coordinate = int((1 - lat_percent) * screen_height)
    return x_coordinate, y_coordinate

def get_distance(lat, lng):
    base = setting["LAT"], setting["LON"]
    dist = haversine(base, (lat, lng), unit=Unit.NAUTICAL_MILES)
    return dist



