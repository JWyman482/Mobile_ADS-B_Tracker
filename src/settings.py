import decoder
from haversine import haversine, Unit


LAT, LON = decoder.get_lat_lon()
# LAT, LON = 43.57212,-90.40166

distLat = haversine((LAT, LON), (LAT-1, LON), unit=Unit.NAUTICAL_MILES)
distLon = haversine((LAT, LON), (LAT, LON-1), unit=Unit.NAUTICAL_MILES)

setting = {
    "BASE_FONT": 15,
    "ACFT_FONT": 15,
    "RANGE_NM": 30,
    "RR_DIST": 10,
    "LAT": LAT,
    "LON": LON,
    "NM_PER_DEGREE_LAT": 60,
    "NM_PER_DEGREE_LON": 40,
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
        "LAT": 47.26993,
        "LON": -122.1871,
        "RWY": 160
    },
    {
        "Name": "BFI",
        "Type": "Airport",
        "LAT": 47.3180,
        "LON": -122.1812,
        "RWY": 140
    }
]
