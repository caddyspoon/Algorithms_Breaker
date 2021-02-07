import sys
sys.stdin = open('2606_input.txt', 'r')

N = int(input())
ganseon = int(input())

glist = [list(map(int, input().split())) for _ in range(ganseon)]

stack = [1]
visited = [False] * (N + 1)
visited[1] = True

answer = 0

while stack:
    cnum = stack.pop()
    answer += 1
    for x, y in glist:
        if x == cnum:
            if not visited[y]:
                visited[y] = True
                stack.append(y)
        elif y == cnum:
            if not visited[x]:
                visited[x] = True
                stack.append(x)

print(answer - 1)