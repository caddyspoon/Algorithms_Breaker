def permutation(a, result, visited, cnt = 0):
    if 2 == cnt:
        print(result)
        print(result - a)
        return

    for i in range(len(a)):
        if not visited[i]:
            result.append(a[i])
            visited[i] = True
            permutation(a, result, visited, cnt + 1)
            visited[i] = False
            result.pop()

a = [1, 2, 3, 4, 5, 6]
result = []
visited = [False] * len(a)
permutation(a, result, visited)