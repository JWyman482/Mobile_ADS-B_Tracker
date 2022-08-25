import decoder # For GPS use
from haversine import haversine, Unit


LAT, LON = 47.7997, -122.5100
HOST = "127.0.0.1"
# LAT, LON = decoder.get_lat_lon(HOST)
def setLatLon(LAT, LON):
    distLat = haversine((LAT, LON), (LAT-1, LON), unit=Unit.NAUTICAL_MILES)
    distLon = haversine((LAT, LON), (LAT, LON-1), unit=Unit.NAUTICAL_MILES)
    return distLat, distLon

distLat, distLon = setLatLon(LAT, LON)

setting = {
    "BASE_FONT": 12,
    "ACFT_FONT": 12,
    "RANGE_NM": 40,
    "RR_DIST": 10,
    "LAT": LAT,
    "LON": LON,
    "NM_PER_DEGREE_LAT": distLat,
    "NM_PER_DEGREE_LON": distLon,
    "ALT_FILTER": 400,
    "HOST": HOST,
    "PORT": 30003,
    "HDR_SIZE": 4096,
    "TIMEOUT": 60
}

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
