def readfile():
    symbols = dict()
    with open('data') as f:
        n = 0
        for line in f:
            line = line.strip()
            m = len(line)
            for i, ch in enumerate(line):
                if ch != '.':
                    if ch not in symbols:
                        symbols[ch] = []
                    symbols[ch].append([n, i])
            n += 1
    antennas = []
    for k in symbols:
        antennas.append(symbols[k])
    return n, m, antennas


def solve(n, m, antennas):
    antinodes = set()
    for antenna in antennas:
        l = len(antenna)

        for i in range(l - 1):
            for j in range(i + 1, l):
                dx = antenna[j][0] - antenna[i][0]
                dy = antenna[j][1] - antenna[i][1]

                x, y = antenna[j][0], antenna[j][1]
                antinodes.add((x, y))
                while 0 <= x + dx <= n - 1 and 0 <= y + dy <= m - 1:
                    x += dx
                    y += dy
                    antinodes.add((x, y))
                x, y = antenna[i][0], antenna[i][1]
                antinodes.add((x, y))
                while 0 <= x - dx <= n - 1 and 0 <= y - dy <= m - 1:
                    x -= dx
                    y -= dy
                    antinodes.add((x, y))
    return len(antinodes)


if __name__ == '__main__':
    n, m, antennas = readfile()
    ans = solve(n, m ,antennas)
    print(ans)
