from flask import Flask
from DataService import DataService
import time

app = Flask(__name__)
data_service = DataService()
data_service.load_data()

@app.route("/")
def index():
    return "Hello World!"

@app.route("/floor/<int:id>")
def get_floor(id):
    print("SADDS")
    print(id)
    return data_service.get_floor(id)

@app.route("/building/<int:id>")
def get_building(id):
    return data_service.get_building(id)