from functools import reduce

def solve(s,x):

    if len(x) == 1:
        if x[0] == s:
            return s
        else:
            return 0
    else:
        t1 = x[1:]
        t1[0] += x[0]
        t2 = x[1:]
        t2[0] *= x[0]
        t3 = x[1:]
        t3[0] = int(str(x[0]) + str(x[1]))
        return solve(s, t1) or solve(s, t2) or solve(s, t3)
ans = 0
with open('puzzle.txt') as f:
    for line in f:
        s, x = line.strip().split(':')
        ans += solve(int(s), list(map(int, x.split())))
ans