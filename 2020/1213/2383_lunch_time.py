import sys
sys.stdin = open('2383_input.txt', 'r')

def time_by_walk(person, stair):
    return abs(person[0] - stair[0]) + abs(person[1] - stair[1])

def time_for_stair(people, stair):
    q = []
    while people:
        person = people.pop(0)
        walk_time = time_by_walk(person, stair)
        q.append(walk_time)
    return q

def gyedan_select(saram):
    global answer

    from itertools import combinations
    # 어느 계단으로 분배할지 사람들을 나누기

    for i in range(len(saram) + 1):
        comb_list = combinations(range(len(saram)), i)
        for idx in comb_list:
            import copy
            # 첫 번째 계단으로 갈 사람들
            temp_1 = copy.deepcopy(saram)
            # 두 번째 계단으로 갈 사람들
            temp_2 = []

            this_answer = float('inf')

            flag = 0

            for j in idx:
                temp_2.append(saram[j])
                temp_1.remove(saram[j])
            # print('temp_1: ', temp_1)
            # print('temp_2: ', temp_2)
            # print('===================')
            q1 = sorted(time_for_stair(temp_1, gyedan[0]))
            q2 = sorted(time_for_stair(temp_2, gyedan[1]))

            # print(q1)
            # print(q2)
            q1_answer = 0
            if q1:
                t1_s = 0
                # 다 내려가야 하는 사람 수
                t1_goal = len(q1)
                # 다 내려간 사람 수
                t1_done = 0
                # 데이터 조견표
                t1_status = [False] * t1_goal
                # 현재 시간
                crnt_1 = q1[0]
                # 계단
                st_1 = [[] for _ in range(3)]
                while t1_done != t1_goal:
                    # print(t1_status)
                    # 계단에 있던 얘들 내려가고 내보내기
                    for j in range(3):
                        if st_1[j]:
                            st_1[j][1] += 1
                            # 계단 걸리는 시간만큼 있었으면 다 온 것
                            if st_1[j][1] == gyedan[0][2]:
                                # 나가
                                st_1[j] = []
                                t1_done += 1

                                if t1_done == t1_goal:
                                    break

                    # 아무튼 계단에 넣기
                    for j in range(t1_s, t1_goal):
                        if q1[j] <= crnt_1 and not t1_status[j]:
                            # 세 명까지 되니까 아무튼 넣기
                            for k in range(3):
                                if not st_1[k]:
                                    st_1[k] = [q1[j], 0]
                                    t1_status[j] = True
                                    t1_s = j
                                    break

                    # 시간 보내기
                    crnt_1 += 1
                    if crnt_1 > answer:
                        flag = 1
                        break
                # print('q1의 최종 걸린 시간은: ', crnt_1)
                q1_answer = crnt_1

            if flag:
                continue

            q2_answer = 0
            if q2:
                t2_s = 0
                # 다 내려가야 하는 사람 수
                t2_goal = len(q2)
                # 다 내려간 사람 수
                t2_done = 0
                # 데이터 조견표
                t2_status = [False] * t2_goal
                # 현재 시간
                crnt_2 = q2[0]
                # 계단
                st_2 = [[] for _ in range(3)]
                while t2_done != t2_goal:
                    # print(t2_status)
                    # 계단에 있던 얘들 내려가고 내보내기
                    for j in range(3):
                        if st_2[j]:
                            st_2[j][1] += 1
                            # 계단 걸리는 시간만큼 있었으면 다 온 것
                            if st_2[j][1] == gyedan[1][2]:
                                # 나가
                                st_2[j] = []
                                t2_done += 1
                                if t2_done == t2_goal:
                                    break

                    # 아무튼 계단에 넣기
                    for j in range(t2_s, t2_goal):
                        if q2[j] <= crnt_2 and not t2_status[j]:
                            # 세 명까지 되니까 아무튼 넣기
                            for k in range(3):
                                if not st_2[k]:
                                    st_2[k] = [q2[j], 0]
                                    t2_status[j] = True
                                    t2_s = j
                                    break
                    # 시간 보내기
                    crnt_2 += 1
                    if crnt_2 > answer:
                        flag = 1
                        break
                # print('q2 최종 걸린 시간은: ', crnt_2)
                q2_answer = crnt_2

            if flag:
                continue

            if q1_answer > q2_answer:
                this_answer = q1_answer
            else:
                this_answer = q2_answer

            if this_answer < answer:
                answer = this_answer
    return

for case in range(1, int(input()) + 1):
    N = int(input())
    bang = [list(map(int, input().split())) for _ in range(N)]

    saram = []
    gyedan = []
    for i in range(N):
        for j in range(N):
            if bang[i][j]:
                if bang[i][j] == 1:
                    saram.append([i, j])
                else:
                    gyedan.append([i, j, bang[i][j]])

    answer = float('inf')
    gyedan_select(saram)
    print('#{} {}'.format(case, answer))