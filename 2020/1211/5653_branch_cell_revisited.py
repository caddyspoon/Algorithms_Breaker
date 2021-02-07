import sys
sys.stdin = open('5653_input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for case in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    pan = [list(map(int, input().split())) for _ in range(N)]

    info_pan = []

    for _ in range(350):
        temp = []
        for _ in range(350):
            cell = [0, 0, False, False, 1]
            temp.append(cell)
        info_pan.append(temp)

    for i in range(N):
        for j in range(M):
            if pan[i][j]:
                info_pan[150 + i][150 + j] = [pan[i][j], 0, False, False, 1]

    trial = 1

    si = 150
    sj = 150

    ei = N + 150
    ej = M + 150

    while trial < K + 1:
        # for l in range(N):
        #     for m in range(M):
        #         if info_pan[l][m][4]:
        #             info_pan[l][m][4] = False
                    # print(info_pan[l][m][4])
        i = si
        j = sj

        while i <= ei:
            while j <= ej:
                static, time, dead, new, born = info_pan[i][j]

                if dead or not static:
                    j += 1
                    continue

                # 활성 가능한 칸에 대해서 칸에 대해서
                if not new:
                    time += 1

                    # 활성 상태
                    if static == time:
                        for k in range(4):
                            ni = i + dx[k]
                            nj = j + dy[k]

                            if k % 2:
                                if ni < si:
                                    si = ni
                                elif ni > ei:
                                    ei = ni
                            else:
                                if nj < sj:
                                    sj = nj
                                elif nj > ej:
                                    ej = nj

                            if not info_pan[ni][nj][0]:
                                info_pan[ni][nj] = [static, 0, False, True, trial + 1]
                            elif info_pan[ni][nj][0] < static and info_pan[ni][nj][4] == trial + 1:
                                    info_pan[ni][nj][0] = static

                    # 사망 상태
                    elif static * 2 == time:
                        dead = True

                # 이전 단계에서 새로 만들어진 세포를 활성화 상태로
                elif new and born == trial:
                    new = False

                info_pan[i][j] = [static, time, dead, new, born]
                j += 1

            i += 1
            j = sj

        # if case == 1:
        #     print('===========')
        #     print(trial, 'hour(s) after')
        #     for k in range(si, ei+1):
        #         for l in range(sj, ej+1):
        #             if info_pan[k][l][0]:
        #                 print(info_pan[k][l][0], end=' ')
        #             else:
        #                 print(0, end=' ')
        #         print()
        #     print()

        # if case == 1:
        #     print('Still Alive')
        #     for k in range(si, ei+1):
        #         for l in range(sj, ej+1):
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
        i = si
        j = sj

    answer = 0
    for x in range(si, ei + 1):
        for y in range(sj, ej + 1):
            static, time, dead, new, born = info_pan[x][y]

            if dead or not static or new:
                continue

            answer += 1

    answer_sentence = '#{} {}'.format(case, answer)
    print(answer_sentence)