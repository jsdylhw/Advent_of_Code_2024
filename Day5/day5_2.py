rules_input = []
with open('page_ordering_rules.txt') as f:
    for line in f:
        rules_input.append(line.split())

updates_input = []
with open('pages_to_produce_in_each_update.txt') as f:
    for line in f:
        updates_input.append(list(map(int, line.split(','))))

def parse_rule(rule_line):
    x, y = rule_line.strip().split("|")
    return int(x), int(y)



def is_update_in_correct_order(update, rules):
    # 将更新中的页面及其所在位置记录下来
    position = {page: i for i, page in enumerate(update)}
    update_pages = set(update)

    # 检查规则
    for x, y in rules:
        if x in update_pages and y in update_pages:
            # 若有 X|Y 的规则，需保证在更新中 X 出现位置在 Y 之前
            if position[x] >= position[y]:
                return False
    return True

def sort_update_correctly(update, rules):
    # 对无序更新进行排序，使其符合规则
    # 思路：这相当于一个拓扑排序问题。如果我们将页面视为节点，
    # 规则X|Y表示有向边X->Y，要求X在Y之前出现。
    # 对update中出现的页面进行子图提取，然后对这些页面进行拓扑排序。

    # 提取只包含当前update中页面的子图规则
    update_pages = set(update)
    # 构建图的入度和邻接表
    graph = {p: [] for p in update_pages}
    indegree = {p: 0 for p in update_pages}

    for x, y in rules:
        if x in update_pages and y in update_pages:
            graph[x].append(y)
            indegree[y] += 1

    # 拓扑排序（Kahn算法）
    from collections import deque
    q = deque([p for p in update_pages if indegree[p] == 0])

    sorted_update = []
    while q:
        node = q.popleft()
        sorted_update.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    # sorted_update中应包含update中所有页面，且为符合规则的顺序
    # 如果排序后元素数量与update数量一致，则排序成功
    if len(sorted_update) == len(update):
        return sorted_update
    else:
        # 理论上不应出现无法排序的情况（题意暗示都有合法顺序）
        # 若出现则原样返回
        return update

# 解析规则

# 解析更新
all_updates = updates_input

# 确定哪些是正确有序的，哪些是错误的
correctly_ordered = []
incorrectly_ordered = []

for up in all_updates:
    if is_update_in_correct_order(up, all_rules):
        correctly_ordered.append(up)
    else:
        incorrectly_ordered.append(up)

# 对错误的更新进行重新排序
sorted_incorrect_updates = [sort_update_correctly(up, all_rules) for up in incorrectly_ordered]

# 找出这些更新的中间页面并求和
sum_middle_pages = 0
for up in sorted_incorrect_updates:
    mid_index = len(up) // 2
    sum_middle_pages += up[mid_index]

print(sum_middle_pages)  # 根据示例应为 123