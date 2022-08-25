import pyModeS as pms
import socket
import pprint
from time import time
import pygame

HDR_SIZE = 4096 
HOST = "192.168.1.37"
PORT = 30003
TIMEOUT = 60
acftDB = {}
run = True

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Radar")

def draw_window():
    WIN.fill((255,255,255))

# Delete timed out aircraft
def time_out_acft():
    timeNow = time()
    delList = []
    for acft in acftDB:
        if timeNow - acftDB[acft]["Count"] > float(TIMEOUT):
            delList.append(acft)
    for acft in delList:
        acftDB.pop(acft)

# Create the client socket
s = socket.socket()

# Connect to receiver (server)
print(f"[+] Connecting to {HOST}:{PORT}")
s.connect((HOST, PORT))
print("[+] Connected.")

while run:
    orig_message = s.recv(HDR_SIZE).decode().split('\n')
    for acft in orig_message:
        acft = acft.split(',')
        if len(acft) != 22:
            continue

        if acft[0] != "MSG":
            continue
        
        # ICAO
        if acft[4] not in acftDB:
            acftDB[acft[4]] = {"Callsign": "", "Count": 0.0, "Alt": "", "Lat": "", "Lon": ""}
            acftDB[acft[4]]["Count"] = time()
        
        # Callsign
        if acft[10] != '' and acft[10] != acftDB[acft[4]]["Callsign"]:
            acftDB[acft[4]]["Callsign"] = acft[10]
            acftDB[acft[4]]["Count"] = time()
        
        # Altitude
        if acft[11] != '' and acft[11] != acftDB[acft[4]]["Alt"]:
            acftDB[acft[4]]["Alt"] = acft[11]
            acftDB[acft[4]]["Count"] = time()

        # Lat/Lon - we assume if we have one we have both
        if acft[14] != '' and (acft[14] != acftDB[acft[4]]["Lat"] or acft[15] != acftDB[acft[4]]["Lon"]):
            acftDB[acft[4]]["Lat"] = acft[14]
            acftDB[acft[4]]["Lon"] = acft[15]
            acftDB[acft[4]]["Count"] = time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    time_out_acft()
    pprint.pprint(acftDB)

s.close()
