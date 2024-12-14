from collections import Counter
def count_stones(count):
    new_count = Counter()
    for stone, n in count.items():

        if stone == 0:
            new_count[1] += n
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            new_count[int(s[:(len(s) // 2)])] += n
            new_count[int(s[(len(s) // 2):])] += n
        else:
            new_count[stone * 2024] += n
    return new_count



count = Counter([572556, 22, 0, 528, 4679021, 1, 10725, 2790])
for _ in range(75):
    count = count_stones(count)
sum(count.values())