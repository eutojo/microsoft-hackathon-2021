
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
        
        print(current_coord, coord, prev_coord, "x-diff", x_diff, "y_diff", y_diff, "new_dir", new_dir)
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
                print(instruction)
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
                print(instruction)
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

if __name__ == "__main__":
    # test cases
    ## always turn right
    cw_spiral = [(1,1),(2,1),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(4,9),(3,9),(2,9),(2,8),(2,7),(2,6),(2,5),(2,4)]
    ## always turn left
    acw_spiral = [(10,1),(9,1),(8,1),(7,1),(6,1),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(6,7),(7,7),(8,7),(9,7),(9,6),(9,5),(9,4),(9,3)]
    both_turns = [(10,1),(9,1),(8,1),(7,1),(7,2),(7,3),(7,4),(6,4),(5,4),(5,3),(5,2),(5,1),(4,1),(3,1),(2,1)]
    # print(create_instructions(cw_spiral))
    # print(create_instructions(acw_spiral))
    print(create_instructions(both_turns))
