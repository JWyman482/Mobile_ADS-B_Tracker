from queue import Empty

def get_aircraft(orig_message):

    if orig_message == Empty: exit()
    orig_message = orig_message.split("\n")
    # Split below breaks down the pieces of each message.
    for acft in orig_message:
        acft = acft.split(',')
        if len(acft) != 22:
            print("Less than 22")
            print(len(acft))
            continue

        if acft[0] != "MSG":
            print("Not MSG")
            continue
        
        # ICAO
        if acft[4] not in current_aircraft:
            current_aircraft[acft[4]] = {"Callsign": "", "Count": 0.0, "Alt": "", "Lat": "", "Lon": "", "Squawk": "", "Track": ""}
            # current_aircraft[acft[4]]["Count"] = time()
            # if s.getsockname()[0] == "127.0.0.1":
            #     current_aircraft[acft[4]]["Type"] = get_aircraft_type(acft[4])
        
        # Callsign
        if acft[10] != '' and acft[10] != current_aircraft[acft[4]]["Callsign"]:
            current_aircraft[acft[4]]["Callsign"] = acft[10]
            # current_aircraft[acft[4]]["Count"] = time()
        
        # Altitude
        if acft[11] != '' and acft[11] != current_aircraft[acft[4]]["Alt"]:
            current_aircraft[acft[4]]["Alt"] = acft[11]
            # current_aircraft[acft[4]]["Count"] = time()

        # Lat/Lon - we assume if we have one we have both
        if acft[14] != '' and (acft[14] != current_aircraft[acft[4]]["Lat"] or acft[15] != current_aircraft[acft[4]]["Lon"]):
            current_aircraft[acft[4]]["Lat"] = acft[14]
            current_aircraft[acft[4]]["Lon"] = acft[15]
            # current_aircraft[acft[4]]["Count"] = time()
    
        # Squawk
        if acft[17] != '' and acft[17] != current_aircraft[acft[4]]["Squawk"]:
            current_aircraft[acft[4]]["Squawk"] = acft[17]
            # current_aircraft[acft[4]]["Count"] = time()
        
        # Track
        if acft[13] != '' and acft[13] != current_aircraft[acft[4]]["Track"]:
            current_aircraft[acft[4]]["Track"] = acft[13]
            # current_aircraft[acft[4]]["Count"] = time()
            
    # time_out_acft(TIMEOUT)
    """
    current_aircraft structure:
    {
        "ICAO1": {
            "Callsign": "balls1",
            "Count": 0.0,
            "Alt": "9500",
            "Lat": "42.23423",
            "Lon": "-122.12321"
            "Track": "225",
        },
        "ICAO2": {
            "Callsign": "balls2",
            "Count": 0.0,
            "Alt": "9500",
            "Lat": "42.23423",
            "Lon": "-122.12321",
            "Track": "360"
        }
    }
    """
    print(current_aircraft)

if __name__ == '__main__':
    a = open("src/testData.txt", "r")
    orig_message = a.read()
    a.close()

    current_aircraft = {}

    
