import pygame
import decoder
from settings import airports
from models.Aircraft import Aircraft
from models.BaseStation import BaseStation
from models.AlertMessage import AlertMessage

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


def display_aircraft_los(screen):
    """Draws LOS aircraft on screen"""
    a = AlertMessage('LOS - ADS-B Aircraft')
    a.draw(screen)


def run_screen():
    """Runs the screen"""
    screen = get_screen()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                running = False
        screen.fill((0, 0, 0))
        for aircraft_json in decoder.get_aircraft():
            acft_type = decoder.get_aircraft_type(aircraft_json["hex"])
            aircraft_json["type"] = acft_type
            a = Aircraft(aircraft_json)
            a.draw(screen)
        draw_my_location(screen)
        display_aircraft_los(screen)
        pygame.display.flip()
        pygame.time.wait(1000)
