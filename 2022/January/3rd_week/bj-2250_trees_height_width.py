import sys
sys.stdin = open('bj-2250.txt', 'r')

def solution():
    n = int(input())
    nodes = [[] for _ in range(n+1)]
    parent_check = [False] * (n+1)
    for _ in range(n):
        i, p, q = list(map(int, input().split()))   # 현재 인덱스, 왼쪽, 오른쪽
        parent_check[p] = True
        parent_check[q] = True
        nodes[i] = [p, q, i, 0, 0]  # 왼쪽 자식, 오른쪽 자식, 자신, 깊이, 부모 노드

    # 최상단 찾기
    top_node = -1
    for i in range(1, n+1):
        if not parent_check[i]:
            top_node = i
            break

    # 깊이 딕셔너리 만들기
    # 키: 층 | 밸류: 층에 속한 번호
    visited = [False] * (n+1)
    stack = [nodes[top_node]]
    map_dict = {}
    while stack:
        l, r, i, d, p = stack.pop()
        for child in (l, r):
            depth = d + 1
            if child > 0:
                nodes[child][3] = depth
                nodes[child][4] = i
                stack.append(nodes[child])

            if not visited[i]:
                visited[i] = True
                try:
                    map_dict[depth].append(i)
                except:
                    map_dict[depth] = [i]

    second_visited = [False] * (n+1)
    stack = []

    # 해당 노드의 가장 최하단에 위치한 왼쪽 자식 찾기
    def find_start(idx):
        l, r, i, d, p = nodes[idx]
        if l == -1:
            return i
        else:
            return find_start(l)

    stack.append(find_start(top_node))

    # 1번부터 n번까지 x좌표 상의 리스트 만들기
    idx_arr = [-1] * (n+1)
    crnt_idx = 1
    while stack:
        l, r, here, d, parent = nodes[stack.pop()]
        second_visited[here] = True
        idx_arr[here] = crnt_idx
        crnt_idx += 1

        if parent > 0 and not second_visited[parent]:
            stack.append(parent)
        if r > 0 and not second_visited[r]:
            final_left = find_start(r)
            stack.append(final_left)

    answer = 0
    node_num = -1
    # 각 층별 순회, 가장 긴 구간 찾기
    for level in map_dict:
        far_left = float('inf')
        far_right = 0
        for elm in map_dict[level]:
            if idx_arr[elm] < far_left:
                far_left = idx_arr[elm]
            if idx_arr[elm] > far_right:
                far_right = idx_arr[elm]
        gap = far_right - far_left + 1
        if gap > answer:
            answer = gap
            node_num = level
            
    print(node_num, answer)

solution()