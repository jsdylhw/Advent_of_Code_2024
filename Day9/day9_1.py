
def readfile():
    with open('data') as f:
        for line in f:
            return line.strip()


def solve(s):
    l = len(s)
    blocks = ''
    idx = 0
    for i in range(l):
        if i % 2 == 0:
            blocks += str(idx) * int(s[i])
            idx += 1
        else:
            blocks += '.' * int(s[i])

    blocks = list(blocks)


    left = 0
    right = len(blocks) - 1

    while left <= right:
        while blocks[right] == '.': right -= 1
        if blocks[left] != '.':
            left += 1
        else:
            blocks[left] = blocks[right]
            blocks[right] = '.'
            left += 1
            right -= 1

    return sum(int(i) * idx for idx, i in enumerate(blocks) if i.isdigit())


if __name__ == '__main__':
    s = readfile()

    ans = solve(s)
    print(ans)