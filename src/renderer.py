import pygame
import pygame_gui
import decoder
import settings as stg
from models.Aircraft import Aircraft
from models.BaseStation import BaseStation

DEBUG = False

def get_screen():
    """Returns the screen object"""
    pygame.init()
    pygame.font.init()
    return pygame.display.set_mode(stg.SCREENSIZE, pygame.RESIZABLE)


def draw_my_location(screen):
    """Draws the current user's location"""
    for airport in stg.airports:
        b = BaseStation(airport)
        if airport["Name"] == "Home":
           for radius in b.rr:
               pygame.draw.circle(screen, (84, 170, 232), (b.x_coordinate, b.y_coordinate), radius, 2)
        b.draw(screen)


def run_screen():
    if not DEBUG:
        decoder.connectToServer(stg.HOST, stg.PORT)

    screen = get_screen()
    manager = pygame_gui.UIManager(stg.SCREENSIZE)
    clock = pygame.time.Clock()
    is_running = True
    
    rr_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect = pygame.Rect(stg.RR_RECT), start_value=stg.RR_DIST, value_range=(5, 50), manager=manager)
    range_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect = pygame.Rect(stg.RANGE_RECT), start_value=stg.RANGE_NM, value_range=(10, 100), manager=manager)
    filter_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect = pygame.Rect(stg.FILTER_RECT), start_value=stg.ALT_FILTER, value_range=(40, 400), manager=manager)
    reset_button = pygame_gui.elements.UIButton(relative_rect= pygame.Rect(stg.RESET_RECT), text = "Reset", manager = manager)

    while is_running:
        time_delta = clock.tick(100)/1000.0

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
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        stg.ALT_FILTER = stg.ALT_FILTER + 20
                    else: 
                        stg.ALT_FILTER = stg.ALT_FILTER - 20
                if event.key == pygame.K_t:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        stg.ACFT_FONT = stg.ACFT_FONT + 1
                    else: 
                        stg.ACFT_FONT = stg.ACFT_FONT - 1
                
            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == rr_slider:
                    stg.RR_DIST = rr_slider.get_current_value()
                
                if event.ui_element == range_slider:
                    stg.RANGE_NM = range_slider.get_current_value()
                
                if event.ui_element == filter_slider:
                    stg.ALT_FILTER = filter_slider.get_current_value()
                
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == reset_button:
                    stg.RR_DIST = stg.DEF_RR_DIST
                    stg.RANGE_NM = stg.DEF_RANGE_NM
                    stg.ALT_FILTER = stg.DEF_ALT_FILTER
                
            manager.process_events(event)
        
        screen.fill((0, 0, 0))
        draw_my_location(screen)
        manager.update(time_delta)
        
        if not DEBUG: aircraftList = decoder.get_aircraft(stg.HDR_SIZE, stg.TIMEOUT)
        else: aircraftList = {}

        for aircraft in aircraftList:
            a = Aircraft(aircraftList[aircraft])
            a.draw(screen)
        
        manager.draw_ui(screen)
        pygame.display.flip()
        # pygame.time.wait(1000)
