directions = [
    "NORTHWEST",
    "NORTH",
    "NORTHEAST",
    "WEST",
    "EAST",
    "SOUTHWEST",
    "SOUTH",
    "SOUTHEAST"
]

def next_location(direction, row, col):
    if direction == "NORTHWEST":
        return row-1, col-1
    if direction == "NORTH":
        return row-1, col
    if direction == "NORTHEAST":
        return row-1, col+1
    if direction == "WEST":
        return row, col-1
    if direction == "EAST":
        return row, col+1
    if direction == "SOUTHWEST":
        return row+1, col-1
    if direction == "SOUTH":
        return row+1, col
    if direction == "SOUTHEAST":
        return row+1, col+1
    
    return -1, -1
    

def xmas(table, row, col, next_letter, direction=None):
    if row < 0 or row >= len(table):
        return 0
    
    if col < 0 or col >= len(table[row]):
        return 0
    
    current = table[row][col]

    if current != next_letter:
        return 0

    if current == "S":
        return 1
    
    count = 0
    if current == "X":
        for d in directions:
            next_row, next_col = next_location(d, row, col)
            count += xmas(table, next_row, next_col, "M", d)
    else:
        next_row, next_col = next_location(direction, row, col)
        count += xmas(table, next_row, next_col, "A" if current == "M" else "S", direction)

    return count

with open("input.txt") as f:
    table = f.read().splitlines()

count = 0
for row in range(len(table)):
    for col in range(len(table[row])):
       count += xmas(table, row, col, "X")

print(count)