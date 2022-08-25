import decoder
from haversine import haversine, Unit


# LAT, LON = decoder.get_lat_lon()
LAT, LON = 47.7997, -122.5100

distLat = haversine((LAT, LON), (LAT-1, LON), unit=Unit.NAUTICAL_MILES)
distLon = haversine((LAT, LON), (LAT, LON-1), unit=Unit.NAUTICAL_MILES)

setting = {
    "BASE_FONT": 15,
    "ACFT_FONT": 15,
    "RANGE_NM": 30,
    "RR_DIST": 10,
    "LAT": LAT,
    "LON": LON,
    "NM_PER_DEGREE_LAT": distLat,
    "NM_PER_DEGREE_LON": distLon,
    "ALT_FILTER": 60
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
