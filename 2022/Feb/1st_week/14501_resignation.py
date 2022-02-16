import sys
sys.stdin = open('14501_input.txt', 'r')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * n  # 당일 저녁에 정산을 한다고 생각해보자
for i in range(n):
    d, p = arr[i]
    end_day = i + d - 1
    try:
        if i > 0:
            p += max(dp[:i])
        dp[end_day] = max(dp[end_day], p)
    except: continue
    print(dp)

print(max(dp))