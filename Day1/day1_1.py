xs, ys = [], []
with open('data.txt', 'r') as file:
    for line in file:
        data = line.split()
        xs.append(int(data[0]))
        ys.append(int(data[1]))


xs = sorted(xs)
ys = sorted(ys)
print(sum(abs(i - j) for i, j in zip(xs, ys)))