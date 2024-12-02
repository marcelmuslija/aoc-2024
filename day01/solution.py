left, right = [], []

with open("input.txt") as f:
    lines = f.read().splitlines()
    for l in lines:
        first, second = map(int, l.split())
        left.append(first)
        right.append(second)

l_sorted = sorted(left)
r_sorted = sorted(right)

dist_sum = 0
similarity_score = 0
for i in range(len(left)):
    dist_sum += abs(l_sorted[i]-r_sorted[i])
    similarity_score += l_sorted[i] * r_sorted.count(l_sorted[i])

# part one
print(dist_sum)

# part two
print(similarity_score)


