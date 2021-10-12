import sys
from PIL import Image
import numpy as np

im = Image.open(str(sys.argv[1]))
row,col = im.size
data={} #r,g,b,i,j
pixels=im.load()
im = im.convert('1')
for i in range(col):
    col_data = []
    for j in range(row):
        col_data.append(pixels[j,i])
    data[i] = col_data
print(data)
# f = open(str(sys.argv[2]),"w")
# f.write(str(data))
# f.close
