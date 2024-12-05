import collections

def load():
    rules = collections.defaultdict(list)
    updates = []
    with open("input.txt") as f:
        lines = f.read().splitlines()
        reading_rules = True
        for l in lines:
            if l == "":
                reading_rules = False
                continue
            
            if reading_rules:
                x, y = map(int, l.split("|"))
                rules[x].append(y)
            else:
                updates.append(list(map(int, l.split(","))))
        
    return rules, updates

def getfix(update, rules):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if update[i] in rules[update[j]]:
                return i, j
    
    return NO_FIX

if __name__ == "__main__":
    rules, updates = load()

    NO_FIX = -1, -1

    sum_correct = 0
    sum_fixed = 0
    for update in updates:
        i, j = getfix(update, rules)
        if (i, j) == NO_FIX:
            sum_correct += update[len(update)//2]
        else:
            while (i, j) != NO_FIX:
                update.insert(i, update.pop(j))
                i, j = getfix(update, rules)
            sum_fixed += update[len(update)//2]

    print(sum_correct, sum_fixed)