import pygame
import pygame_gui
import decoder
import settings as stg
from models.Aircraft import Aircraft
from models.BaseStation import BaseStation

DEBUG = True

def get_screen():
    """Returns the screen object"""
    pygame.init()
    pygame.font.init()
    return pygame.display.set_mode(stg.SCREENSIZE, pygame.RESIZABLE)


def draw_my_location(screen):
    """Draws the current user's location"""
    for airport in stg.airports:
        b = BaseStation(airport)
        b.draw(screen)
        if airport["Name"] == "Home":
           for radius in b.rr:
               pygame.draw.circle(screen, (84, 170, 232), (b.x_coordinate, b.y_coordinate), radius, 2)

def run_screen():
    if not DEBUG:
        decoder.connectToServer(stg.HOST, stg.PORT)
    
    """Runs the screen"""
    screen = get_screen()
    manager = pygame_gui.UIManager((750,750))
    clock = pygame.time.Clock()
    is_running = True
    
    # hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(50, 50, 350, 275), text = 'Say Hello', manager=manager)
    Text_Test = pygame_gui.elements.UIHorizontalSlider(relative_rect = pygame.Rect(0, 0, stg.BAR_WIDTH, stg.BAR_HEIGHT), start_value=stg.RR_DIST, value_range=(5, 50), manager=manager)

    while is_running:
        time_delta = clock.tick(60)/1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    stg.RANGE_NM = stg.RANGE_NM + 1
                if event.key == pygame.K_DOWN:
                    stg.RANGE_NM = stg.RANGE_NM - 1
                if event.key == pygame.K_LEFT:
                    stg.RR_DIST = stg.RR_DIST - 1
                if event.key == pygame.K_RIGHT:
                    stg.RR_DIST = stg.RR_DIST + 1
                if event.key == pygame.K_f:
                    stg.ALT_FILTER = stg.ALT_FILTER - 20
                if event.key == pygame.K_g:
                    stg.ALT_FILTER = stg.ALT_FILTER + 20
            
            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == Text_Test:
                    print(Text_Test.get_current_value())
                    stg.RR_DIST = Text_Test.get_current_value()
                
            manager.process_events(event)
        
        manager.update(time_delta)
        screen.fill((0, 0, 0))
        draw_my_location(screen)
        
        if not DEBUG: aircraftList = decoder.get_aircraft(stg.HDR_SIZE, stg.TIMEOUT)
        else: aircraftList = {}

        for aircraft in aircraftList:
            a = Aircraft(aircraftList[aircraft])
            a.draw(screen)
        
        manager.draw_ui(screen)
        pygame.display.flip()
        # pygame.time.wait(1000)
