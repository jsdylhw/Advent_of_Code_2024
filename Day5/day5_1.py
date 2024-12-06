def read_rules():
    d = dict()
    with open('page_ordering_rules.txt') as f:
        for line in f:
            x, y = map(int, line.split('|'))

            if x not in d:
                d[x] = [y]
            else:
                d[x].append(y)
    return d

def read_updates():
    updates = []
    with open('pages_to_produce_in_each_update.txt') as f:
        for line in f:
            updates.append(list(map(int, line.split(','))))

    return updates

def check(rule, d):
    avail = set()
    for i in d[rule[0]]:
        avail.add(i)
    for i in range(1, len(rule)):

        if rule[i] not in avail:
            return False
        else:
            if rule[i] in d:
                for j in d[rule[i]]:
                    if j in rule[:i]:
                        return False
                for j in d[rule[i]]:
                    avail.add(j)
        if i == len(rule) - 1:
            return True

def ans1():
    d = read_rules()
    updates = read_updates()
    s = 0
    for update in updates:
        if check(update, d) == True:
            s += update[len(update) // 2]
    print(f'answer for 5_1 is {s}')



if __name__ == '__main__':
    ans1()
