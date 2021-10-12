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

        print(self.floors)
        return True

    def get_floor(self, floor_id):
        im = Image.open('./rawImages/test.png')
        row,col = im.size
        data={} #r,g,b,i,j
        pixels=im.load()
        im = im.convert('1')
        for i in range(row):
            col_data = []
            for j in range(col):
                col_data.append(pixels[i,j])
            data[i] = col_data
        return jsonify(data)

    def get_building(self, building_id):
        return self.levels

