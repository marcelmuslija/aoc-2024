def trail(map, i, j, height, reached_peaks):
    if i < 0 or i >= len(map):
        return 0

    if j < 0 or j >= len(map[0]):
        return 0

    if map[i][j] != height:
        return 0

    if map[i][j] == 9:
        reached_peaks.add((i,j))
        return 1
    
    return trail(map, i-1, j, height+1, reached_peaks) + \
        trail(map, i+1, j, height+1, reached_peaks) + \
        trail(map, i, j-1, height+1, reached_peaks) + \
        trail(map, i, j+1, height+1, reached_peaks)


if __name__ == "__main__":

    with open("input.txt") as f:
        map = [[int(c) for c in line] for line in f.read().splitlines()]

    score = 0
    rating = 0
    for i in range(len(map)):
        for j in range(len(map)):
            reached_peaks = set()
            rating += trail(map, i, j, 0, reached_peaks)
            score += len(reached_peaks)

    print(rating)
    print(score)