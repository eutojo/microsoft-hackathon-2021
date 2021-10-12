import sys
from PIL import Image
import numpy as np
from flask import jsonify


row,col = im.size
data={} #r,g,b,i,j
pixels=im.load()
im = im.convert('1')
for i in range(col):
    col_data = []
    for j in range(row):
        col_data.append(pixels[j,i])
    data[i] = col_data
        
