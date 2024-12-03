def isSafe(levels):
    MIN_DIFF = 1
    MAX_DIFF = 3
    
    isIncreasing = levels[1] - levels[0] > 0
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i-1]
        if abs(diff) < MIN_DIFF or abs(diff) > MAX_DIFF:
            return False
        
        if isIncreasing and diff <= 0:
            return False
        
        if not isIncreasing and diff >= 0:
            return False
        
    return True

def combos(levels):
    combos = []

    for i in range(len(levels)):
        combos.append(levels[:i] + levels[i+1:])
    
    return combos

with open('input.txt') as f:
    reports = f.read().splitlines()

    safeCount = 0
    for report in reports:
        levels = list(map(int, report.split()))
        
        # part one
        if isSafe(levels): 
            safeCount += 1
        # part two
        else:
            for combo in combos(levels):
                if isSafe(combo):
                    safeCount += 1
                    break
    
    print(safeCount)
