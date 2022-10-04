# Mobile ADS-B Tracker 
## Description
A project to track the location of nearby aircraft with a Raspberry Pi and an ADS-B receiver.

## Steps to prepare:
1. Double click the desktop icon OR run run.sh.
2. Lat: 60nm / deg, Lng: 40nm / deg at 48 deg N

# Mobile ADS-B Tracker 

# GPS
[Follow these directions](https://canadagps.ca/blogs/knowledgebase-by-platform-linux/how-to-connect-an-usb-gps-receiver-with-a-linux-computer)

- sudo apt install gpsd
- sudo gpsd -D 5 -N -n /dev/ttyACM0
- sudo apt install gpsd-clients  
To test:  
- gpspipe -w -n 10 | grep -m 1 lon
if lat/lon is 0, try:
- sudo dpkg-reconfigure gpsd  

- To make gpsd startup automatic:  
  - Update /etc/default/gpsd
  - DEVICES=""
  - GPSD_OPTIONS="/dev/ttyACM0"
  - START_DAEMON="true"  
