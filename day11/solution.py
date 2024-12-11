import argparse
from collections import defaultdict

def blink(stones):
    new_stones = defaultdict(lambda: 0)
    for stone in stones.copy().keys():
        if stone == '0':
            new_stones['1'] += stones[stone]
        elif len(stone) % 2 == 0:
            half = len(stone)//2
            l = stone[:half]
            r = str(int(stone[half:]))
            new_stones[l] += stones[stone]
            new_stones[r] += stones[stone]
        else:
            new_stones[str(int(stone) * 2024)] += stones[stone] 
    
    return new_stones

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AOC2024 - Day 11")
    parser.add_argument("blinks", type=int, help="The number of blinks to perform.")

    args = parser.parse_args()
    
    blinks = args.blinks

    stones = defaultdict(lambda: 0)
    with open("input.txt") as f:
        for n in f.read().split():
            stones[n] += 1 

    for i in range(blinks):
        stones = blink(stones)
    
    print(sum(stones.values()))
