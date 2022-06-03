import sys
sys.stdin = open('input_bj2110.txt', 'r')

def solution():
    N, C = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    arr.sort()

    start = 1
    end = arr[N-1] - arr[0]
    crnt_gap = 0

    while start <= end:
        distance = (start+end) // 2
        route_cnt = 1
        last_route = arr[0]

        # 해당 거리로 모든 공유기를 설치할 수 있는지 확인
        for i in range(1, N):
            crnt_v = arr[i]
            if crnt_v >= last_route + distance:
                route_cnt += 1
                last_route = crnt_v

        if route_cnt >= C:
            start = distance + 1
            if crnt_gap < distance:
                crnt_gap = distance
        else:
            end = distance - 1

    return crnt_gap

print(solution())