import renderer
import settings as stg
# from settings import setting

def main():
    """Main entrypoint for application"""
    # choice = input("Defaults (y/n)")
    # if choice.lower() != "y":
    #     stg.RANGE_NM = int(input("Range: "))
    #     stg.RR_DIST = int(input("Range Rings: "))
    #     stg.ACFT_FONT = int(input("Aircraft Font Size: "))
    #     stg.BASE_FONT = int(input("Base Font Size: "))
    #     stg.HOST = input("Host: ")
    #     print(stg.RANGE_NM)
    renderer.run_screen()

if __name__ == '__main__':
    main()
