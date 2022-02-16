def solution(n):
    N = int(input())
    arr = {1: 0, 2: 1, 3: 1}

    for i in range(2, N+1):
        arr[i] = arr[i-1] + 1
        if i % 2 == 0:
            arr[i] = min(arr[i], arr[i//2] + 1)
        if i % 3 == 0:
            arr[i] = min(arr[i], arr[i//3] + 1)

    return arr[N]

print(solution(10))
