import pygame
import decoder
from settings import airports
from settings import setting
from models.Aircraft import Aircraft
from models.BaseStation import BaseStation

def get_screen():
    """Returns the screen object"""
    pygame.init()
    pygame.font.init()
    return pygame.display.set_mode((1000,1000), pygame.RESIZABLE)


def draw_my_location(screen):
    """Draws the current user's location"""
    for airport in airports:
        b = BaseStation(airport)
        b.draw(screen)
        if airport["Name"] == "Home":
           for radius in b.rr:
               pygame.draw.circle(screen, (84, 170, 232), (b.x_coordinate, b.y_coordinate), radius, 2)

def run_screen():
    """Runs the screen"""
    screen = get_screen()
    running = True
    decoder.connectToServer(setting['HOST'], setting['PORT'])
    setting["Filter"] = 400

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    setting["RANGE_NM"] = setting["RANGE_NM"] + 1
                if event.key == pygame.K_DOWN:
                    setting["RANGE_NM"] = setting["RANGE_NM"] - 1
                if event.key == pygame.K_LEFT:
                    setting["RR_DIST"] = setting["RR_DIST"] - 1
                if event.key == pygame.K_RIGHT:
                    setting["RR_DIST"] = setting["RR_DIST"] + 1
                if event.key == pygame.K_f:
                    setting["Filter"] = setting['Filter'] - 20
                if event.key == pygame.K_g:
                    setting["Filter"] = setting['Filter'] + 20
                # running = False
        screen.fill((0, 0, 0))
        draw_my_location(screen)
        aircraftList = decoder.get_aircraft(setting['HDR_SIZE'], setting['TIMEOUT'])
        for aircraft in aircraftList:
            a = Aircraft(aircraftList[aircraft])
            a.draw(screen)
        
        pygame.display.flip()
        pygame.time.wait(1000)
