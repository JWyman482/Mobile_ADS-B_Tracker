# from json import decoder
# from types import NoneType
import renderer
import settings
import decoder
from pyembedded.gps_module.gps import GPS

def main():
    print(f"1) Try GPS module\n2) Manually enter GPS coords\n3) Use current Coords ({settings.LAT, settings.LON})")
    choice = input(">")
    if int(choice) == 1:
        # settings.LAT, settings.LON = decoder.get_lat_lon(settings.HOST)
        # tempLat, tempLon = decoder.get_lat_lon()
        gps = GPS(port='/dev/ttyACM0', baud_rate=9600)
        coords = gps.get_lat_long()
        print(coords)
        # if coords is not None:
        #     settings.LAT = coords[0]
        #     settings.LON = coords[1] * -1
        
        i = 1
        while coords is None and i < 100000:
            coords = gps.get_lat_long()
            i += 1
        print(coords)
        settings.LAT = coords[0]
        settings.LON = coords[1] * -1

        # print(f"Lat: {}, Lon: {tempLon}")
        # if tempLat != 0:
        #     settings.LAT, settings.LON = tempLat, tempLon
        
    elif int(choice) == 2:
        latInput = input("Enter your latitude. Example - 46.333221: ")
        lonInput = input("Enter your longitude. Example - -120.2423: ")
        settings.LAT = float(latInput)
        settings.LON = float(lonInput)

    settings.NM_PER_DEGREE_LAT, settings.NM_PER_DEGREE_LON = settings.setLatLon(settings.LAT, settings.LON)
    
    renderer.run_screen()

if __name__ == '__main__':
    main()
