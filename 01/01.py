INPUT_FILE = '01_input.txt'
LEFT = []
RIGHT = []

with open(INPUT_FILE, encoding='utf-8') as f:
    for line in f.readlines():
        l_val ,r_val = line.split('   ')
        LEFT.append(int(l_val))
        RIGHT.append(int(r_val))

LEFT.sort()
RIGHT.sort()
distances = [abs(l-r) for l,r in zip(LEFT, RIGHT)]
# 1st result 
print(f'total_distance: {sum(distances)}')

similarity_scores = [l*RIGHT.count(l) for l in LEFT]
# 2nd result 
print(f'total_similarity_score: {sum(similarity_scores)}')