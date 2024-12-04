n, m = 0, 0
data = []
with open('data.txt', 'r') as f:
    for line in f:
        data.append(list(line.strip()))
        n += 1
    m = len(line)


def search(i, j):
    l = [data[i - 1][j - 1],
         data[i - 1][j + 1],
         data[i + 1][j - 1],
         data[i + 1][j + 1]]
    if sorted(l) == ['M', 'M', 'S', 'S'] and (data[i - 1][j - 1] == data[i - 1][j + 1] or data[i - 1][j - 1] == data[i + 1][j - 1]):
        return 1
    else:
        return 0
solu = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 'A' and 1 <= i < n - 1 and 1 <= j < m - 1:
            solu += search(i,j)
print(solu)