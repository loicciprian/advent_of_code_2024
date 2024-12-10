""" ONLY if len(line) < 20 ; highest file_id == 9 """

INPUT_FILE = '09_input_test.txt'


def block_move(s):
    print(s.replace('.', s[-1], 1)[:-1]+'.')
    return s.replace('.', s[-1], 1)[:-1]


with open(INPUT_FILE, encoding='utf-8') as f:
    for line in f.readlines():
        # 1. get disk map layout
        ## rewrite disk map dense format into the layout of files and free space on the disk (ex: '12345' --> '0..111....22222')
        disk_map = ''.join([str(file_id)*int(n_file) + '.'*int(n_free_space) for file_id,n_file,n_free_space in zip(range(10),line[::2],(line+'0')[1::2])])
        print(disk_map)

        # 2. file-compacting process
        ## move file blocks one at a time from the end of the disk to the leftmost free space block
        while disk_map.count('.'):
            disk_map = block_move(disk_map)

        # 3. update filesystem checksum
        ## add up the result of multiplying each of these blocks' position with the file ID number it contains
        checksum = sum([file_pos*int(file_id) for file_pos,file_id in enumerate(disk_map)])

print(checksum)