inputs = []
with open('test') as f:
    for line in f:
        if line != '\n':
            inputs.append(line.strip())

def solve(a1, a2, b1, b2, x, y):
    numa = numb = 0
    ans = 999999
    solvable = False
    for i in range(min(100, x // a1 + 1)):
        if (x - i * a1) % b1 == 0 and (x - i * a1) // b1 <= 100:
            numa = i
            numb = (x - i * a1) // b1 
            if numa * a2 + numb * b2 == y and 3 * numa + numb < ans:
                ans = 3 * numa + numb
                solvable = True
    if solvable:
        return ans
    else:
        return 0
ans = 0
print(len(inputs))
for i in range(0, len(inputs), 3):
    i1, i2 ,i3 = inputs[i].split(), inputs[i + 1].split(), inputs[i + 2].split()
    
    a1 = int(i1[2][2:-1])
    a2 = int(i1[3][2:])
    b1 = int(i2[2][2:-1])
    b2 = int(i2[3][2:])
    x = int(i3[1][2:-1])
    y = int(i3[2][2:])
    ans += solve(a1, a2, b1, b2, x, y)
print(a1, a2, b1, b2, x, y)
print(ans)