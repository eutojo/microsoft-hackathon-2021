
# for coord in cw_spral[1:]:
def create_instructions(path):
    # Instruction list
    instructions = []

    # Figure out initial direction
    current_dir = ''
    distance = 1

    # Length of 1 and 2 edge cases
    x1, y1 = path[0]
    x2, y2, = path[1]

    start_x = x1
    start_y = y1

    x_diff = x2 - x1
    y_diff = y2 - y1

    # Determine if moving on x or y plane
    if x_diff != 0:
        current_dir = 'x'
    elif y_diff != 0:
        current_dir = 'y'
    
    start_coord = path[0]
    current_coord = path[1]
    prev_coord = None

    # Assumption: direction changes cannot be diagonal
    for coord in path[2:]:
        x1, y1 = current_coord
        x2, y2 = coord

        x_diff = x2 - x1
        y_diff = y2 - y1

        if x_diff != 0:
            new_dir = 'x'
        elif y_diff != 0:
            new_dir = 'y'
        
        # print(current_coord, coord, prev_coord, "x-diff", x_diff, "y_diff", y_diff, "new_dir", new_dir)
        if new_dir != current_dir:
            # Change of direction
            # From x to y
            if new_dir == 'y':
                # Still need to look at X predecessor
                if prev_coord[0] < coord[0]:
                    if y_diff < 0:
                        instruction = "LEFT"
                    else:
                        instruction = "RIGHT"
                else:
                    if y_diff < 0:
                        instruction = "RIGHT"
                    else:
                        instruction = "LEFT"
                current_dir = 'y'
                # print(instruction)
                new_instruction = create_instruction(start_coord, current_coord, instruction)
                instructions.append(new_instruction)
                start_coord = current_coord

            # From y to x
            else:
                if prev_coord[1] < coord[1]:
                    # (5,6), (6,7)
                    if x_diff < 0:
                        instruction = "RIGHT"
                    else:
                        instruction = "LEFT"
                else:
                    if x_diff < 0:
                        instruction = "LEFT"
                    else:
                        instruction = "RIGHT"
                current_dir = 'x'
                # print(instruction)
                new_instruction = create_instruction(start_coord, current_coord, instruction)
                instructions.append(new_instruction)
                start_coord = current_coord
        else:
            prev_coord = current_coord
            current_coord = coord

    new_instruction = create_instruction(start_coord, current_coord, "CONTINUE")
    instructions.append(new_instruction)    
    return instructions

# Consider last one

def create_instruction(start_coord, end_coord, instruction):
    x1, y1 = start_coord
    x2, y2 = end_coord

    distance = max(abs(x2-x1), abs(y2-y1) ) + 1
    return {
        "start_x" : x1,
        "start_y" : y1,
        "end_x" : x2,
        "end_y" : y2,
        "distance" : distance,
        "instruction" : instruction
    }

def scale_instruction(instruction, scale_factor):
    return {
        "start_x" : instruction["start_x"]*scale_factor,
        "start_y" : instruction["start_y"]*scale_factor,
        "end_x" : instruction["end_x"]*scale_factor,
        "end_y" : instruction["end_y"]*scale_factor,
        "distance" : instruction["distance"]*scale_factor,
        "instruction" : instruction["instruction"]
    }

def scale_instructions(instructions, scale_factor):
    new_instructions = []
    for i in instructions:
        new_instructions.append(scale_instruction(i,scale_factor))
    return new_instructions

def reverse_coordinates(instructions):
    coords = []
    for i in instructions:
        y, x = i
        coords.append((x,y))
    return coords

