import renderer
import settings
from pyembedded.gps_module.gps import GPS

def deg_to_dec(coord):
    # For example, for a DMS lat of 47.4791819
    deg = int(coord)            # deg = 47
    mins = (coord % deg) * 100  # mins = 47.91819
    minsDec = mins / 60         # minsDec = .798637
    result = deg + minsDec      # result = 47.798637
    return result

def main():
    print(f"1) Try GPS module\n2) Manually enter GPS coords\n3) Use current Coords ({settings.LAT, settings.LON})")
    choice = input(">")
    if int(choice) == 1:
        gps = GPS(port='/dev/ttyACM0', baud_rate=9600)
        coords = gps.get_lat_long()
        print(coords)
        i = 1
        while coords is None and i < 100000:
            coords = gps.get_lat_long()
            i += 1
        print(coords)
        settings.LAT = deg_to_dec(coords[0])
        settings.LON = deg_to_dec(coords[1]) * -1
        
    elif int(choice) == 2:
        latInput = input("Enter your latitude. Example - 46.333221: ")
        lonInput = input("Enter your longitude. Example - -120.2423: ")
        settings.LAT = float(latInput)
        settings.LON = float(lonInput)

    settings.NM_PER_DEGREE_LAT, settings.NM_PER_DEGREE_LON = settings.setLatLon(settings.LAT, settings.LON)
    
    renderer.run_screen()

if __name__ == '__main__':
    main()
