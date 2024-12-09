import re

INPUT_FILE = '03_input.txt'
TOTAL = 0

with open(INPUT_FILE, encoding='utf-8') as f:
    for line in f.readlines():
        # 1st part
        # correct_data = re.findall(r'mul\((\d+),(\d+)\)',line) 
        # multiplications = [int(k[0]) * int(k[1]) for k in correct_data]
        # TOTAL += sum(multiplications)

        # 2nd part
        do_commands = line.split("don't()")[0]
        for cmd in line.split("don't()")[1:]:
            do_commands += ''.join(cmd.split("do()")[1:])

        correct_data = re.findall(r'mul\((\d+),(\d+)\)',do_commands) 
        multiplications = [int(k[0]) * int(k[1]) for k in correct_data]
        TOTAL += sum(multiplications)
        
print(f'sum of multiplications: {TOTAL}')

