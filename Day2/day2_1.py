def is_safe(data):
    flag = 1 if data[0] < data[1] else 0   # 1 increase
    if flag == 1:
        for i in range(1, len(data)):
            t = data[i] - data[i - 1]
            if not(1 <= t <= 3):
                return 0

    if flag == 0:
        for i in range(1, len(data)):
            t = data[i - 1] - data[i]
            if not(1 <= t <= 3):
                return 0
    return 1

s = 0
with open('data.txt', 'r') as file:
    for line in file:
        data = list(map(int, line.split()))
        s += is_safe(data)
print(s)