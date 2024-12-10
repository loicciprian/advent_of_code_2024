INPUT_FILE = '09_input_test.txt'
disk_map = []
file_id = 0

def block_move(l):
    # print(s.replace('.', s[-1], 1)[:-1])
    l[l.index('.')] = l.pop()
    # print(''.join(l))


def file_move(l,file_id):
    # count last file blocks
    file_size = l.count(file_id)
    file_pos = l.index(file_id)

    # search for enough available leftmost free space to move entire file blocks
    free_space_size = 0
    current_index = l.index('.')
    while free_space_size < file_size and current_index < l.index(file_id):
        # new search for free space
        free_space_size = 0
        free_space_pos = current_index = l.index('.', current_index)
        # count free space blocks
        while l[current_index]=='.':
            free_space_size += 1
            current_index += 1

    # move file to leftmost available space
    if free_space_size >= file_size:
        for k in range(file_size):
            l[free_space_pos + k]=file_id
            l[file_pos + k]='.'
    print(''.join([str(k) for k in l]))



with open(INPUT_FILE, encoding='utf-8') as f:
    for line in f.readlines():
        # 1. get disk map layout
        ## rewrite disk map dense format into the layout of files and free space on the disk (ex: '12345' --> '0..111....22222')
        for n,val  in enumerate(line):
            if int(n) % 2 == 0: # files 
                disk_map += [str(file_id)]*int(val)
                file_id += 1
            else: # free space
                disk_map += ['.']*int(val)
        print(''.join(disk_map))

        # 2. file-compacting process
        ## move file blocks from the end of the disk to the leftmost free space block
        # part 1
        # while disk_map.count('.'):
        #     block_move(disk_map)
        # part 2
        for file_id in range(int(disk_map[-1]),0,-1):
            # print(file_id)
            file_move(disk_map, str(file_id))

        # 3. update filesystem checksum
        ## add up the result of multiplying each of these blocks' position with the file ID number it contains
        checksum = sum([file_pos*int(file_id) for file_pos,file_id in enumerate(disk_map) if file_id != '.'])

print(checksum)