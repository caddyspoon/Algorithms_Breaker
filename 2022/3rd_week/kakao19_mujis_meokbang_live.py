import heapq
def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    
    works = []
    for idx, elm in enumerate(food_times):
        heapq.heappush(works, [elm, idx])
    
    last_food = 0 # 지난 음식
    while k >= (works[0][0] - last_food) * len(works):
        l = len(works)
        crnt_food = heapq.heappop(works)[0]
        if last_food < crnt_food:
            k -= (crnt_food - last_food) * l
        last_food = crnt_food
    works.sort(key = lambda x: (x[1]))

    if k > 0 and len(works) > 0:
        k = k % len(works)
    
    return works[k][1] + 1

food_times = [[3, 1, 2], [1, 1, 1, 1, 1, 1], [3, 3, 3, 3], [1, 100], [3,1,1,1,2,4,3]]
k = [5, 4, 5, 10, 12]
result = [1, 5, 2, 2, 6]


for trial in range(len(food_times)):
    my_answer = solution(food_times[trial], k[trial])
    print(my_answer, my_answer == result[trial])
    print()