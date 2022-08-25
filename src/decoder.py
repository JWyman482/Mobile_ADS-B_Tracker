import gps
import socket
from time import time

current_aircraft = {}


# Create the client socket
s = socket.socket()

def connectToServer(HOST, PORT):
    # Connect to receiver (server)
    print(f"[+] Connecting to {HOST}:{PORT}")
    s.connect((HOST, PORT))
    print("[+] Connected.")

# Delete timed out aircraft
def time_out_acft(TIMEOUT):
    timeNow = time()
    delList = []
    for acft in current_aircraft:
        if timeNow - current_aircraft[acft]["Count"] > float(TIMEOUT):
            delList.append(acft)
    for acft in delList:
        current_aircraft.pop(acft)

def get_aircraft(HDR_SIZE, TIMEOUT):
    # orig_message will be multiple acft in base-station format
    # The first split splits the msgs into individual messages
    orig_message = s.recv(HDR_SIZE).decode().split('\n')

    # Split below breaks down the pieces of each message.
    for acft in orig_message:
        acft = acft.split(',')
        if len(acft) != 22:
            continue

        if acft[0] != "MSG":
            continue
        
        # ICAO
        if acft[4] not in current_aircraft:
            current_aircraft[acft[4]] = {"Callsign": "", "Count": 0.0, "Alt": "", "Lat": "", "Lon": "", "Squawk": ""}
            current_aircraft[acft[4]]["Count"] = time()
        
        # Callsign
        if acft[10] != '' and acft[10] != current_aircraft[acft[4]]["Callsign"]:
            current_aircraft[acft[4]]["Callsign"] = acft[10]
            current_aircraft[acft[4]]["Count"] = time()
        
        # Altitude
        if acft[11] != '' and acft[11] != current_aircraft[acft[4]]["Alt"]:
            current_aircraft[acft[4]]["Alt"] = acft[11]
            current_aircraft[acft[4]]["Count"] = time()

        # Lat/Lon - we assume if we have one we have both
        if acft[14] != '' and (acft[14] != current_aircraft[acft[4]]["Lat"] or acft[15] != current_aircraft[acft[4]]["Lon"]):
            current_aircraft[acft[4]]["Lat"] = acft[14]
            current_aircraft[acft[4]]["Lon"] = acft[15]
            current_aircraft[acft[4]]["Count"] = time()
    
        # Squawk
        if acft[17] != '' and acft[17] != current_aircraft[acft[4]]["Squawk"]:
            current_aircraft[acft[4]]["Squawk"] = acft[17]
            current_aircraft[acft[4]]["Count"] = time()

    time_out_acft(TIMEOUT)
    """
    current_aircraft structure:
    {
        "ICAO1": {
            "Callsign": "balls1",
            "Count": 0.0,
            "Alt": "9500",
            "Lat": "42.23423",
            "Lon": "-122.12321"
        },
        "ICAO2": {
            "Callsign": "balls2",
            "Count": 0.0,
            "Alt": "9500",
            "Lat": "42.23423",
            "Lon": "-122.12321"
        }
    }
    """
    return current_aircraft

def get_lat_lon():
    # Listen on port 2947 (gpsd) of localhost
    session = gps.gps("192.168.1.34", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    lat = None
    lon = None

    while lat == None and lon == None:
        try:
            report = session.next()
            # Wait for a 'TPV' report and display the current time
            # To see all report data, uncomment the line below
            # print(report)
            if report['class'] == 'TPV':
                if hasattr(report, 'lat') and hasattr(report, 'lon'):
                    print(str(report.lat) + " " + str(report.lon))
                    lat = round(report.lat, 4)
                    lon = round(report.lon, 4)
                    print(str(lat) + " " + str(lon))
                    session = None
                    return lat, lon
        except KeyError:
            pass
        except KeyboardInterrupt:
            quit()
        except StopIteration:
            session = None
            print("GPSD has terminated")
