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

def next_in_direction(direction, row, col):
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

def is_expected(table, row, col, expected):
    if row < 0 or row >= len(table):
        return False
    
    if col < 0 or col >= len(table[row]):
        return False
    
    return table[row][col] == expected

    

def xmas(table, row, col, expected, direction=None):
    if not is_expected(table, row, col, expected):
        return 0
    
    current = table[row][col]

    if current == "S":
        return 1
    
    count = 0
    if current == "X":
        for d in directions:
            next_row, next_col = next_in_direction(d, row, col)
            count += xmas(table, next_row, next_col, "M", d)
    else:
        next_row, next_col = next_in_direction(direction, row, col)
        count += xmas(table, next_row, next_col, "A" if current == "M" else "S", direction)

    return count

def mas(table, row, col):
    if not (is_expected(table, row-1, col-1, "M") and is_expected(table, row+1, col+1, "S")) and \
        not (is_expected(table, row-1, col-1, "S") and is_expected(table, row+1, col+1, "M")):
        return 0

    if not (is_expected(table, row-1, col+1, "M") and is_expected(table, row+1, col-1, "S")) and \
        not (is_expected(table, row-1, col+1, "S") and is_expected(table, row+1, col-1, "M")):
        return 0
    
    return 1

with open("input.txt") as f:
    table = f.read().splitlines()

xmas_count, mas_count = 0, 0
for row in range(len(table)):
    for col in range(len(table[row])):
       xmas_count += xmas(table, row, col, "X")
       if table[row][col] == "A":
           mas_count += mas(table, row, col)

print(xmas_count, mas_count)