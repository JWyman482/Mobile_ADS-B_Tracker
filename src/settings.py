import decoder

LAT, LON = decoder.get_lat_lon()
# LAT, LON = 43.57212,-90.40166

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
        "LAT": 47.45193,
        "LON": -122.30952,
        "RWY": 160
    }
]
