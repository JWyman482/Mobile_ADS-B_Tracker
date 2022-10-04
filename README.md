# Mobile ADS-B Tracker 
## Description
A project to track the location of nearby aircraft with a Raspberry Pi and an ADS-B receiver.

## Steps to prepare:
1. Double click the desktop icon OR run run.sh.
2. Lat: 60nm / deg, Lng: 40nm / deg at 48 deg N

# Mobile ADS-B Tracker 

# GPS

## Install Updates
sudo apt-get update
sudo apt-get upgrade

## see USB devices
lsusb

## Install GPS software
sudo apt -y install gpsd gpsd-clients python-gps 

## Edit GPS config file
sudo nano /etc/default/gpsd

## Add this to file
START_DAEMON=”true”

USBAUTO=”true”

DEVICES=”/dev/ttyACM0″

GPSD_OPTIONS=”-n”

## Install chrony
sudo apt-get install chrony

## reboot pi

## check to see if services are running
systemctl is-active gpsd
systemctl is-active chronyd

## Check GPS output
cgps – s
gpsmon -n

## Edit chrony config file
sudo nano /etc/chrony/chrony.conf

## Add this to end of file
refclock SHM 0 offset 0.5 delay 0.2 refid NMEA

## Check Chrony Output
sudo chronyc sources -v

## Check chrony output
sudo chronyc tracking

## Force time sync
sudo chronyc makestep