def annotate_draw_path(instruction):
    x1, y1 = instruction["start_x"], instruction["start_y"]
    x2, y2 = instruction["end_x"], instruction["end_y"]

    # Vertical line
    if x1 == x2:
        if y1 > y2:
            temp = y2
            y2 = y1
            y1 = temp 

            temp = x2
            x2 = x1
            x1 = temp

    # Horizontal line
    elif y2 == y1:
        if x1 > x2:
            temp = y2
            y2 = y1
            y1 = temp 

            temp = x2
            x2 = x1
            x1 = temp

    return {
        "start_x" : instruction["start_x"],
        "start_y" : instruction["start_y"],
        "end_x" : instruction["end_x"],
        "end_y" : instruction["end_y"],
        "draw_start_x" : x1,
        "draw_start_y" : y1,
        "draw_end_x" : x2,
        "draw_end_y" : y2,
        "distance" : instruction["distance"],
        "instruction" : instruction["instruction"]
    }

def annotate_instructions(instructions):
    new_instructions = []
    for i in instructions:
        new_instructions.append(annotate_draw_path(i))
    return new_instructions

if __name__ == "__main__":
    # test cases
    ## always turn right
    cw_spiral = [(1,1),(2,1),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(4,9),(3,9),(2,9),(2,8),(2,7),(2,6),(2,5),(2,4)]
    ## always turn left
    acw_spiral = [(10,1),(9,1),(8,1),(7,1),(6,1),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(6,7),(7,7),(8,7),(9,7),(9,6),(9,5),(9,4),(9,3)]
    both_turns = [(10,1),(9,1),(8,1),(7,1),(7,2),(7,3),(7,4),(6,4),(5,4),(5,3),(5,2),(5,1),(4,1),(3,1),(2,1)]

    test = [(100, 3), (99, 3), (98, 3), (97, 3), (96, 3), (95, 3), (94, 3), (93, 3), (92, 3), (91, 3), (90, 3), (89, 3), (88, 3), (87, 3), (86, 3), (86, 4), (86, 5), (86, 6), (86, 7), (86, 8), (86, 9), (86, 10), (86, 11), (86, 12), (86, 13), (86, 14), (86, 15), (86, 16), (86, 17), (86, 18), (86, 19), (86, 20), (86, 21), (86, 22), (86, 23), (86, 24), (86, 25), (86, 26), (86, 27), (86, 28), (86, 29), (86, 30), (86, 31), (86, 32), (86, 33), (86, 34), (86, 35), (86, 36), (86, 37), (86, 38), (86, 39), (86, 40), (86, 41), (86, 42), (86, 43), (86, 44), (86, 45), (86, 46), (86, 47), (86, 48), (86, 49), (86, 50), (86, 51), (86, 52), (86, 53), (86, 54), (86, 55), (86, 56), (86, 57), (86, 58), (86, 59), (86, 60), (86, 61), (86, 62), (86, 63), (86, 64), (86, 65), (86, 66), (86, 67), (86, 68), (86, 69), (86, 70), (86, 71), (86, 72), (86, 73), (86, 74), (86, 75), (86, 76), (86, 77), (86, 78), (86, 79), (86, 80), (86, 81), (86, 82), (86, 83), (86, 84), (86, 85), (86, 86), (85, 86), (84, 86), (83, 86), (82, 86), (81, 86), (80, 86), (79, 86), (78, 86), (77, 86), (76, 86), (75, 86), (74, 86), (73, 86), (72, 86), (71, 86), (70, 86), (69, 86), (68, 86), (67, 86), (66, 86), (65, 86), (64, 86), (63, 86), (62, 86), (61, 86), (60, 86), (59, 86), (59, 87), (59, 88), (59, 89), (59, 90), (59, 91), (59, 92), (59, 93), (59, 94), (59, 95), (59, 96), (59, 97), (59, 98), (59, 99), (59, 100), (59, 101), (59, 102), (59, 103), (59, 104), (59, 105), (59, 106), (59, 107), (59, 108), (59, 109), (59, 110), (59, 111), (59, 112), (59, 113), (59, 114), (59, 115), (59, 116), (59, 117), (59, 118), (59, 119), (59, 120), (59, 121), (59, 122), (59, 123), (58, 123), (58, 124), (58, 125), (58, 126), (58, 127), (58, 128), (58, 129), (58, 130), (58, 131), (58, 132), (58, 133), (58, 134), (58, 135), (58, 136), (58, 137), (58, 138), (58, 139), (58, 140), (58, 141), (58, 142), (58, 143), (58, 144), (58, 145), (58, 146), (58, 147), (58, 148), (58, 149), (58, 150), (58, 151), (58, 152), (58, 153), (58, 154), (58, 155), (58, 156), (58, 157), (58, 158), (58, 159), (58, 160), (58, 161), (58, 162), (58, 163), (58, 164), (58, 165), (58, 166), (58, 167), (58, 168), (58, 169), (58, 170), (58, 171), (58, 172), (58, 173), (58, 174), (58, 175), (58, 176), (58, 177), (58, 178), (58, 179), (58, 180), (58, 181), (58, 182), (58, 183), (58, 184), (58, 185), (58, 186), (58, 187), (58, 188), (58, 189), (58, 190), (58, 191), (58, 192), (58, 193), (58, 194), (58, 195), (58, 196), (58, 197), (58, 198), (58, 199), (58, 200), (58, 201), (58, 202), (58, 203), (58, 204), (58, 205), (58, 206), (58, 207), (58, 208), (58, 209), (58, 210), (58, 211), (58, 212), (58, 213), (58, 214), (58, 215), (58, 216), (58, 217), (58, 218), (58, 219), (58, 220), (58, 221), (58, 222), (58, 223), (58, 224), (58, 225), (59, 225)]
    # print(create_instructions(cw_spiral))
    # print(create_instructions(acw_spiral))
    path = [(50, 1), (49, 1), (48, 1), (47, 1), (46, 1), (45, 1), (44, 1), (43, 1), (43, 2), (43, 3), (43, 4), (43, 5), (43, 6), (43, 7), (43, 8), (43, 9), (43, 10), (43, 11), (43, 12), (43, 13), (43, 14), (43, 15), (43, 16), (43, 17), (43, 18), (43, 19), (43, 20), (43, 21), (43, 22), (43, 23), (43, 24), (43, 25), (43, 26), (43, 27), (43, 28), (43, 29), (43, 30), (43, 31), (43, 32), (43, 33), (43, 34), (43, 35), (43, 36), (43, 37), (43, 38), (43, 39), (43, 40), (43, 41), (43, 42), (43, 43), (42, 43), (41, 43), (40, 43), (39, 43), (38, 43), (37, 43), (36, 43), (35, 43), (34, 43), (33, 43), (32, 43), (31, 43), (30, 43), (29, 43), (29, 44), (29, 45), (29, 46), (29, 47), (29, 48), (29, 49), (29, 50), (29, 51), (29, 52), (29, 53), (29, 54), (29, 55), (29, 56), (29, 57), (29, 58), (29, 59), (29, 60), (29, 61), (28, 61), (28, 62), (28, 63), (28, 64), (28, 65), (28, 66), (28, 67), (28, 68), (28, 69), (28, 70), (28, 71), (28, 72), (28, 73), (28, 74), (28, 75), (28, 76), (28, 77), (28, 78), (28, 79), (28, 80), (28, 81), (28, 82), (28, 83), (28, 84), (28, 85), (28, 86), (28, 87), (28, 88), (28, 89), (28, 90), (28, 91), (28, 92), (28, 93), (28, 94), (28, 95), (28, 96), (28, 97), (28, 98), (28, 99), (28, 100), (28, 101), (28, 102), (28, 103), (28, 104), (28, 105), (28, 106), (28, 107), (28, 108), (28, 109), (28, 110), (28, 111), (28, 112), (29, 112)]
    instructions = create_instructions(path)
    instructions = scale_instructions(instructions,4)
    instructions = annotate_instructions(instructions)
    print(instructions)
