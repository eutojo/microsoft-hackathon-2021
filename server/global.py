from queue import PriorityQueue
import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys

class Pixel:
    def __init__(self, x, y, total_rows, total_cols):
        self.x = x
        self.y = y
        self.neighbors = []
        self.id = 1
        self.total_rows = total_rows
        self.total_cols = total_cols

    def get_pos(self):
        return self.x, self.y

    def is_closed(self):
        return self.id == 2

    def is_open(self):
        return self.id == 1

    def is_wall(self):
        return self.id == 0

    def is_start(self):
        return self.id == 9

    def is_end(self):
        return self.id == 8

    def is_path(self):
        return self.id == 5

    def reset(self):
        self.id = 1
    
    def make_closed(self):
        self.id = 2

    def make_open(self):
        self.id = 1
    
    # def make_wall(self):
    #     self.id = "WALL"
    
    def make_start(self):
        self.id = 9

    def make_end(self):
        self.id = 8

    def make_path(self):
        self.id = 5

    def make_variable(self, in_id):
        self.id = in_id
    
    def draw(self, img_arr):
        #front-end function
        #set coordinate to path id       
        img_arr[self.x][self.y] = self.id


    def update_neighbors(self, grid):
        self.neighbors = []
        if self.x < self.total_rows - 1 and not grid[self.x + 1][self.y].is_closed(): #DOWN
            self.neighbors.append(grid[self.x + 1][self.y])

        if self.x > 0 and not grid[self.x - 1][self.y].is_closed(): #UP
            self.neighbors.append(grid[self.x - 1][self.y])

        if self.y < self.total_cols - 1 and not grid[self.x][self.y + 1].is_closed(): #RIGHT
            self.neighbors.append(grid[self.x][self.y + 1])

        if self.y > 0 and not grid[self.x][self.y - 1].is_closed(): #LEFT
            self.neighbors.append(grid[self.x][self.y - 1])

    def get_direction():
        #maybe
        pass

    def __lt__(self, other):
        return False

def hero(p1, p2):
    #p1 = (x, y)
    x1, y1 = p1
    x2, y2 = p2
    #mannhatten distance
    return abs(x1 - x2) + abs(y1 - y2)

def make_grid(img_arr, x, y):
    #convert image from image array to array of 'Pixels'
    # gap = width // rows #give gap between rows
    grid = []
    for i in range(x):
        grid.append([])
        for j in range(y):
            pixel = Pixel(i, j, x, y)
            pixel.make_variable(img_arr[i][j])
            grid[i].append(pixel)

    return grid

"""
Backtracking need to keep track of turns and distance
back_track_arr = []
back_track_arr.append(['direction', 'distance to this turn/aka. how many pixels its backtracked'])
turn left: ETA/distance left
turn back_track_arr[1][0] == 'direction': back_track_arr[1][1] == 'distance'
"""

def reconstruct_path(came_from, current, draw):
    tmp_list = []
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()
        tmp_list.append(current)
        print(tmp_list)

def astar(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {pixel: float("inf") for row in grid for pixel in row}
    g_score[start] = 0
    
    f_score = {pixel: float("inf") for row in grid for pixel in row}
    f_score[start] = hero(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            #make path/backtrack
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + hero(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    
    return None

def draw(img_arr, grid):
    for row in grid:
        for pixel in row:
            pixel.draw(img_arr)


#   return img_arr thats updated
def update_neighbors(grid):
    for row in grid:
        for pixel in row:
            pixel.update_neighbors(grid)



if __name__ == "__main__":
    id_2_var = {
        1 : "OPEN",
        0 : "WALLS",
        2 : "CLOSED",
        9 : "START",
        8 : "END",
        5 : "PATH"
    }

    var_2_id = {
        "OPEN" : 1,
        "WALLS" : 0,
        "CLOSED" : 2,
        "START" : 9,
        "END" : 8,
        "PATH" : 5
    }
    img = cv2.imread('/mnt/d/ms_hack_2021/microsoft-hackathon-2021/server/floor_plan/test_img.png', 0)
    # plt.imshow(img, cmap = 'gray')
    # plt.show()
    
    # img = cv2.bitwise_not(img)
    img[img == 255] = 1
    plt.imshow(img, cmap = 'gray')
    plt.show()
    x, y = img.shape

    # y cols
    # x rows

    img_cpy = img
    grid = make_grid(img, x, y)
    start = grid[1][20]
    end = grid[23][35]
    start.make_start
    end.make_end

    update_neighbors(grid)
    astar(lambda: draw(img_cpy, grid), grid, start, end)

    np.set_printoptions(threshold=sys.maxsize)
    print(img_cpy)