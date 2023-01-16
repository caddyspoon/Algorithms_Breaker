# Test Case Below
# N = 5
# tree_input = [-1, 0, 0, 1, 1]
# target = 1
#

# N = 9
# tree_input = [-1, 0, 0, 2, 2, 4, 4, 6, 6]
# target = 4

from collections import deque

N = int(input())
tree_input = list(map(int, input().split()))
target = int(input())

tree = [[] for _ in range(N)]
root = None
target_parent = None

for i in range(N):
    parent = tree_input[i]
    node = i

    if parent == -1:
        root = node
    else:
        tree[parent].append(node)

    if node == target:
        target_parent = parent

if root == target:
    print(0)
else:
    tree[target_parent].remove(target)

    stack = deque()

    for child in tree[target]:
        stack.append(child)

    tree[target] = None

    while stack:
        child_node = stack.pop()

        for grand_child in tree[child_node]:
            stack.append(grand_child)
        tree[child_node] = None

    answer = 0
    for elm in tree:
        if elm == None:
            continue

        if len(elm) == 0:
            answer += 1

    print(answer)