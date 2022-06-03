import heapq

def solution(jobs):
    answer = 0
    l = len(jobs)

    jobs.sort()

    works = []

    now = jobs[0][0]
    total = 0

    while len(jobs) != 0 or len(works) != 0:
        while True:
            if jobs:
                time, work = jobs.pop(0)
                if time <= now:
                    heapq.heappush(works, [work, time])
                else:
                    jobs.insert(0, [time, work])
                    break
            else:
                break

        if len(works) > 0:
            work, time = heapq.heappop(works)
            total += now - time + work
            now += work
        else:
            now = jobs[0][0]

    return total // l


jobs = [[0, 3], [1, 9], [2, 6], [3, 1], [6, 2], [8, 7], [10, 5]]    # 10
# jobs = [[0, 3], [1, 9], [2, 6]]   # 9
# jobs = [[0, 5], [2, 10], [10000, 2]] # 6
# jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]    # 72
print('answer: ', solution(jobs))