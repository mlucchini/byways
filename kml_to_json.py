from geo2kml import to_kml

import glob
import json
import os


source_directory = 'geojson'
destination_directory = 'kml'
valid_paths = os.path.join(source_directory, '*.json')

try:
    for source_path in glob.glob(valid_paths):
        source_filename = os.path.basename(source_path)
        destination_path = os.path.join(destination_directory, source_filename + '.kml')

        with open(source_path) as json_file:
            data = json.load(json_file)
            kml = to_kml(data)

            with open(destination_path, 'w') as file:
                file.write(kml)
                print('Success: ' + source_path + ' --> ' + destination_path)
except Exception as e:
    print('Error: ' + source_path + ' --> ' + destination_path)
    print(e)
