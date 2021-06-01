import decoder

LAT, LON = decoder.get_lat_lon()

setting = {
    "BASE_FONT": 15,
    "ACFT_FONT": 15,
    "RANGE_NM": 30,
    "RR_DIST": 10,
    "LAT": LAT,
    "LON": LON,
    "NM_PER_DEGREE_LAT": 60,
    "NM_PER_DEGREE_LON": 40
}

airports = [
    {
        "Name": "Home",
        "LAT": LAT,
        "LON": LON,
        "RWY": 90
    },
    {
        "Name": "SEA",
        "LAT": 47.45193,
        "LON": -122.30952,
        "RWY": 160
    }
]