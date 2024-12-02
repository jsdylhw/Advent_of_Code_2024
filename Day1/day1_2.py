from collections import Counter
xs, ys = [], []
with open('data.txt', 'r') as file:
    for line in file:
        data = line.split()
        xs.append(int(data[0]))
        ys.append(int(data[1]))

c = Counter(ys)
print(sum(i * c[i] for i in xs))