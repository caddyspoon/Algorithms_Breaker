def solution(begin, target, words):
    init_visited = [False] * len(words)

    min_trial = float('inf')

    def is_changable(a, b):
        cnt = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                cnt += 1

            if cnt > 1:
                return False

        if cnt == 1:
            return True

        return False


    def dfs(crnt=begin, visited=init_visited, cnt=0):
        nonlocal min_trial

        if crnt == target or sum(init_visited) == len(words):
            if crnt == target and cnt < min_trial:
                min_trial = cnt
            return

        for i in range(len(words)):
            if visited[i]:
                continue

            this_word = words[i]
            if is_changable(crnt, this_word):
                visited[i] = True
                dfs(this_word, visited, cnt + 1)

                visited[i] = False

    dfs()

    if min_trial == float('inf'):
        return 0
    else:
        return min_trial