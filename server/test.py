from PIL import Image
import numpy as np

im = Image.open('./rawImages/test.png')
row,col = im.size
data=[] #r,g,b,i,j
pixels=im.load()
im = im.convert('1')
for i in range(row):
    col_data = []
    for j in range(col):
        col_data.append(pixels[i,j])
    data.append(col_data)

print(data)