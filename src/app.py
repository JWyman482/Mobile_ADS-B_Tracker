from json import decoder
import renderer
import settings
import decoder

def main():
    """Main entrypoint for application"""
    print(f"1) Try GPS module\n2) Manually enter GPS coords\n3) Use current Coords ({settings.LAT, settings.LON})")
    choice = input(">")
    if int(choice) == 1:
        settings.LAT, settings.LON = decoder.get_lat_lon()
        
    elif int(choice) == 2:
        latInput = input("Enter your latitude. Example - 46.333221: ")
        lonInput = input("Enter your longitude. Example - -120.2423: ")
        settings.LAT = float(latInput)
        settings.LON = float(lonInput)

    settings.NM_PER_DEGREE_LAT, settings.NM_PER_DEGREE_LON = settings.setLatLon(settings.LAT, settings.LON)
    
    renderer.run_screen()

if __name__ == '__main__':
    main()
