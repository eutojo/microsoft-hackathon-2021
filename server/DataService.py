import json
from PIL import Image
import numpy as np
from flask import jsonify

sample_floor_fn = "./rawMap/sample_floor_metadata.json"
sample_ground_fn = "./rawMap/sample_floor_metadata.json"

class DataService:
    floors = None
    levels = None

    def __init__(self):
        pass

    def load_data(self):
        with open(sample_floor_fn, 'r') as file:
            self.floors = json.load(file)

        with open(sample_floor_fn, 'r',) as file:
            self.levels = json.load(file)

        with open("./rawImages/all.txt", "r") as file:
            self.levelall = eval(file.read())
        with open("./rawImages/level1.txt", "r") as file:
            self.level1 = eval(file.read())
        with open("./rawImages/level2.txt", "r") as file:
            self.level2 = eval(file.read())

        print(self.floors)
        return True

    def get_floor(self, floor_id):
        if floor_id == 1:
            return jsonify(self.level1)
        elif floor_id == 2:
            return jsonify(self.level2)
        else:
            return jsonify(self.levelall)     
        
    def get_building(self, building_id):
        return self.levels

