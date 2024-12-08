from itertools import product

def mul(x, y):
    return x * y

def add(x, y):
    return x + y

def concat(x, y):
    return int(str(x) + str(y))

def is_equation_true(test_value, equation):
    op_count = len(equation) - 1
    op_combos = list(product([add, mul, concat], repeat=op_count))

    for operations in op_combos:
        calibration_result = equation[0]
        for i in range(op_count):
            x = calibration_result
            y = equation[i+1]
            operation = operations[i]
            calibration_result = operation(x, y)

        if calibration_result == test_value:
            return True
    
    return False

if __name__ == "__main__":
    total_calibration_sum = 0
    with open("input.txt") as f:
        lines = f.read().splitlines()
        for l in lines:
            split_line = l.split(": ")
            test_value = int(split_line[0])
            equation = list(map(int, split_line[1].split()))
            if is_equation_true(test_value, equation):
                total_calibration_sum += test_value                
    print(total_calibration_sum)