import json
from PIL import Image
import numpy as np
from flask import jsonify
from bs4 import BeautifulSoup

sample_floor_fn = "./rawMap/sample_floor_metadata.json"
sample_ground_fn = "./rawMap/sample_floor_metadata.json"
sample_foundry = "./rawMap/building_data/foundry_data/FDY-L1.json"

IMAGE_PATH = "./rawImages/foundry_data/"
SVG = ".svg"

def scrapeSVG(image):
    with open(image) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    svg = soup.find_all('svg')
    for item in svg:
        viewbox = item['viewbox']

    rect = soup.find_all('rect')
    floors = []

    for item in rect:
        if (item["fill"] == "#ffffff"):
            className = "blank"
        elif (item["fill"] == "#f5f5f5"):
            className = "booked"
        else:
            className = "free"

        floors.append({
            "type":"rect",
            "x": item["x"],
            "y": item["y"],
            "width": item["width"],
            "height": item["height"],
            "stroke": item["stroke"],
            "className": className
        })
    
    return {"floors": floors, "viewbox": viewbox}

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
        floors = scrapeSVG(IMAGE_PATH + str(floor_id) + SVG)

        with open(sample_foundry, 'r') as file:
            data = json.load(file)

        data.update(floors)
        
        return jsonify(data)     
        
    def get_building(self, building_id):
        return self.levels

