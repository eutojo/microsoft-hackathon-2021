from flask import Flask, jsonify
import DataService
import time

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/buildings/get")
def get_buildings():
    data = DataService.get_buildings()
    return jsonify(data)

@app.route("/buildings/get/<building_id>")
def get_building_by_id(building_id):
    data = DataService.get_building_info_by_id(building_id)
    return jsonify(data)

@app.route("/buildings/get/<building_id>/<floor_id>")
def get_floor_info_by_id(building_id, floor_id):
    data = DataService.get_floor_info_by_id(building_id, floor_id)
    return jsonify(data)

@app.route("/instructions/get")
def get_instructions():
    data = DataService.get_instructions()
    return jsonify(data)

