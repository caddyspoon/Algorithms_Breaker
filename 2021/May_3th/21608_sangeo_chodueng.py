import sys
sys.stdin = open('21608_input.txt', 'r')

def yeppuge(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print('{:2}'.format(arr[i][j]), end = ' ')
        print()


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def is_ok(x, y):
    return 0 <= x < N and 0 <= y < N


def plese_be_sitted(student_info, ban, sitted):
    student = student_info[0]
    their_loves = student_info[1:]
    max_score = [-1, -1, -1, -1]

    for i in range(N):
        for j in range(N):
            if not ban[i][j]:
                love_score = are_you_my_friend(i, j, their_loves, ban)
                if love_score[0] >= max_score[0]:
                    if love_score[0] > max_score[0]:
                        max_score = love_score[0], love_score[1], i, j
                    else:
                        if love_score[1] > max_score[1]:
                            max_score = love_score[0], love_score[1], i, j
    mv, mc, mi, mj = max_score
    ban[mi][mj] = student
    sitted[student] = [True, mv, their_loves]
    update_ban(mi, mj, student, ban, sitted)
    return
    

def are_you_my_friend(x, y, their_loves, ban):
    love_score = [0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if is_ok(nx, ny):
            if ban[nx][ny]:
                if ban[nx][ny] in their_loves:
                    if love_score[0] == 0: love_score[0] = 1
                    else: love_score[0] *= 10
            else:
                love_score[1] += 1
    return love_score


def update_ban(mi, mj, student, ban, sitted):
    for k in range(4):
        nmi = mi + dx[k]
        nmj = mj + dy[k]
        if is_ok(nmi, nmj):
            if ban[nmi][nmj]:
                if student in sitted[ban[nmi][nmj]][2]:
                    if sitted[ban[nmi][nmj]][1] == 0: sitted[ban[nmi][nmj]][1] = 1
                    else: sitted[ban[nmi][nmj]][1] *= 10
    return


def puli(students_info):
    sitted = [[False, 0]] * (N**2 + 1)

    ban = [[False] * N for _ in range(N)]
    ban[1][1] = students_info[0][0]
    sitted[students_info[0][0]] = [True, 0, students_info[0][1:]]

    for idx in range(1, len(students_info)):
        student_info = students_info[idx]
        plese_be_sitted(student_info, ban, sitted)
    
    score = 0
    yeppuge(ban)

    for elm in sitted:
        score += elm[1]
    return score


for case in range(1, int(input())+1):
    N = int(input())
    students_info = [list(map(int, input().split())) for _ in range(N**2)]
    print(puli(students_info))