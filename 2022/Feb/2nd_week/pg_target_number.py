
def solution(numbers, target):
    answer = 0

    def dfs(n, num):
        nonlocal answer
        if n == len(numbers):
            if num == target:
                answer += 1
            return
        dfs(n+1, num+numbers[n])
        dfs(n+1, num-numbers[n])

    dfs(0, 0)
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
target_answer = 5

print(solution(numbers, target))