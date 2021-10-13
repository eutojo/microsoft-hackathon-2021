from bs4 import BeautifulSoup
import json

IMAGE_PATH = "../rawImages/foundry_data/"
SVG = ".svg"

def scrapeSVG(image, id):
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

    data = {"floors": floors, "viewbox": viewbox}

    with open('FDY-L' + str(id) + '.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)


for i in range(4):
    scrapeSVG(IMAGE_PATH + str(i) + SVG, i)