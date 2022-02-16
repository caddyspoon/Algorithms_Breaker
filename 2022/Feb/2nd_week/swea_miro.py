import sys
sys.stdin = open('miro_input.txt', 'r')

def pprint(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end = ' ')
        print()
    print()

def find_start(arr):
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                return [i, j]

def is_wall(x, y):
    if arr[x][y]:
        return True
    return False

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(int(input())):
    case_no = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    visited = [[False] * 16 for _ in range(16)]
    start = find_start(arr)
    stack = [start]
    visited[start[0]][start[1]] = True
    answer = 0

    flag = False
    while stack:
        if flag: break

        p, q = stack.pop()
        for i in range(4):
            np = p + dx[i]
            nq = q + dy[i]

            if arr[np][nq] == 3:
                answer = 1
                flag = True
                break

            if not is_wall(np, nq):
                if not visited[np][nq]:
                    stack.append([np, nq])
                    visited[np][nq] = True

    print(answer)