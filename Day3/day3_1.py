def solve(line):
    ans = 0
    i = 0
    l = len(line)
    while i < len(line):
        if i + 4 <= l and line[i:i + 4] == 'mul(':
            j = i + 4
            if line[j:j + 3].isdigit():
                j = j + 3
            elif line[j:j + 2].isdigit():
                j = j + 2
            elif line[j:j + 1].isdigit():
                j = j + 1
            if line[j] == ',':

                if line[j + 1:j + 4].isdigit() and line[j + 4] == ')':
                    ans += int(line[j + 1:j + 4]) * int(line[i + 4: j])
                elif line[j + 1:j + 3].isdigit() and line[j + 3] == ')':
                    ans += int(line[j + 1:j + 3]) * int(line[i + 4: j])
                elif line[j + 1:j + 2].isdigit() and line[j + 2] == ')':
                    ans += int(line[j + 1:j + 2]) * int(line[i + 4: j])
        i += 1
    return ans


s = 0

with open('data.txt') as file:
    for line in file:
        s += solve(line)
print(s)