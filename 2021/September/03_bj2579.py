import sys
sys.stdin = open("bj2579_input.txt", "r")

n = int(input())
stairs = []

for _ in range(n):
    stairs.append(int(input()))

def solution(n, stairs):
    if n <= 2:
        return sum(stairs)

    dp = [[0, 0] for _ in range(n)]

    dp[0][1] = stairs[0]

    dp[1][0] = stairs[0] + stairs[1]
    dp[1][1] = stairs[1]

    for i in range(2, n):
        dp[i][1] += max(dp[i-2][0], dp[i-2][1]) + stairs[i]
        dp[i][0] += dp[i-1][1] + stairs[i]

    return max(dp[n-1][0], dp[n-1][1])

print(solution(n, stairs))