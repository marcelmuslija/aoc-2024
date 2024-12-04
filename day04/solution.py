directions = ["NW", "N", "NE", "W", "E", "SW", "S", "SE"]

def next_in_direction(direction, row, col):
    if direction == "NW":
        return row-1, col-1
    if direction == "N":
        return row-1, col
    if direction == "NE":
        return row-1, col+1
    if direction == "W":
        return row, col-1
    if direction == "E":
        return row, col+1
    if direction == "SW":
        return row+1, col-1
    if direction == "S":
        return row+1, col
    if direction == "SE":
        return row+1, col+1
    
    return -1, -1

def is_char_at_pos(table, row, col, expected):
    if row < 0 or row >= len(table):
        return False
    
    if col < 0 or col >= len(table[row]):
        return False
    
    return table[row][col] == expected

def xmas(table, row, col, expected, direction=None):
    if not is_char_at_pos(table, row, col, expected):
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
    if not (is_char_at_pos(table, row-1, col-1, "M") and is_char_at_pos(table, row+1, col+1, "S")) and \
        not (is_char_at_pos(table, row-1, col-1, "S") and is_char_at_pos(table, row+1, col+1, "M")):
        return 0

    if not (is_char_at_pos(table, row-1, col+1, "M") and is_char_at_pos(table, row+1, col-1, "S")) and \
        not (is_char_at_pos(table, row-1, col+1, "S") and is_char_at_pos(table, row+1, col-1, "M")):
        return 0
    
    return 1

with open("input.txt") as f:
    matrix = f.read().splitlines()

xmas_count, mas_count = 0, 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
       xmas_count += xmas(matrix, row, col, "X")
       if matrix[row][col] == "A":
           mas_count += mas(matrix, row, col)

print(xmas_count, mas_count)