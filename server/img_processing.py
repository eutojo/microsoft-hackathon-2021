import numpy as np
import cv2
import matplotlib.pyplot as plt



# def help(input):
#   if (input[0] + input[1] + input[2]) >= 384:
#     return 1
#   else:
#     return 0

def generate_matrix(x,y):
  matrix = []
  for i in range(y):
    row_list = []
    for j in range(x):
      row_list.append(1)
    
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

    if visited[y][x]==0:
      continue
    else:
        visited[y][x] = 0

        # Look at its neighbours
        # Out of bounds check

        # Look up
        if (x >= 0) and (x < row_size) and (y-1 > 0) and (y-1 < col_size):
            # free space is 1, and not visited is 0
            if image_array[y-1][x] == 1 and visited[y-1][x] != 0:
                queue.append((x,y-1))

        # Look down
        if (x >= 0) and (x < row_size) and (y+1 > 0) and (y+1 < col_size):
            # free space is 1, and not visited is 0
            if image_array[y+1][x] == 1 and visited[y+1][x] != 0:
                queue.append((x,y+1))

        # Look left
        if (x-1 >= 0) and (x-1 < row_size) and (y > 0) and (y < col_size):
            # free space is 1, and not visited is 0
            if image_array[y][x-1] == 1 and visited[y][x-1] != 0:
                queue.append((x-1,y))

        # Look Right
        if (x+1 >= 0) and (x+1 < row_size) and (y > 0) and (y < col_size):
            # free space is 1, and not visited is 0
            if image_array[y][x+1] == 1 and visited[y][x+1] != 0:
                queue.append((x+1,y))

  return visited

if __name__ == "__main__":
    img = cv2.imread('./floor_plan/test_img.png', 0)
    # plt.imshow(img, cmap = 'gray')
    # plt.show()
    
    # img = cv2.bitwise_not(img)
    img[img == 255] = 1
    plt.imshow(img, cmap = 'gray')
    plt.show()

    # room_dict = {}

    col_size, row_size = img.shape
    img_searched = bfs(img, (2, 30), row_size, col_size)
    # room_dict.update({1: img_searched})
    
    plt.imshow(img_searched, cmap = 'gray')
    plt.show()

    
    sum_img = img + img_searched
    # img_searched = bfs(sum_img, (23, 3), row_size, col_size)
    plt.imshow(sum_img, cmap = 'gray')
    plt.show()