import sys
sys.stdin = open('2683_input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
trial = 0

switch = 1

while switch:

    switch = 0
    melting = []

    for i in range(N):
        for j in range(M):
            if pan[i][j]:
                switch = 1
                starts = []
                # 시작점 찾기
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]

                    if not pan[ni][nj]:
                        starts.append([ni, nj])

                if len(starts) >= 2:
                    cnt = 0
                    while starts:
                        si, sj = starts.pop()
                        visited = [[False] * M for _ in range(N)]
                        visited[si][sj] = True
                        stack = [[si, sj]]

                        flag = 0
                        while stack and not flag:
                            ci, cj = stack.pop()

                            if ci == 0 or ci == N - 1 or cj == 0 or cj == M - 1:
                                cnt += 1
                                break

                            for k in range(4):
                                ni = ci + dx[k]
                                nj = cj + dy[k]

                                if ni == 0 or ni == N - 1 or nj == 0 or nj == M - 1:
                                    cnt += 1
                                    flag = 1

                                elif pan[ni][nj] == 0 and not visited[ni][nj]:
                                    visited[ni][nj] = True
                                    stack.append([ni, nj])

                        if cnt >= 2:
                            melting.append([i, j])
                            break
    if melting:
        trial += 1

        while melting:
            mi, mj = melting.pop()
            pan[mi][mj] = 0

print(trial)