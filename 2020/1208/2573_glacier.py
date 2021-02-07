import sys
sys.stdin = open('2573_input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]

switch = 1
trial = 0

while switch:
    switch = 0
    melting = []

    for i in range(N):
        for j in range(M):
            if jido[i][j]:

                cnt = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]

                    if jido[ni][nj] == 0:
                        cnt += 1

                melting.append([i, j, cnt])

    while melting:
        ci, cj, ccnt = melting.pop()
        jido[ci][cj] -= ccnt
        if jido[ci][cj] < 0:
            jido[ci][cj] = 0

    ctn_cnt = 0
    visited = [[False] * M for _ in range(N)]

    nflag = 0
    for i in range(N):
        if not nflag:
            for j in range(M):
                if jido[i][j] and not visited[i][j]:
                    stack = [[i, j]]
                    visited[i][j] = True

                    while stack:
                        ci, cj = stack.pop()

                        for k in range(4):
                            ni = ci + dx[k]
                            nj = cj + dy[k]

                            if jido[ni][nj] and not visited[ni][nj]:
                                visited[ni][nj] = True
                                stack.append([ni, nj])
                    ctn_cnt += 1

                    if ctn_cnt > 1:
                        nflag = 1
                        break
    trial += 1

    if ctn_cnt == 1:
        switch = 1
    elif ctn_cnt == 0:
        print('0')
    else:
        print(trial)