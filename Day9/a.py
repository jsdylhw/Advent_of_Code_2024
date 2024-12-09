import os

def readfile():
    if os.path.exists('data'):
        with open('data') as f:
            return f.read().strip()
    return '2333133121414131402'  # Default for testing/debugging

def solve(s):
    length = len(s)
    disk_layout = ''
    idx = 0

    for i in range(length):
        if i % 2 == 0:
            disk_layout += str(idx) * int(s[i])  # Add file blocks
            idx += 1
        else:
            disk_layout += '.' * int(s[i])  # Add free space

    disk_layout = list(disk_layout)
    left, right = 0, len(disk_layout) - 1

    # Compact files
    while left <= right:
        while disk_layout[right] == '.':
            right -= 1
        if disk_layout[left] != '.':
            left += 1
        else:
            disk_layout[left] = disk_layout[right]
            left += 1
            right -= 1

    # Calculate checksum
    return sum(int(disk_layout[i]) * i for i in range(left) if disk_layout[i].isdigit())

if __name__ == '__main__':
    s = readfile()
    ans = solve(s)
    print(ans)
