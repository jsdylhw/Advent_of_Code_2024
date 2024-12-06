def readfile():
    matrix = []
    with open('data.txt') as f:
        for line in f:
            matrix.append(list(line.strip()))
    return matrix


def search(matrix, sx, sy):
    visited = [[0] * m for _ in range(n)]
    visited[sx][sy] = 1
    direction = 0
    # 0 -> up
    # 1 -> left
    # 2 -> down
    # 3 -> right

    while sx != 0 and sx != n - 1 and sy != 0 and sy != m - 1:

        if direction == 0:
            if matrix[sx - 1][sy] != '#':
                sx, sy = sx - 1, sy
                visited[sx][sy] += 1
            else:
                direction = 3
        if direction == 1:
            if matrix[sx][sy - 1] != '#':
                sx, sy = sx, sy - 1
                visited[sx][sy] += 1
            else:
                direction = 0
        if direction == 2:
            if matrix[sx + 1][sy] != '#':
                sx, sy = sx + 1, sy
                visited[sx][sy] += 1
            else:
                direction = 1
        if direction == 3:
            if matrix[sx][sy + 1] != '#':
                sx, sy = sx, sy + 1
                visited[sx][sy] += 1
            else:
                direction = 2
        if visited[sx][sy] > 10:
            return True
    return False


if __name__ == '__main__':
    matrix = readfile()

    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '^':
                sx, sy = i, j
    ans = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '.':
                matrix[i][j] = '#'
                if search(matrix, sx, sy):
                    ans += 1
                matrix[i][j] = '.'
    print(ans)