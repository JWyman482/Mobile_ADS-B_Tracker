import renderer
import settings

def main():
    """Main entrypoint for application"""
    choice = input("1) Try GPS module\n2) Manual GPS\n:> ")
    if int(choice) == 1:
        settings.GPS = True
    elif int(choice) == 2:
        latInput = input("Enter your latitude. Example - 46.333221: ")
        lonInput = input("Enter your longitude. Example - -120.2423: ")
        settings.LAT = float(latInput)
        settings.LON = float(lonInput)

    renderer.run_screen()

if __name__ == '__main__':
    main()
