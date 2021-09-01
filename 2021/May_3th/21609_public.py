# import sys
# sys.stdin = open("21609_input.txt", "r")

import copy

def gravity(bayeol):
    for i in range(len(bayeol)-1, 0, -1):
        for j in range(len(bayeol[0])):
            if pan[i][j] == -2:
                for k in range(i-1, -1, -1):
                    if pan[k][j] == -1:
                        break
                    if pan[k][j] >= 0:
                        pan[i][j] = pan[k][j]
                        pan[k][j] = -2
                        break


def rotation(bayeol):
    global pan
    temp = [[-3]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = bayeol[j][N-1-i]
    pan = copy.deepcopy(temp)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def is_ok(x, y):
    return 0 <= x < N and 0 <= y < N


def dfs():
    global visited, score, enough
    
    game = 1
    
    wanna_check = False
    max_gaesu = 0
    max_mujigae = 0
    max_block_info = []

    min_hang = 0
    min_yeol = 0

    while game:
        gaesu = 0
        mujigae = 0
        block_info = []
        min_i = float('inf')
        min_j = float('inf')

        stack = []

        flag = 0
        cvisited = [[False] * N for _ in range(N)]
        
        for i in range(N):
            if flag == 0:
                for j in range(N):
                    if pan[i][j] >= 1:
                        if not visited[i][j]:
                            stack.append((i, j))
                            block_info.append([i, j])
                            visited[i][j] = True
                            cvisited[i][j] = True
                            flag = 1
                            color = pan[i][j]
                            break
                    if (i == N - 1) and (j == N - 1):
                        game = 0
                        break


        while stack:
            x, y = stack.pop()

            gaesu += 1
            if pan[x][y] == 0:
                mujigae += 1
            elif pan[x][y] >= 1:
                if x < min_i:
                    min_i, min_j = x, y
                elif x == min_i:
                    if y < min_j:
                        min_i, min_j = x, y

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                # print('This should be nx and ny', nx, ny)
                if is_ok(nx, ny):
                    if pan[nx][ny] == color or pan[nx][ny] == 0:
                        if cvisited[nx][ny] == False:
                            cvisited[nx][ny] = True
                            
                            if pan[nx][ny] > 0:
                                visited[nx][ny] = True
                            
                            stack.append((nx, ny))
                            block_info.append([nx, ny])

        '''
        크기가 가장 큰 블록 그룹을 찾는다. 
        그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 
        그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그것도 여러개이면 열이 가장 큰 것을 찾는다.
        '''

        if not wanna_check:
            max_gaesu = gaesu
            max_mujigae = mujigae
            max_block_info = copy.deepcopy(block_info)
            max_hang = min_i
            max_yeol = min_j

            wanna_check = True

        else:
            if gaesu > max_gaesu:
                max_gaesu = gaesu
                max_mujigae = mujigae
                max_block_info = copy.deepcopy(block_info)
                max_hang = min_i
                max_yeol = min_j
                
            elif gaesu == max_gaesu:
                if mujigae > max_mujigae:
                    max_mujigae = mujigae
                    max_block_info = copy.deepcopy(block_info)
                    max_hang = min_i
                    max_yeol = min_j
                
                elif max_mujigae == mujigae:
                    if min_i > max_hang:
                        max_block_info = copy.deepcopy(block_info)
                        max_hang = min_i
                        max_yeol = min_j
                    
                    elif min_i == max_hang:
                        if min_j > max_yeol:
                            max_block_info = copy.deepcopy(block_info)
                            max_yeol = min_j
    if max_gaesu < 2:
        enough = True
        return
        
    for x, y in max_block_info:
        pan[x][y] = -2
    score += max_gaesu ** 2

    return

N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

lets_go = True
score = 0
enough = False
while lets_go:
    lets_go = False
    visited = [[False] * N for _ in range(N)]
    dfs()
    gravity(pan)
    rotation(pan)
    gravity(pan)
    for i in range(N):
        for j in range(N):
            if not enough:
                if pan[i][j] >= 0:
                    lets_go = True
print(score)