import renderer
from settings import setting

def main():
    """Main entrypoint for application"""
    choice = input("Defaults (y/n)")
    if choice.lower() != "y":
        setting["RANGE_NM"] = int(input("Range: "))
        setting["RR_DIST"] = int(input("Range Rings: "))
        setting["ACFT_FONT"] = int(input("Aircraft Font Size: "))
        setting["BASE_FONT"] = int(input("Base Font Size: "))
    renderer.run_screen()


if __name__ == '__main__':
    main()
