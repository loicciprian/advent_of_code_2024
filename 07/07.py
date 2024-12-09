INPUT_FILE = '07_input.txt'
total_calibration_result = 0

def valid_equation(test_value,ops):
    results = [
        ops[0] + ops[1],
        ops[0] * ops[1],
        int(str(ops[0])+str(ops[1])) # part 2
    ]
    if results.count(test_value): 
        return test_value
    for op in ops[2:]:
        # results = [r+op for r in results] + [r*op for r in results] # part 1
        results = [r+op for r in results] + [r*op for r in results] + [int(str(r)+str(op)) for r in results] # part 2
    if results.count(test_value):
        return test_value
    return 0


with open(INPUT_FILE, encoding='utf-8') as f:
    for line in f.readlines():
        test_value = int(line.split(': ')[0])
        operands = [int(operand) for operand in line.split(': ')[1].split(' ')]

        total_calibration_result += valid_equation(test_value,operands)

print(total_calibration_result)