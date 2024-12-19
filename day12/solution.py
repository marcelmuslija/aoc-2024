from collections import defaultdict

def area_and_perim(map, visited, current_region, perimiters, x, y):
    if x < 0 or x >= len(map):
        perimiters.add((x, y))
        return 0, 1
    
    if y < 0 or y >= len(map[0]):
        perimiters.add((x, y))
        return 0, 1
    
    plant = map[x][y]

    if plant != current_region:
        perimiters.add((x, y))
        return 0, 1
    
    if visited[x][y]:
        return 0, 0

    visited[x][y] = True

    a1, p1 = area_and_perim(map, visited, current_region, perimiters, x-1, y)
    a2, p2 = area_and_perim(map, visited, current_region, perimiters, x+1, y)
    a3, p3 = area_and_perim(map, visited, current_region, perimiters, x, y-1)
    a4, p4 = area_and_perim(map, visited, current_region, perimiters, x, y+1)

    return 1+a1+a2+a3+a4, p1+p2+p3+p4


if __name__ == "__main__":
    with open("test_input.txt") as f:
        map = f.read().splitlines()

    visited = [[False for y in range(len(map[0]))] for x in range(len(map))]

    price = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if not visited[x][y]:
                current_region = map[x][y]
                perimiters = set()
                area, perim = area_and_perim(map, visited, current_region, perimiters, x, y)
                price += area * perim
                print(sorted(perimiters))
    print(price)