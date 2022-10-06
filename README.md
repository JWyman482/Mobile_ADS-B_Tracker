# Mobile ADS-B "Radar"
## Description

It takes in raw ADS-B signals via software defined radio, then uses dump1090 to translate that into basestation format and rebroadcast that over port 30003 on the local network. This software connects to the broadcasting device, collects the data and drops it into an ATC friendly UI.

### Run Instructions:
1. Run dump1090 --net  
2. Run src/app.py

### Notes:
Calculates nautical miles (NM) per degree of lattitude as 60 NM / degree, and longitude as 40 NM / degree at 48 degrees North.  

## System Components
### Dump1090

    $ git clone https://github.com/flightaware/dump1090.git  
    $ sudo apt-get install build-essential debhelper librtlsdr-dev pkg-config dh-systemd libbladerf-dev  
    $ cd dump1090  
    $ make

Run with: `./dump1090 --net`

### Python
    $ python -m venv .venv
    $ ./.venv/bin/activate
    $ pip install pygame pygame_ui gps haversine

### GPS
[Follow these directions](https://canadagps.ca/blogs/knowledgebase-by-platform-linux/how-to-connect-an-usb-gps-receiver-with-a-linux-computer)
    sudo apt install gpsd
    sudo gpsd -D 5 -N -n /dev/ttyACM0
    sudo apt install gpsd-clients  
Test with: `gpspipe -w -n 10 | grep -m 1 lon`

If lat/lon is 0, try: `sudo dpkg-reconfigure gpsd`

To make gpsd startup automatic update `/etc/default/gpsd` with:  
    `DEVICES=""`  
    `GPSD_OPTIONS="/dev/ttyACM0"`  
    `START_DAEMON="true"`  

Or [these](https://pypi.org/project/pyembedded/)
    
    pip install pyembedded
    sudo cat /dev/ttyACM0
