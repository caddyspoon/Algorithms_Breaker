import sys
sys.stdin = open("21609_input.txt", "r")

import copy

def yeppuge(bayeol):
    for i in range(len(bayeol)):
        for j in range(len(bayeol[0])):
            if bayeol[i][j] == -2:
                print(' *', end=' ')
            else:
                print(f'{bayeol[i][j]:2}', end=' ')
        print()
    print()


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

'''
00 01 02 03 04
10 11 12 13 14
20 21 22 23 24
30 31 32 33 34
40 41 42 43 44

04 14 24 34 44
03 13 23 33 43
02 12 22 32 42
'''

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
            # print('We alwasy wanted Bigger i', i)
            if flag == 0:
                for j in range(N):
                    # print('...and j too', j)
                    if pan[i][j] >= 1:
                        if not visited[i][j]:
                            # if pan[i][j] == 3:
                            #     print('start: ', i, j)
                            stack.append((i, j))
                            block_info.append([i, j])
                            visited[i][j] = True
                            cvisited[i][j] = True
                            flag = 1
                            color = pan[i][j]
                            break
                    if (i == N - 1) and (j == N - 1):
                        game = 0
                        # print(stack, 'Dont do this for me...')
                        break

        # print('We start here...', stack)
        # print('This is the origin visited', visited)
        while stack:
            # print('In progress', stack)
            x, y = stack.pop()
            # print('...And color is ', color)

            gaesu += 1
            if pan[x][y] == 0:
                mujigae += 1
            elif pan[x][y] >= 1:
                if y < min_j:
                    min_i, min_j = x, y
                elif y == min_j:
                    if x < min_i:
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


                    # print('And qualified one is', nx, ny)
                    # if pan[nx][ny] == -1:
                    #     continue

                    # if pan[nx][ny] >= 1:
                    #     if color != pan[nx][ny]:
                    #         continue

                    # if cvisited[nx][ny]:
                    #     continue

                    # cvisited[nx][ny] = True
                    # # elif pan[nx][ny] == 0:
                    # #     mujigae += 1

                    # stack.append((nx, ny))
                    # # print(stack, 'Stack!')
                    # block_info.append([nx, ny])

        # print('이번 블록 개수', gaesu)

        '''
        크기가 가장 큰 블록 그룹을 찾는다. 
        그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 
        그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그것도 여러개이면 열이 가장 큰 것을 찾는다.
        '''
        # print('Please get here')

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
                    max_gaesu = gaesu
                    max_mujigae = mujigae
                    max_block_info = copy.deepcopy(block_info)
                    max_hang = min_j
                    max_yeol = min_i
                
                elif max_mujigae == mujigae:
                    if min_i > max_hang:
                        max_gaesu = gaesu
                        max_mujigae = mujigae
                        max_block_info = copy.deepcopy(block_info)
                        max_hang = min_i
                        max_yeol = min_j
                    
                    elif min_i == max_hang:
                        if min_j > max_yeol:
                            max_gaesu = gaesu
                            max_mujigae = mujigae
                            max_block_info = copy.deepcopy(block_info)
                            max_hang = min_i
                            max_yeol = min_j
    if max_gaesu < 2:
        enough = True
        return
        # print('This is the end of the step')
        # print(visited)
        # print('info ', block_info)
        
    # print(max_block_info)

    for x, y in max_block_info:
        pan[x][y] = -2
        # print('Do you get here')
    score += max_gaesu ** 2

    return print('이번 퍼즐 점수', max_gaesu)

for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    pan = [list(map(int, input().split())) for _ in range(N)]

    lets_go = True
    score = 0
    enough = False
    # if case == 1:
    while lets_go:
        lets_go = False
        visited = [[False] * N for _ in range(N)]

        print('Ready')
        yeppuge(pan)
        dfs()
        print()
        print('Done')
        yeppuge(pan)
        print('1st gravity')
        gravity(pan)
        yeppuge(pan)

        print('rotation')
        rotation(pan)
        yeppuge(pan)

        print('2nd gravitys')
        gravity(pan)
        yeppuge(pan)
        # break
        print('current score: ', score)
        for i in range(N):
            for j in range(N):
                if not enough:
                    if pan[i][j] >= 0:
                        lets_go = True
    print('Final scroe: ', score)
    print('=====================')
