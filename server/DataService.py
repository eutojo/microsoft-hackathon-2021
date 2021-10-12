import json

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
        return self.floors

    def get_building(self, building_id):
        return self.levels

