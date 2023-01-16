import sys
sys.stdin = open("5178_input.txt", "r")

T = int(input())

for case in range(T):
    N, M, L = map(int, input().split(" "))

    tree = [0 for _ in range(N + 1)]

    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    for i in range(N, 0, -1):
        parent = i // 2
        tree[parent] += tree[i]

    print(f'#{case + 1} {tree[L]}')