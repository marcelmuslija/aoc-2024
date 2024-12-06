import copy

class Map:
    def __init__(self, map):
        self._map = map
        self.width = len(map[0])
        self.height = len(map)

    def __iter__(self):
        return self._map.__iter__()
    
    def __next__(self):
        return self._map.__next__()
    
    def __getitem__(self, x):
        return self._map[x]
    
    def has_obstacle_at(self, x, y):
        if x < 0 or x >= len(self._map):
            return False

        if y < 0 or y >= len(self._map[0]):
            return False
        
        return self._map[x][y] == "#"

    def find_guard(self):
        for x in range(len(self._map)):
            if '^' in self._map[x]:
                return x, self._map[x].find('^')
            
        raise ValueError("Guard not on map")
    
    def mark(self, x, y, symbol):
        row = list(self._map[x])
        row[y] = symbol
        self._map[x] = "".join(row)

class Guard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = "NORTH"
        self.moves = {}

    def rotate(self):
        if self.direction == "NORTH":
            self.direction = "EAST"
        elif self.direction == "EAST":
            self.direction = "SOUTH"
        elif self.direction == "SOUTH":
            self.direction = "WEST"
        else:
            self.direction = "NORTH"

    def is_inside(self, map):
        if self.x < 0 or self.x >= map.width:
            return False
        
        if self.y < 0 or self.y >= map.height:
            return False

        return True
    
    def is_in_loop(self):
        pos = self.x, self.y

        # guard is in previous position and moving in same direction
        return self.direction == self.moves.get(pos, "")

    def _next_pos(self):
        if self.direction == "NORTH":
            return self.x-1, self.y
        if self.direction == "EAST":
            return self.x, self.y+1
        if self.direction == "SOUTH":
            return self.x+1, self.y
        
        return self.x, self.y-1

    def move(self, map):
        self.moves[self.x, self.y] = self.direction
        x, y = self._next_pos()
        while map.has_obstacle_at(x, y):
            self.rotate()
            x, y = self._next_pos()

        self.x, self.y = x, y

    def patrol(self, map):
        while guard.is_inside(map) and not guard.is_in_loop():
            map.mark(guard.x, guard.y, "X")
            guard.move(map)



if __name__ == "__main__":
    with open("input.txt") as f:
        original_map = Map(f.read().splitlines())

    patroled_map = copy.deepcopy(original_map)
    
    start = patroled_map.find_guard()
    guard = Guard(*start)

    guard.patrol(patroled_map)

    # part one solution
    print("".join(patroled_map).count('X'))

    """ 
        Use the patroled map to see where the guard moves when no obstacles are added.
        When you find a position the guard visited (exclude the starting position):
            Copy the original map, and put an obstacle at that position.
            Create a new guard at the starting position and patrol the map copy.
            Once the patrol is over, check if it ended because he got stuck in a loop.
    """
    loop_counts = 0
    for x in range(patroled_map.height):
        for y in range(patroled_map.width):
            if patroled_map[x][y] == "X" and (x, y) != start:
                looped_map = copy.deepcopy(original_map)
                guard = Guard(*start)
                looped_map.mark(x, y, "#")
                guard.patrol(looped_map)
                if guard.is_in_loop():
                    loop_counts += 1
    
    print(loop_counts)