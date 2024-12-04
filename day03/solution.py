mem = ""
with open("input.txt") as f:
    mem = f.read()

mul_sum = 0
mul_enabled = True
while "mul" in mem:
    mul_index = mem.index("mul")

    # part two {
    prefix = mem[:mul_index]
    dont_index = prefix.rfind("don't()")
    do_index = prefix.rfind("do()")

    if not mul_enabled and do_index > dont_index:
        mul_enabled = True
    elif mul_enabled and dont_index > do_index:
        mul_enabled = False
    # }  

    mem = mem[mul_index + len("mul"):]

    if not mul_enabled:
        continue

    if mem[0] != "(":
        continue

    mem = mem[1:]
    digit_count = 0
    for c in mem:
        if c.isdigit():
            digit_count += 1
        else:
            break
    
    if digit_count < 1 or digit_count > 3:
        continue

    first = int(mem[:digit_count])

    mem = mem[digit_count:]

    if mem[0] != ",":
        continue

    mem = mem[1:]

    digit_count = 0
    for c in mem:
        if c.isdigit():
            digit_count += 1
        else:
            break
    
    if digit_count < 1 or digit_count > 3:
        continue

    second = int(mem[:digit_count])

    mem = mem[digit_count:]

    if mem[0] != ")":
        continue

    mul_sum += first*second

print(mul_sum)
