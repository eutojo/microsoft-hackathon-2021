import cv2
import matplotlib.pyplot as plt
import numpy as np

class RoomFinder:
    room_list = []
    path = None
    col_size = 0
    row_size = 0

    def __init__(self) -> None:
        pass

    def get_rooms(self, filename, path_coord):
        # Clear room list
        self.room_list = []

        img = self.load_image(filename)

        # Remove Path
        # self.display_image(img)
    
        # This is the path
        self.col_size, self.row_size = img.shape
        img_searched = self.bfs(img, path_coord, self.row_size, self.col_size)
        self.path = img_searched

        # Render new image without path      
        img = np.multiply(img, img_searched)

        # loop through all bfs
        for y in range(self.col_size):
            for x in range(self.row_size):
                if img[y][x] == 1:
                    img_searched = self.bfs(img, (x,y), self.row_size, self.col_size)
                    img = np.multiply(img, img_searched)
                    self.room_list.append(img_searched)

        return

    def load_image(self, filename):
        # Import image - 0 for greyscale mode
        img = cv2.imread(filename, 0)
        print(img)
        self.display_image(img)

        # Image processing
        # img[img == 255] = 1
        # walls are 102
        img[img == 102] = 0
        img[img != 0] = 1
        self.display_image(img)
        

        # white space
        return img

    def convert_to_coordinates(self, matrix):
        pass

    def display_rooms(self):
        for index,r in enumerate(self.room_list):
            print("----ROOM----", index)
            print("\n",r)
            self.display_image(r)
            

    def display_image(self, img):
        plt.imshow(img, cmap = 'gray')
        plt.show()

    # start_node = (x,y) = 1,1 
    def bfs(self, image_array, start_node, row_size, col_size):
        queue = []
        visited = self.generate_matrix(row_size, col_size)
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
        return np.array(visited)

    def generate_matrix(self, x, y):
        matrix = []
        for i in range(y):
            row_list = []
            for j in range(x):
                row_list.append(1)
            
            matrix.append(row_list)
        return matrix

    # Assumption all rooms are rectangle
    def _generate_room_details(self, id, img):
        first_x = None
        first_y = None
        last_x = None
        last_y = None
      
        for y in range(self.col_size):
            for x in range(self.row_size):
                # This is part of the room
                if img[y][x] == 0:
                    if first_x is None:
                        first_x = x
                        first_y = y
                        last_x = x
                        last_y = y
                    else:
                        if y > last_y:
                            last_y = y
                        if x > last_x:
                            last_x = x
                            
        print(self.row_size, self.col_size)
        print(first_x, first_y)
        print(last_x, last_y)

        return_val = {
            "id": id,
            "x": first_x-1,
            "y": first_y-1,
            "height": last_y - first_y + 2,
            "width": last_x - first_x + 2,
        }
        return return_val

    def get_room_json(self):
        return_list = []
        for id, r in enumerate(self.room_list):
            print(r)
            return_list.append(self._generate_room_details(id,r))
        return return_list
                    
    def get_path(self) -> np.array:
        return self.path

# Test code
if __name__ == "__main__":
    filename = './floor_plan/1.png'
    x = 1
    y = 1

    # THIS IS ANY COORDINATE THAT IS THE PATH AND NOT ROOMS, you need to include this
    coordinates = (x,y)
    
    rf = RoomFinder()
    rf.get_rooms(filename=filename, path_coord=coordinates)
    # rf.display_rooms()

    # print("----PATH----", rf.get_path())
    print(rf.get_room_json())
