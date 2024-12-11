from collections import deque
D = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def readfile():
    map = []
    with open('data') as f:
        for line in f:
            map.append([int(i) for i in line.strip()])
    return map

if __name__ == '__main__':
    map = readfile()
    ans = 0
    
    deque = deque()
    vis = dict()
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                deque.append((i,j,[(i,j)]))
                vis[(i,j)] = set()
    while deque:
        x, y, path = deque.popleft()
        if len(path) == 10:
            vis[(x,y)].add(path[-1])
        for dx, dy in D:
            if (0 <= path[-1][0] + dx < len(map) and 0 <= path[-1][1] + dy < len(map[0])
                    and map[path[-1][0] + dx][path[-1][1] + dy] == len(path)):
                deque.append((x, y, path + [(path[-1][0] + dx, path[-1][1] + dy)]))
    ans = 0
    for i in vis:
        ans += len(vis[i])
    print(ans)