class Node():
    def __init__(self, idx, depth=0):
        self.idx = idx
        self.depth = depth


def solution(n, vertex):
    arr = [[] for _ in range(n+1)]
    for x, y in vertex:
        arr[x].append(y)
        arr[y].append(x)

    depth_arr = [False] * (n+1)
    depth_arr[1] = True

    queue = []
    while arr[1]:
        queue.append(Node(arr[1].pop(), 1))

    far_depth = 0
    far_nodes = []

    while queue:
        node = queue.pop(0)
        idx = node.idx
        depth = node.depth

        if depth_arr[idx]:
            continue

        depth_arr[idx] = depth
        if depth >= far_depth:
            if far_depth == depth:
                far_nodes.append(idx)

            else:
                far_depth = depth
                far_nodes = [idx]

        while arr[idx]:
            elm = arr[idx].pop()
            if not depth_arr[elm]:
                queue.append(Node(elm, depth + 1))

    answer = len(depth_arr)
    return answer


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
result = 3

print(solution(n, vertex) == result)