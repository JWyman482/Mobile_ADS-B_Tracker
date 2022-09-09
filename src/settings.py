import decoder # For GPS use
from haversine import haversine, Unit

def setLatLon(LAT, LON):
    distLat = haversine((LAT, LON), (LAT-1, LON), unit=Unit.NAUTICAL_MILES)
    distLon = haversine((LAT, LON), (LAT, LON-1), unit=Unit.NAUTICAL_MILES)
    return distLat, distLon

HOST = "127.0.0.1"
LAT, LON = 47.7997, -122.5100
# LAT, LON = decoder.get_lat_lon(HOST)
NM_PER_DEGREE_LAT, NM_PER_DEGREE_LON = setLatLon(LAT, LON)
BASE_FONT = 12
ACFT_FONT = 12
RANGE_NM = 40
RR_DIST = 10
ALT_FILTER = 400
PORT = 30003
HDR_SIZE = 4096
TIMEOUT = 60
SCREENSIZE = (750, 750)
X_PAD = 10
Y_PAD = 5
BAR_WIDTH = int(SCREENSIZE[0] / 5)
BAR_HEIGHT = BASE_FONT + Y_PAD

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
