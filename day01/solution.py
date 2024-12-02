left, right = [], []

with open("input.txt") as f:
    lines = f.read().splitlines()
    for l in lines:
        first, second = map(int, l.split())
        left.append(first)
        right.append(second)

lSorted = sorted(left)
rSorted = sorted(right)

distSum = 0
similarityScore = 0
for i in range(len(left)):
    distSum += abs(lSorted[i]-rSorted[i])
    similarityScore += lSorted[i] * rSorted.count(lSorted[i])

# part one
print(distSum)

# part two
print(similarityScore)
