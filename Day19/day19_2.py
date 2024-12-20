checklist = []
with open('data') as f:
    flag = 0
    for line in f:
        if line == '\n':
            flag = 1
        elif flag == 0:
            avails = line.strip().split(', ')
        else:
            checklist.append(line.strip())

ans = 0
for s in checklist:
    l = len(s)
    dp = [0 for _ in range(l + 1)]
    dp[0] = 1
    for i in range(1, l + 1):
        for pattern in avails:
            if i >= len(pattern) and s[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]
    ans += dp[l]
print(ans)