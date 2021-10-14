import json
from PIL import Image
import numpy as np
from lib.InstructionsFromPath import *
from lib.PathFind import *

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

def get_instructions(building_id, floor_id, current_user_location):
    img = cv2.imread('./floor_plan/0.png', 0)
    # plt.imshow(img, cmap = 'gray')
    # plt.show()
    scale_percent = 25 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    img_resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    # img = cv2.bitwise_not(img)
    img_resized[img_resized != 255] = 0
    img_resized[img_resized == 255] = 1
    x, y = img_resized.shape

    grid = make_grid(img_resized, x, y)
    # y cols
    # x rows

    # start_x = math.floor(user_loc[0]/2)
    # start_y = math.floor(user_loc[1]/2)

    # end_x = math.floor(room_loc[0]/2)
    # end_y = math.floor(room_loc[1]/2)
    # start = grid[start_x][start_y]
    # end = grid[end_x][end_y]
    
    start = grid[50][1] #100 #3
    end = grid[29][112] #59 #225 (50% SCALE)

    start.make_start()
    end.make_end()

    update_neighbors(grid)
    result_path = astar(lambda: draw(img_resized, grid), grid, start, end)
    # print(result_path)
    result_path = reverse_coordinates(result_path)
    instructions = create_instructions(result_path)
    instructions = scale_instructions(instructions,4)
    instructions = annotate_instructions(instructions)
    return instructions

    
