from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def search(matrix, i, j, visited):
    d = deque()
    d.append((i,j))
    char = matrix[i][j]
    visited[i][j] = 1
    area = 0
    perimeter = 0

    while d:
        x, y = d.popleft()
        area += 1
        for dx, dy in directions:
            if x + dx < 0: perimeter += 1
            if y + dy < 0: perimeter += 1
            if x + dx >= n: perimeter += 1
            if y + dy >= m: perimeter += 1
            if 0 <= x + dx < n and 0 <= y + dy < m and matrix[x + dx][y + dy] != char:
                perimeter += 1
            if (0 <= x + dx < n and 0 <= y + dy < m
                    and visited[x + dx][y + dy] == 0 and matrix[x + dx][y + dy] == char):
                d.append((x + dx, y + dy))
                visited[x + dx][y + dy] = 1

    return area * perimeter




matrix = []
with open('data') as f:
    for line in f:
        matrix.append(list(line.strip()))

price = 0
n, m = len(matrix), len(matrix[0])
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            price += search(matrix, i, j, visited)
print(price)
