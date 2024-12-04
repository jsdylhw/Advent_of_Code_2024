n, m = 0, 0
data = []
with open('data.txt', 'r') as f:
    for line in f:
        data.append(list(line.strip()))
        n += 1
    m = len(line)



def search(data, i, j):
    ans = 0
    if i >= 3 and j >= 3:
        temp = data[i][j] + data[i - 1][j - 1] + data[i - 2][j - 2] + data[i - 3][j - 3]
        if temp == 'XMAS' or temp == 'SAMX':
            ans += 1

    if i >= 3:
        temp = data[i][j] + data[i - 1][j] + data[i - 2][j] + data[i - 3][j]
        if temp == 'XMAS' or temp == 'SAMX':
            ans += 1

    if j >= 3:
        temp = data[i][j] + data[i][j - 1] + data[i][j - 2] + data[i][j - 3]
        if temp == 'XMAS' or temp == 'SAMX':
            ans += 1

    if i >= 3 and j < m - 3:
        temp = data[i][j] + data[i - 1][j + 1] + data[i - 2][j + 2] + data[i - 3][j + 3]
        if temp == 'XMAS' or temp == 'SAMX':
            ans += 1

    if i < n - 3:
        temp = data[i][j] + data[i + 1][j] + data[i + 2][j] + data[i + 3][j]
        if temp == 'XMAS' or temp == 'SAMX':
            ans += 1

    if j < m - 3:
        temp = data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i][j + 3]
        if temp == 'XMAS' or temp == 'SAMX':
            ans += 1

    if i < n - 3 and j < m - 3:
        temp = data[i][j] + data[i + 1][j + 1] + data[i + 2][j + 2] + data[i + 3][j + 3]
        if temp == 'XMAS' or temp == 'SAMX':
            ans += 1

    if i < n - 3 and j >= 3:
        temp = data[i][j] + data[i + 1][j - 1] + data[i + 2][j - 2] + data[i + 3][j - 3]
        if temp == 'XMAS' or temp == 'SAMX':
            ans += 1
    return ans
solu = 0
for i in range(n):
    for j in range(m):
        solu += search(data,i,j)
print(solu // 2)