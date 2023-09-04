def solution(user_id, banned_id):
    answer = []

    init_visited = [False] * len(banned_id)

    banned_case = set()

    def is_possible(user, bully):
        if len(user) != len(bully):
            return False
        
        for i in range(len(user)):
            if bully[i] == '*':
                continue
            elif user[i] != bully[i]:
                return False
        else:
            return True

    def find_user_id(visited=init_visited, idx=0, bannded_info=[]):
        # print(visited, idx, bannded_info)
        if idx == len(user_id):
            if sum(visited) == len(visited):
                banned_case.add('|'.join(bannded_info))
            return
        
        crnt_id = user_id[idx]
        for crnt_idx, crnt_banned_id in enumerate(banned_id):
            if not visited[crnt_idx] and is_possible(crnt_id, crnt_banned_id):
                visited[crnt_idx] = True
                bannded_info.append(crnt_id)
                find_user_id(visited, idx+1, bannded_info)

                visited[crnt_idx] = False
                bannded_info.pop()
        else:
            find_user_id(visited, idx+1, bannded_info)

    find_user_id()

    return len(banned_case)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]

print(solution(user_id, banned_id))