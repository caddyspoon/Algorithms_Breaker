import sys
sys.stdin = open("5176_input.txt", "r")

T = int(input())
for case in range(T):
    N = int(input())

    # 빈 트리 만들기
    tree = [None for _ in range(N + 1)]

    search_order = []
    # 중위탐색
    def mid_search(node = 1):
        global search_order

        if (node * 2) <= N:
            mid_search(node * 2)
        search_order.append(node)
        if (node * 2 + 1) <= N:
            mid_search(node * 2 + 1)

    mid_search()

    for value, idx in enumerate(search_order):
        tree[idx] = value + 1

    print(f'#{case + 1} {tree[1]} {tree[N//2]}')