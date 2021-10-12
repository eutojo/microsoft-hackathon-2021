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

        with Image.open('./rawImages/draft.png') as image:
            self.level1 = DataService.calculate_json(self, image)
        with Image.open('./rawImages/draft2.png') as image:
            self.level2 = DataService.calculate_json(self, image)
        with Image.open('./rawImages/test.png') as image:
            self.levelall = 

        print(self.floors)
        return True

    def get_floor(self, floor_id):
        if floor_id == 1:
            return self.level1
        elif floor_id == 2:
            return self.level2
        else:
            return self.levelall      
        
    def calculate_json(self, im):
        row,col = im.size
        data={} #r,g,b,i,j
        pixels=im.load()
        im = im.convert('1')
        for i in range(col):
            col_data = []
            for j in range(row):
                col_data.append(pixels[j,i])
            data[i] = col_data
        return jsonify(data)

    def get_building(self, building_id):
        return self.levels

