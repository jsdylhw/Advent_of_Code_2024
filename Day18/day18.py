
from collections import deque
n ,m = 71, 71
grids = [['.' for _ in range(m)] for _ in range(n)]
with open('data') as file:
    counter = 0
    for line in file:
        x, y = map(int, line.split(','))

        grids[y][x] = '#'
        counter += 1
        if counter == 2991:
            print(x, y)
            exit()

from collections import deque
ans = float('inf')

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]




dis = [[float('inf') for _ in range(m)] for _ in range(n)]
dis[0][0] = 0
d = deque()
d.append((0, 0))
while d:

    x, y = d.popleft()

    if x == n and y == m:
        continue
    for dx, dy in directions:

        if 0 <= x + dx < n and 0 <= y + dy < m and grids[x + dx][y + dy] != '#' and dis[x][y] + 1 < dis[x + dx][y + dy]:
            dis[x + dx][y + dy] = dis[x][y] + 1
            d.append((x + dx, y + dy))


print(dis[n - 1][m - 1])
