## @file: json_manager.py
#

import json

class JSON_Manager:
    def __init__(self):
        pass
    def write(self, data_2_write, filename='calibrate.json'):
        json_file = open(filename,'w')
        json.dump(data_2_write,json_file,indent=4)
        json_file.close()
    def read(self, filename='calibrate.json'):
        json_file = open(filename,'r')
        json_data = json.load(json_file)
        json_file.close()
        return json_data
