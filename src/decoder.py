import os
import json
import time
import gps

current_aircraft = []


def get_data_directory_path():
    """Return the path of the data directory"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, '../data')

def clean_up_directory():
    """Cleans up the JSON directory"""
    for file_name in os.listdir(get_data_directory_path()):
        if file_name.startswith('history_'):
            os.remove(os.path.join(get_data_directory_path(), file_name))

def get_aircraft():
    """Retrieving aircraft from dump1090 json output"""
    clean_up_directory()
    print('getting aircraft at {}'.format(str(int(time.time()))))
    json_path = os.path.join(get_data_directory_path(), 'aircraft.json')
    with open(json_path) as file:
        aircraft_json = json.loads(file.read())
    print('{} found'.format(len(aircraft_json['aircraft'])))
    return aircraft_json['aircraft']

def get_aircraft_type(icao_hex):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    json_dir_path = os.path.join(dir_path, '../../dump1090/public_html/db')
    return request_from_db(icao_hex, 1, json_dir_path)
    
def request_from_db(icao, level, path):
    icao = icao.upper()
    bkey = icao[:level]
    dkey = icao[level:]
    json_path = os.path.join(path, bkey + '.json')

    with open(json_path) as file:
        type_json = json.loads(file.read())
    if dkey in type_json:
        return type_json[dkey].get('t')
    elif "children" in type_json:
        subkey = bkey + dkey[:1]
        if subkey in type_json['children']:
            return request_from_db(icao, level + 1, path)
        return "Unk"
    return "Unk"

def get_lat_lon():
    # Listen on port 2947 (gpsd) of localhost
    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    lat = None
    lon = None

    while lat == None and lon == None:
        try:
            report = session.next()
            # Wait for a 'TPV' report and display the current time
            # To see all report data, uncomment the line below
            # print(report)
            if report['class'] == 'TPV':
                if hasattr(report, 'lat') and hasattr(report, 'lon'):
                    print(str(report.lat) + " " + str(report.lon))
                    lat = round(report.lat, 4)
                    lon = round(report.lon, 4)
                    print(str(lat) + " " + str(lon))
                    session = None
                    return lat, lon
        except KeyError:
            pass
        except KeyboardInterrupt:
            quit()
        except StopIteration:
            session = None
            print("GPSD has terminated")
