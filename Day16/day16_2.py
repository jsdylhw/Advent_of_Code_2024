from collections import deque
ans = float('inf')

maze = []
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
# (0 1) right
# (-1 0) up
# (0 -1) left
# (1 0) down
with open('data') as f:
    for line in f:
        maze.append(list(line.strip()))

n, m = len(maze), len(maze[0])
for i in range(n):
    for j in range(m):
        if maze[i][j] == 'S':
            x, y = i, j
            break
for i in range(n):
    for j in range(m):
        if maze[i][j] == 'E':
            endx, endy = i, j
            break

dis = [[[float('inf') for _ in range(4)] for _ in range(m)] for _ in range(n)]
dis[x][y][0] = 0
d = deque()
d.append((x, y, 0, [(x, y)], 0))
answers = []
while d:
    x, y, direc, path, score = d.popleft()
    if x == endx and y == endy:
        answers.append([path, score])
    dx, dy = directions[direc]

    if 0 <= x + dx < n and 0 <= y + dy < m and maze[x + dx][y + dy] != '#' and dis[x][y][direc] + 1 <= dis[x + dx][y + dy][direc]:
        dis[x + dx][y + dy][direc] = dis[x][y][direc] + 1
        d.append((x + dx, y + dy, direc, path + [(x + dx, y + dy)], score + 1))
    r1, r2 = (direc + 1) % 4, (direc - 1) % 4

    if dis[x][y][direc] + 1000 <= dis[x][y][r1]:
        dis[x][y][r1] = dis[x][y][direc] + 1000
        d.append((x, y, r1, path, score + 1000))
    if dis[x][y][direc] + 1000 <= dis[x][y][r2]:
        dis[x][y][r2] = dis[x][y][direc] + 1000
        d.append((x, y, r2, path, score + 1000))

vis = set()
ans = min(dis[endx][endy])
for path, score in answers:
    if score == ans:
        for i in path:
            vis.add(i)
print(len(vis))
