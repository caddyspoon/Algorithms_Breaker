import sys
sys.stdin = open('dfs_input.txt', 'r')

x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = [list(map(int, input().split())) for _ in range(x)]

def pprint(arr):
    for i in range(x):
        for j in range(y):
            print(arr[i][j], end=' ')
        print()
    print()

start = []

flag = False
for i in range(x):
    for j in range(y):
        if arr[i][j] == 2:
            start = [i, j]
            flag = True
            break
    if flag:
        break

stack = [start]

visited = [[False] * x for _ in range(y)]

answer = []

nflag = False
while stack:
    p, q = stack.pop()
    arr[p][q] = 'S'
    for i in range(4):
        nx = p + dx[i]
        ny = q + dy[i]

        # 갈 수 있는지 (인덱스 상으로)
        if 0 <= nx < x and 0 <= ny < y:
            # 길인지
            if arr[nx][ny] != 1:
                # 방문한 적이 없는 곳인지
                if visited[nx][ny] == False:
                    arr[nx][ny] = 'X'
                    pprint(arr)
                    if arr[nx][ny] == 3:
                        answer = [nx, ny]
                        nflag = True
                        break
                    stack.append([nx, ny])
                    visited[nx][ny] = True

    if nflag == True:
        break

print(answer)