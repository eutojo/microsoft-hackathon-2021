from queue import PriorityQueue


class Pixel:
    def __init__(self, row, col, width, total_rows, total_cols):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.neighbors = []
        self.id = 1
        self.width = width
        self.total_rows = total_rows
        self.total_cols = total_cols

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.id == 0

    def is_open(self):
        return self.id == 1

    def is_variable(self):
        #check what variable it is
        pass

    def is_end(self):
        return self.id == -1

    def draw(self, img_arr):
        #front-end function
        #set coordinate to path id       
        pass

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_closed(): #DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_closed(): #UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_closed(): #RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_closed(): #LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

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

def make_grid(rows, cols, width):
    #convert image from image array to array of 'Pixels'
    grid = []
    gap = width // rows #give gap between rows
    for i in range(cols):
        grid.append([])
        for j in range(rows):
            pixel = Pixel(i, j, gap, rows, cols)
            grid[i].append(pixel)
    return grid

"""
Backtracking need to keep track of turns and distance
back_track_arr = []
back_track_arr.append(['direction', 'distance to this turn/aka. how many pixels its backtracked'])
turn left: ETA/distance left
turn back_track_arr[1][0] == 'direction': back_track_arr[1][1] == 'distance'
"""

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
            #make path
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

# def draw(img_arr, grid, rows, width):
#     win.fill(WHITE)

#     for row in grid:
#         for pixel in row:
#             pixel.draw(id)

#     draw_grid(win, rows, width)
#     pygame.display.update()

#   return img_arr thats updated

