from sympy import symbols, Eq, solve

x, y = symbols('x y')
inputs = []
with open('data') as f:
    for line in f:
        if line != '\n':
            inputs.append(line.strip())


def bottons(a1, a2, b1, b2, c1, c2):
    equation1 = Eq(a1 * x + b1 * y, c1)

    equation2 = Eq(a2 * x + b2 * y, c2)
    solutions = solve((equation1, equation2), (x, y))

    if int(solutions[x]) == solutions[x] and int(solutions[y]) == solutions[y]:

        return 3 * solutions[x] + solutions[y]
    else:

        return 0


ans = 0

for i in range(0, len(inputs), 3):
    i1, i2, i3 = inputs[i].split(), inputs[i + 1].split(), inputs[i + 2].split()

    a1 = int(i1[2][2:-1])
    a2 = int(i1[3][2:])
    b1 = int(i2[2][2:-1])
    b2 = int(i2[3][2:])
    c1 = int(i3[1][2:-1]) + 10000000000000
    c2 = int(i3[2][2:]) + 10000000000000
    ans += bottons(a1, a2, b1, b2, c1, c2)

print(ans)