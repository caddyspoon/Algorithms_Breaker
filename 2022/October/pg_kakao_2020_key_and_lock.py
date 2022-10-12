from copy import deepcopy

def solution(key, lock):
    N = len(key)
    M = len(lock)

#     def is_opened():
#         for i in range(M):
#             for j in range(M):
#                 if lock[i][j] == 0:
#                     return False
#         return True

#     if is_opened():
#         return True

    new_lock = [[0] * ((N-1)*2 + M) for _ in range((N-1)*2 + M)]

    temp_cnt = 0
    for i in range(M):
        ni = i + N-1
        for j in range(M):
            nj = j + N - 1
            new_lock[ni][nj] = lock[i][j]
            if lock[i][j] == 1:
                temp_cnt += 1

    if temp_cnt == M**2:
        return True

    # clockwise
    def turn_key(key_arr):
        M = len(key_arr)
        new_key = [[0] * M for _ in range(M)]
        for i in range(M):
            for j in range(M):
                new_key[j][abs((M - 1) - i)] = key_arr[i][j]

                """
                0 0 -> 0 2
                1 0 -> 0 1
                2 0 -> 0 0

                0 1 -> 1 2
                1 1 -> 1 1
                2 1 -> 1 0
                """
        return new_key


    def is_complited(lock_arr):
        for i in range(M):
            ni = i + N - 1
            for j in range(M):
                nj = j + N - 1
                if lock_arr[ni][nj] == 0:
                    return False
        return True


    def pprint(arr):
        l = len(arr)
        for i in range(l):
            for j in range(l):
                print(arr[i][j], end=' ')
            print()
        print()

    for i in range(M+N-1):
        for j in range(M+N-1):
            for _ in range(4):
                temp_map = deepcopy(new_lock)

                flag = False
                for l in range(N):
                    ni = l + i
                    if flag:
                        break
                    for m in range(N):
                        nj = m + j
                        if temp_map[ni][nj] == 0 and key[l][m] == 1:
                            temp_map[ni][nj] = key[l][m]
                        elif temp_map[ni][nj] == 1 and key[l][m] == 1:
                            flag = True
                            break

                if is_complited(temp_map) and not flag:
                    return True
                key = turn_key(key)

    return False