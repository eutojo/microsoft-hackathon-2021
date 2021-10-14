import json
from PIL import Image
import numpy as np
from flask import jsonify

buildings_json = "./rawMap/building_data/buildings.json"

def get_buildings():
    with open(buildings_json, "r") as file:
        buildings = json.load(file)
    return buildings

def get_building_by_id(id):
    buildings = get_buildings()
    file_location = buildings[id]["file_location"]
    return file_location

def get_building_info_by_id(building_id):
    
    building_floors = get_building_floors(building_id)
    building_rooms = get_building_rooms_by_floors(building_floors)

    data = {
        "floors": building_floors,
        "rooms": building_rooms
    }
    return data

def get_building_floors(building_id):
    building_file = get_building_by_id(building_id)
    with open(building_file, "r") as file:
        building_data = json.load(file)
    building_floor_data = building_data["floor"]
    return building_floor_data

def get_building_rooms_by_floors(building_floor_data):
    building_room_data = []
    for floor in building_floor_data:
        if floor["file_location"] != "":
            with open(floor["file_location"],"r") as file:
                room_data = json.load(file)
            building_room_data.extend(room_data["room"])
    return building_room_data

def get_floor_info_by_id(building_id, floor_id):
    building_floors = get_building_floors(building_id)
    for building_floor in building_floors:
        if building_floor["floor_id"] == floor_id:
            floor_file = building_floor["file_location"]

    with open(floor_file, "r") as file:
        floor = json.load(file)
    
    data = {
        "floor_data": floor
    }

    return data

def get_instructions():
    return [{"distance":32,"draw_end_x":4,"draw_end_y":200,"draw_start_x":4,"draw_start_y":172,"end_x":4,"end_y":172,"instruction":"RIGHT","start_x":4,"start_y":200},{"distance":172,"draw_end_x":172,"draw_end_y":172,"draw_start_x":4,"draw_start_y":172,"end_x":172,"end_y":172,"instruction":"LEFT","start_x":4,"start_y":172},{"distance":60,"draw_end_x":172,"draw_end_y":172,"draw_start_x":172,"draw_start_y":116,"end_x":172,"end_y":116,"instruction":"RIGHT","start_x":172,"start_y":172},{"distance":76,"draw_end_x":244,"draw_end_y":116,"draw_start_x":172,"draw_start_y":116,"end_x":244,"end_y":116,"instruction":"LEFT","start_x":172,"start_y":116},{"distance":4,"draw_end_x":244,"draw_end_y":116,"draw_start_x":244,"draw_start_y":116,"end_x":244,"end_y":116,"instruction":"RIGHT","start_x":244,"start_y":116},{"distance":208,"draw_end_x":448,"draw_end_y":112,"draw_start_x":244,"draw_start_y":116,"end_x":448,"end_y":112,"instruction":"RIGHT","start_x":244,"start_y":116},{"distance":4,"draw_end_x":448,"draw_end_y":112,"draw_start_x":448,"draw_start_y":112,"end_x":448,"end_y":112,"instruction":"CONTINUE","start_x":448,"start_y":112}]
