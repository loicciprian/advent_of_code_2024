INPUT_FILE = '02_input.txt'
counter = 0

def is_safe(report):
    delta = [int(i)-int(j) for i,j in zip(report[1:],report[:-1])]
    return (all([x>0 for x in delta]) and max(delta) <= 3) or (all([x<0 for x in delta]) and min(delta) >= -3)

with open(INPUT_FILE, encoding='utf-8') as f:
    for line in f.readlines():
        report = line.split(' ')
        if is_safe(report):
            counter += 1

        else: # problem Dampener removing one level
            for k in range(len(report)):
                damp_report = report[:k]+report[k+1:]
                if is_safe(damp_report):
                    counter += 1
                    break
        
print(f'safe reports: {counter}')