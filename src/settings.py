# from tkinter import Y
import decoder # For GPS use
from haversine import haversine, Unit

def setLatLon(LAT, LON):
    distLat = haversine((LAT, LON), (LAT-1, LON), unit=Unit.NAUTICAL_MILES)
    distLon = haversine((LAT, LON), (LAT, LON-1), unit=Unit.NAUTICAL_MILES)
    return distLat, distLon

HOST = "127.0.0.1"
PORT = 30003
LAT, LON = 47.7997, -122.5100
# LAT, LON = decoder.get_lat_lon(HOST)
NM_PER_DEGREE_LAT, NM_PER_DEGREE_LON = setLatLon(LAT, LON)
DEF_RANGE_NM = 40
DEF_RR_DIST = 10
DEF_ALT_FILTER = 400
BASE_FONT = 15
ACFT_FONT = 12
RANGE_NM = DEF_RANGE_NM
RR_DIST = DEF_RR_DIST
ALT_FILTER = DEF_ALT_FILTER
HDR_SIZE = 4096
TIMEOUT = 60
SCREENSIZE = (750, 750)

""" UI Settings """
X_PAD = 10
Y_PAD = 5
BAR_WIDTH = int(SCREENSIZE[0] / 5)
BAR_HEIGHT = BASE_FONT
LL_X = 0
LL_Y = 0
LL_XY = (LL_X, LL_Y)
BAR_X = 0
BAR_Y = BASE_FONT + Y_PAD
RR_XY = (BAR_WIDTH + X_PAD, BAR_Y)
RANGE_XY = (BAR_WIDTH + X_PAD, BAR_Y * 2)
# FILT_X = 0
# FILT_Y = (BASE_FONT + Y_PAD) * 3
FILT_XY = (BAR_WIDTH + X_PAD, BAR_Y * 3)
RR_RECT = (BAR_X, BAR_Y, BAR_WIDTH, BAR_HEIGHT)
RANGE_RECT = (BAR_X, BAR_Y * 2, BAR_WIDTH, BAR_HEIGHT)
FILTER_RECT = (BAR_X, BAR_Y * 3, BAR_WIDTH, BAR_HEIGHT)
RESET_RECT = (BAR_X, BAR_Y * 4, 100, BAR_HEIGHT * 2)

airports = [
    {
        "Name": "Home",
        "Type": "Airport",
        "LAT": LAT,
        "LON": LON,
        "RWY": 90
    },
    {
        "Name": "SEA",
        "Type": "Airport",
        "LAT": 47.449221,
        "LON": -122.311119,
        "RWY": 160
    },
    {
        "Name": "BFI",
        "Type": "Airport",
        "LAT": 47.5301,
        "LON": -122.3025,
        "RWY": 140
    }
]
