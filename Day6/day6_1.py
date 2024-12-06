def readfile():
    matrix = []
    with open('data.txt') as f:
        for line in f:
            matrix.append(list(line.strip()))
    return matrix


def answer():
    matrix = readfile()

    n, m = len(matrix), len(matrix[0])
    visited = [[0] * m for _ in range(n)]
    direction = 0
    # 0 -> up
    # 1 -> left
    # 2 -> down
    # 3 -> right

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '^':
                sx, sy = i, j
                visited[i][j] = 1
    while sx != 0 and sx != n - 1 and sy != 0 and sy != m - 1:

        if direction == 0:
            if matrix[sx - 1][sy] != '#':
                sx, sy = sx - 1, sy
                visited[sx][sy] = 1
            else:
                direction = 3
        if direction == 1:
            if matrix[sx][sy - 1] != '#':
                sx, sy = sx, sy - 1
                visited[sx][sy] = 1
            else:
                direction = 0
        if direction == 2:
            if matrix[sx + 1][sy] != '#':
                sx, sy = sx + 1, sy
                visited[sx][sy] = 1
            else:
                direction = 1
        if direction == 3:
            if matrix[sx][sy + 1] != '#':
                sx, sy = sx, sy + 1
                visited[sx][sy] = 1
            else:
                direction = 2

    s = 0
    for i in visited:
        s += sum(i)
    print(s)


if __name__ == '__main__':
    answer()