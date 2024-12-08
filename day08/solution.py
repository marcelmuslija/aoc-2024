from collections import defaultdict
from itertools import combinations


def find_antenna(map, start_x, start_y):
    for x in range(start_x, len(map)):
        for y in range(len(map[0])):
            if x == start_x and y < start_y:
                continue

            if map[x][y] != '.':
                    return map[x][y], x, y

    return "", -1, -1


def get_antinodes(pair, map, part_one=False):
    diff = pair[1][0] - pair[0][0], pair[1][1] - pair[0][1]

    antinodes = []
    multiplier = 1 if part_one else 0
    while True:
        an1 = pair[0][0] - multiplier*diff[0], pair[0][1] - multiplier*diff[1]
        an2 = pair[1][0] + multiplier*diff[0], pair[1][1] + multiplier*diff[1]

        if not is_within_bounds(an1, map) and not is_within_bounds(an2, map):
            break

        if is_within_bounds(an1, map):
            antinodes.append(an1)

        if is_within_bounds(an2, map):
            antinodes.append(an2) 

        if part_one:
            break

        multiplier += 1
        
    return antinodes


def is_within_bounds(antinode, map):
    if antinode[0] < 0 or antinode[0] >= len(map):
        return False
    
    if antinode[1] < 0 or antinode[1] >= len(map[0]):
        return False
    
    return True


if __name__ == "__main__":
    with open("input.txt") as f:
        map = f.read().splitlines()

    antennas = defaultdict(list)

    frequency, x, y = find_antenna(map, 0, 0)
    while frequency != "":
        antennas[frequency].append((x, y))
        frequency, x, y = find_antenna(map, x, y+1)

    antinodes = set()
    for frequency, locations in antennas.items():
        pairs = list(combinations(locations, 2))
        for pair in pairs:
            antinodes.update(get_antinodes(pair, map, part_one=False))

    print(len(antinodes))