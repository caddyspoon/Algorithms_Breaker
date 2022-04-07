from heapq import heappush, heappop

def solution(n, times):
    answer = 0

    l = len(times)
    max_time = e = max(times) * (n // l + 1)
    s = 0
    t = 0

    work = [0] * l
    while True:
        t = (s+e) // 2
        crnt_time = 0
        done = 0


        stack = []
        for i in range(l):
            if work[i] <= crnt_time:
                heappush(stack, [times[i], i])

        while stack and done < n:
            work_time, idx = heappop(stack)
            work[idx] = crnt_time + work_time
            done += 1

        # 아직 done이 n이 아니면
        crnt_time += t


    return answer

n = 6
times = [7, 10]
result = 28

print(solution(n, times))