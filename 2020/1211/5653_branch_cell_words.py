import sys
sys.stdin = open('5653_input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def is_wall(i, j):
    if 0 <= i < N and 0 <= j < M:
        return False
    return True


for case in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    pan = [list(map(int, input().split())) for _ in range(N)]

    from collections import deque

    info_pan = deque()
    for i in range(N):
        temp = deque()
        for j in range(M):
            if pan[i][j]:
                cell = [pan[i][j], 0, 'ready', 1]
            else:
                cell = [0, 0, 'blank', 1]
            temp.append(cell)
        info_pan.append(temp)

    def pprint(pan = pan):
        for i in range(N):
            for j in range(M):
                print(pan[i][j], end=' ')
            print()
        print()

    trial = 1

    i, j = 0, 0
    while trial < K + 1:

        # for l in range(N):
        #     for m in range(M):
        #         if info_pan[l][m][4]:
        #             info_pan[l][m][4] = False
                    # print(info_pan[l][m][4])

        while i < N:
            while j < M:

                # print('current: ', i, j)

                static, time, status, born = info_pan[i][j]
                # print('value:', static)
                # print()

                # 0이 아니며 활성 가능한 칸에 대해서 칸에 대해서
                if status == 'ready' or status == 'active':
                    time += 1

                    # 활성 상태
                    if static == time:
                        status = 'active'

                        for k in range(4):
                            ni = i + dx[k]
                            nj = j + dy[k]

                            # 0칸을 만들어 줄 필요가 있을 때
                            if is_wall(ni, nj):
                                # 네 방향에 대한 새로운 판을 만들어 줄 필요가 있음

                                # 오른쪽 칸이 추가될 때
                                if k == 0:
                                    for l in range(N):
                                        info_pan[l].append([0, 0, 'blank', trial])
                                    M += 1
                                    # print('k == 0')
                                    # pprint(info_pan)
                                    # print(info_pan)

                                # 아래 칸이 추가될 때
                                elif k == 1:
                                    new_row = deque()
                                    for _ in range(M):
                                        new_row.append([0, 0, 'blank', trial])
                                    info_pan.append(new_row)
                                    N += 1
                                    # print('k == 1')
                                    # pprint(info_pan)
                                    # print(info_pan)

                                # 왼쪽 칸이 추가될 때! 주의!
                                elif k == 2:

                                    for l in range(N):
                                        # print('problem here')
                                        # for a in info_pan:
                                            # print(a)
                                        # info_pan[l] = [[0, 0, 'blank', trial]] + info_pan[l]
                                        info_pan[l].appendleft([0, 0, 'blank', trial])
                                    M += 1
                                    j += 1
                                    nj = j + dy[k]

                                    # print('k == 2')
                                    # pprint(info_pan)
                                    # print(info_pan)
                                # 윗쪽 칸이 추가될 때! 주의!
                                elif k == 3:

                                    new_row = deque()
                                    # new_row.append([0, 0, 'blank', trial] for _ in range(M))
                                    for _ in range(M):
                                        new_row.append([0, 0, 'blank', trial])
                                    info_pan.appendleft(new_row)

                                    N += 1
                                    i += 1
                                    ni = i + dx[k]

                                    # print('k == 3')
                                    # pprint(info_pan)
                                    # print(info_pan)


                            # 빈 0이 만들어졌으므로 이제 처리를 해준다.
                            # print('here!', info_pan[ni][nj][2])
                            if info_pan[ni][nj][2] == 'new' and info_pan[ni][nj][0] < static and info_pan[ni][nj][3] == trial + 1:
                                info_pan[ni][nj][0] = static
                            elif not info_pan[ni][nj][0]:
                                info_pan[ni][nj] = [static, 0, 'new', trial + 1]

                    # 사망 상태
                    elif static * 2 == time:
                        status = 'dead'

                    # 이전 단계에서 새로 만들어진 세포를 활성화 상태로
                elif status == 'new' and born == trial:
                    status = 'ready'

                info_pan[i][j] = [static, time, status, born]

                j += 1

            i += 1
            j = 0

        # if case == 1:
        #     print('===========')
        #     print(trial, 'hour(s) after')
        #     for k in range(N):
        #         for l in range(M):
        #             if info_pan[k][l][0]:
        #                 print(info_pan[k][l][0], end=' ')
        #             else:
        #                 print(0, end=' ')
        #         print()
        #     print()
        #
        # if case == 1:
        #     print('Still Alive')
        #     for k in range(N):
        #         for l in range(M):
        #             if info_pan[k][l][2] == 'ready' or info_pan[k][l][2] == 'active':
        #                 if info_pan[k][l][2] == 'active':
        #                     print('*', info_pan[k][l][0], end=' ')
        #                 else:
        #                     print(info_pan[k][l][0], end=' ')
        #             else:
        #                 print(' ', end=' ')
        #         print()
        #     print()
        #
        #     print('status: ')
        #     for k in range(N):
        #         for l in range(M):
        #             if info_pan[k][l][2] == 'blank':
        #                 print('      ', end=' ')
        #             else:
        #                 print('{:6}'.format(info_pan[k][l][2]), end=' ')
        #         print()
        #     print()

        trial += 1
        i = 0
        j = 0

        # if case < 3:
        #     print('trial result')
        #     for l in range(N):
        #         for m in range(M):
        #             if info_pan[l][m][0]:
        #                 print(info_pan[l][m][0], end = ' ')
        #             else:
        #                 print(0, end = ' ')
        #         print()
        #     print()
        # if case < 3:
        #     print('================')

    # if case == 1:
    #     pprint(info_pan)

    # if case == 1:
    #     for i in range(N):
    #         for j in range(M):
    #             if info_pan[i][j][0]:
    #                 print(info_pan[i][j][0], end = ' ')
    #             else:
    #                 print(0, end = ' ')
    #         print()
    #     print()

    answer = 0
    for i in range(N):
        for j in range(M):
            static, time, status, born = info_pan[i][j]
            if status == 'ready' or status == 'active':
                answer += 1
    #             print(info_pan[i][j][0], end = ' ')
    #         else:
    #             print(0, end = ' ')
    #     print()
    # print()
    answer_sentence = '#{} {}'.format(case, answer)
    print(answer_sentence)