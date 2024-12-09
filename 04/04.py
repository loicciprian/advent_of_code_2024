INPUT_FILE = '04_input.txt'
n = 0
GRID = []


with open(INPUT_FILE, encoding='utf-8') as f:
    for line in f.readlines():
        GRID.append(line.replace('\n',''))

# GRID[y][x] to get letter on (x,y) coordinates of the grid
Mx = len(GRID[0])
My = len(GRID)
 

# search horizontally
print('--- search horizontally ---')
for y in range(My):
    search_area = ''
    for x in range(Mx):
        search_area += GRID[y][x]
    print(search_area,'-',search_area.count('XMAS') + search_area.count('SAMX'))
    n += search_area.count('XMAS') # left to right
    n += search_area.count('SAMX') # right to left


# search vertically
print('--- search vertically ---')
for x in range(Mx):
    search_area = ''
    for y in range(My):
        search_area += GRID[y][x]
    print(search_area,'-',search_area.count('XMAS') + search_area.count('SAMX'))
    n += search_area.count('XMAS') # up to down
    n += search_area.count('SAMX') # down to up


# search top left <-> bottom right
print('--- top left <-> bottom right  ---')
for x in range(Mx-4,0,-1):
    i = x
    j = 0
    search_area = ''
    while i<Mx and j<My:
        search_area += GRID[j][i]
        i+=1
        j+=1
    print(search_area,'-',search_area.count('XMAS') + search_area.count('SAMX'))
    n += search_area.count('XMAS') # top left to bottom right
    n += search_area.count('SAMX') # bottom right to top left

for y in range(0,My-3):
    i = 0
    j = y
    search_area = ''
    while i<Mx and j<My:
        search_area += GRID[j][i]
        i+=1
        j+=1
    print(search_area,'-',search_area.count('XMAS') + search_area.count('SAMX'))
    n += search_area.count('XMAS') # top left to bottom right
    n += search_area.count('SAMX') # bottom right to top left


# search top right <-> bottom left
print('--- top right <-> bottom left  ---')
for x in range(3,Mx):
    i = x
    j = 0
    search_area = ''
    while i>=0 and j<My:
        search_area += GRID[j][i]
        i-=1
        j+=1
    print(search_area,'-',search_area.count('XMAS') + search_area.count('SAMX'))
    n += search_area.count('XMAS') # top right to bottom left
    n += search_area.count('SAMX') # bottom left to top right

for y in range(1,My-3):
    i = Mx-1
    j = y
    search_area = ''
    while i>=0 and j<My:
        search_area += GRID[j][i]
        i-=1
        j+=1
    print(search_area,'-',search_area.count('XMAS') + search_area.count('SAMX'))
    n += search_area.count('XMAS') # top right to bottom left
    n += search_area.count('SAMX') # bottom left to top right


print(f'XMAS_counter: {n}')