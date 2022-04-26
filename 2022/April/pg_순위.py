def solution(n, results):
    answer = 0

    graph = [[set(), set()] for _ in range(n+1)]

    for winner, loser in results:
        graph[winner][1].add(loser)
        graph[loser][0].add(winner)

    for win_info, lose_info in graph:
        for winner in win_info:
            graph[winner][1].update(lose_info)

        for loser in lose_info:
            graph[loser][0].update(win_info)

    for i in range(1, n+1):
        if len(graph[i][0]) + len(graph[i][1]) == n-1:
            answer += 1

    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
result = 2

print(solution(n, results) == result)