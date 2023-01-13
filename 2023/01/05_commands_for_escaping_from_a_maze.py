from collections import deque

# 미로를 탈출 할 수 있는지 판별하고, 가능한 경우 최소 이동거리 수와 이동경로를 반환하는 함수
def is_possible(n, m, k, queue, board, visited):
    def is_ok(a, b):
        if 0 <= a < n and 0 <= b < m:
            if not visited[a][b]:
                return True
        return False

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dd = ['r', 'd', 'l', 'u']

    while queue:
        p, q, steps, log = queue.popleft()
        steps += 1
        if steps > k:
            continue
 
        for i in range(4):
            np = p + dx[i]
            nq = q + dy[i]

            if is_ok(np, nq):

                if board[np][nq] == 'G':
                    if not (k - steps) % 2:
                        log = ''.join(sorted(f'{log}{dd[i]}'))
                        return [steps, log]
                    else:
                        return False

                visited[np][nq] = True
                queue.append([np, nq, steps, f'{log}{dd[i]}'])
    return False

# bfs를 통해 탈출 가능 여부를 확인
def bfs(n, m, x, y, r, c, k):
    board = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] * m for _ in range(n)]

    board[r][c] = 'G'
    queue = deque()
    queue.append([x, y, 0, ''])
    visited[x][y] = True

    return is_possible(n, m, k, queue, board, visited)

# bfs 결과를 통해 이동경로 정보를 재가공하는 함수
def refine_result_info(possible_result, k):
    # 필수 걸음 제외, 여유 걸음걸이 수
    remain_steps = k - possible_result[0]
    log = possible_result[1]

    d_cnt = 0
    l_cnt = 0
    r_cnt = 0
    u_cnt = 0
    for char in log:
        if char == 'd':
            d_cnt += 1
        elif char == 'l':
            l_cnt += 1
        elif char == 'r':
            r_cnt += 1
        elif char == 'u':
            u_cnt += 1

    result = {
        'remain_steps': remain_steps,
        'step_cnt_info': {
            'd_cnt': d_cnt,
            'l_cnt': l_cnt,
            'r_cnt': r_cnt,
            'u_cnt': u_cnt
        }
    }

    return result

def make_log(n, x, y, refined_info):
    remain_steps = refined_info['remain_steps']
    count_info = refined_info['step_cnt_info']

    # 골에 도착하기 위해 필수로 이동해야 하는 방향정보
    # 아래, 왼쪽, 오른쪽, 윗쪽 순서
    d_cnt = count_info['d_cnt']
    l_cnt = count_info['l_cnt']
    r_cnt = count_info['r_cnt']
    u_cnt = count_info['u_cnt']

    # 사전상 가장 빠른 경우 아래(d)
    # case 1. 하단 이동만으로 해결이 가능한 경우
    if n > (x + d_cnt + remain_steps) * 2:
        d_log = 'd' * (remain_steps // 2)
        u_log = 'u' * (remain_steps // 2)

        log = 'd' * d_cnt + d_log + 'l' * l_cnt + 'r' * r_cnt + 'u' * u_cnt + u_log

    # 그렇지 않은 경우 다른 방법 탐색
    else:
        # 아래 이동하는 경우를 미리 차감
        # 아래로 이동 후 위로 이동하는 경우도 포함하기 위해 미리 2를 곱해 차감
        # 해당 과정을 통해 현재 위치는 보드의 가장 최하단의 위치해 있는 상태
        remain_steps -= (n - (x + d_cnt + 1)) * 2

        # case 2. d 다음으로 빠른 l이 나오기 위한, 왼쪽으로 이동하는 경우
        if (y - l_cnt) * 2 > remain_steps:
            d_log = 'd' * (n - (x + d_cnt + 1))
            u_log = 'u' * (n - (x + d_cnt + 1))
            l_log = 'l' * (remain_steps // 2)
            r_log = 'r' * (remain_steps // 2)

            log = 'd' * (d_cnt) + d_log + 'l' * l_cnt + l_log + 'r' * r_cnt + r_log + 'u' * u_cnt + u_log

        else:
            # 최좌단으로 이동하는 과정
            remain_steps -= (y - l_cnt) * 2
            # 따라서 현재 위치는 보드의 최하단이자 최좌단

            # 현재 여유 걸음을 소모하며 사전상 가장 빠른 경우는 rl, 오른쪽 이동 후 왼쪽으로 이동하는 경우
            d_log = 'd' * (n - (x + d_cnt + 1))
            u_log = 'u' * (n - (x + d_cnt + 1))
            l_log = 'l' * (y - l_cnt)
            r_log = 'r' * (y - l_cnt)

            # 오른쪽 <-> 왼쪽 이동을 여유 걸음만큼 이동하며 필수 이동 걸음만 만을 때까지 이동할 수 있는 걸음 수를 소모
            rl_log = 'rl' * (remain_steps // 2)

            log = 'd' * (d_cnt) + d_log + 'l' * l_cnt + l_log + rl_log + 'r' * r_cnt + r_log + 'u' * u_cnt + u_log

    return log


# 격자크기, 출발위치, 탈출지점, 이동거리
def solution(n, m, x, y, r, c, k):
    x, y, r, c = x - 1, y - 1, r - 1, c - 1

    possible_result = bfs(n, m, x, y, r, c, k)

    if not possible_result:
        return 'impossible'

    # 미로 탈출이 가능한 경우, 해당 정보를 정제
    refined_info = refine_result_info(possible_result, k)

    # 정제된 정보를 통해 여유 걸음만큼 새로운 이동 추가하기
    log = make_log(n, x, y, refined_info)

    return log