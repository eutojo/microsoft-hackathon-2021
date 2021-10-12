# from PIL import Image
# import numpy as np

# def jpg_image_to_array(image_path):
#   """
#   Loads JPEG image into 3D Numpy array of shape 
#   (width, height, channels)
#   """
#   with Image.open(image_path) as image:         
#     im_arr = np.fromstring(image.tobytes(), dtype=np.uint8)
#     im_arr = im_arr.reshape((image.size[1], image.size[0], 3))                                   
#   return im_arr

# im = jpg_image_to_array("grd_floor_notext.jpg")
# print(im)
# print("what")

from PIL import Image
import numpy as np

def help(input):
  if (input[0] + input[1] + input[2]) >= 384:
    return 1
  else:
    return 0

def generate_matrix(x,y):
  matrix = []
  for i in range(y):
    row_list = []
    for j in range(x):
      row_list.append(0)
    
    matrix.append(row_list)
  return matrix
      
# start_node = (x,y) = 1,1 
def bfs(image_array, start_node, row_size, col_size):
  queue = []
  visited = generate_matrix(row_size, col_size)
  queue.append(start_node)

  while queue:
    current_node = queue.pop(0)
    
    x = current_node[0]
    y = current_node[1]

    print(x,y)
    visited[y][x]=1

    # Look at its neighbours
    # Out of bounds check
    
    # Look up
    if (x >= 0) and (x < row_size) and (y-1 > 0) and (y-1 < col_size):
      # free space is 1, and not visited is 0
      if image_array[y-1][x] == 1 and visited[y-1][x] != 1:
        queue.append((x,y-1))

    print(x,y)
    # Look down
    if (x >= 0) and (x < row_size) and (y+1 > 0) and (y+1 < col_size):
      # free space is 1, and not visited is 0
      if image_array[y+1][x] == 1 and visited[y+1][x] != 1:
          queue.append((x,y+1))

    # Look left
    if (x-1 >= 0) and (x-1 < row_size) and (y > 0) and (y < col_size):
      # free space is 1, and not visited is 0
      if image_array[y][x-1] == 1 and visited[y][x-1] != 1:
        queue.append((x-1,y))

    # Look Right
    if (x+1 >= 0) and (x+1 < row_size) and (y > 0) and (y < col_size):
      # free space is 1, and not visited is 0
      if image_array[y][x+1] == 1 and visited[y][x+1] != 1:
        queue.append((x+1,y))

  return visited


im = Image.open('./image.png')
row,col = im.size
print(row,col)
data=[] #r,g,b,i,j
pixels=im.load()
im = im.convert('1')
for i in range(col):
    col_data = []
    for j in range(row):
        col_data.append(help(pixels[j,i]))
    data.append(col_data)

print(bfs(data, (1,1), row, col))

# # print(data)
# print(row,col)
# bfs(data, visited, (1,1), row, col)
# print(len(set(visited)))

print(bfs(data, (1,1), row, col))
# print("\n\n")
# print(data)

