def solution(n, results):
    answer = 0

    info = {}
    arr = []
    for i in range(n+1):
        info[i] = []
        arr.append([0, 0, 0, i])


    for a, b in results:
        arr[a][0] += 1
        arr[a][1] += 1

        arr[b][0] += 1
        arr[b][2] += 1

    arr.sort(reverse=True)
    print(arr)


    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
result = 2

print(solution(n, results) == result)