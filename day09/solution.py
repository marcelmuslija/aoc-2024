def disk_image():
    with open("input.txt") as f:
        diskmap = f.read().strip()

    disk = []
    for i in range(len(diskmap)):
        length = int(diskmap[i])
        block = [str(i//2) if i % 2 == 0 else '.'] * length
        disk += block

    return disk

def find_leftmost_fit(disk, file_length):
    free_size = 0
    for i, c in enumerate(disk):
        if c == '.':
            free_size += 1
            if free_size >= file_length:
                return i-free_size+1
        else:
            free_size = 0
    
    return -1

def defrag1(disk):
    for i in range(1, len(disk)+1):
        if disk[-i] != '.':
            free_space_index = disk.index('.')
            if free_space_index > len(disk)-i:
                break

            disk[free_space_index], disk[-i] = disk[-i], disk[free_space_index]

def defrag2(disk):
    file_index = len(disk)-1
    while file_index >= 0:
        id = disk[file_index]
        if id == '.':
            file_index -= 1
            continue

        file_length = 0
        while disk[file_index - file_length] == id:
            file_length += 1
        
        free_index = find_leftmost_fit(disk, file_length)
        
        if free_index < 0 or free_index > file_index:
            file_index -= file_length
            continue
        
        for i in range(file_length):
            disk[free_index+i], disk[file_index-i] = disk[file_index-i], disk[free_index+i]
        
        file_index -= file_length


def checksum(disk):
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            continue
        checksum += i * int(disk[i])

    return checksum

if __name__ == "__main__":
    disk = disk_image()

    # defrag1(disk)

    defrag2(disk)

    print(checksum(disk))