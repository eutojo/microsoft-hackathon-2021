import json
from PIL import Image
import numpy as np
from flask import jsonify

sample_floor_fn = "./rawMap/sample_floor_metadata.json"
sample_ground_fn = "./rawMap/sample_floor_metadata.json"
sample_foundry = "./rawMap/building_data/foundry_data/FDY-L1.json"
BUILDING_DATA_PATH = "./rawMap/building_data/foundry_data/FDY-L"
JSON = ".json"

class DataService:
    floors = None
    levels = None

    def __init__(self):
        pass

    def load_data(self):
        with open(sample_foundry, 'r') as file:
            self.floors = json.load(file)

        with open(sample_floor_fn, 'r',) as file:
            self.levels = json.load(file)

        return True

    def get_floor(self, floor_id):
        with open(BUILDING_DATA_PATH + str(floor_id) + JSON, 'r') as file:
            data = json.load(file)
        
        return data 
        
    def get_building(self, building_id):
        return self.levels

    
    

