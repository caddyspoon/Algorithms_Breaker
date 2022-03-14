def solution(n, info):
    answer = [-1]

    apc_point = 0
    for idx, i in enumerate(info):
        point = 10 - idx
        if i:
            # 어피치 점수
            apc_point += point
    # 점수 차이 저장
    max_gap = 0

    init_arr = [0] * 11
    answer_arr = []
    def dfs(arr, apc_point, l = n, crnt_point = 0, cnumber = 10):
        # print('배열: ', arr, '남은 화살 수: ', l, '현재 점수: ', crnt_point, '현재 노리는 점수: ', cnumber)
        nonlocal answer, max_gap, answer_arr

        if l == 0 or cnumber <= 0:
            crnt_gap = crnt_point - apc_point
            if crnt_gap > 0:
                temp_arr = arr[:]
                if l > 0:
                    temp_arr[10] = l
                if max_gap < crnt_gap:
                    max_gap = crnt_gap
                    answer_arr = [temp_arr[:]]
                elif max_gap == crnt_gap:
                    answer_arr.append(temp_arr[:])
            return

        for i in range(cnumber, -1, -1):
            idx = 10 - i

            if i == 0:
                temp_arr = arr[:]
                temp_arr[10] = l
                dfs(temp_arr, apc_point, 0, crnt_point, i - 1)
                break
            l -= info[idx] + 1

            if l < 0:
                temp_arr = arr[:]
                l += info[idx] + 1
                dfs(temp_arr, apc_point, l, crnt_point, i - 1)
                continue

            crnt_point += i

            if info[idx] > 0:
                apc_point -= i

            temp_arr = arr[:]
            temp_arr[idx] = info[idx] + 1
            dfs(temp_arr, apc_point, l, crnt_point, i - 1)

            # 원상복귀
            l += info[idx] + 1
            crnt_point -= i
            if info[idx] > 0:
                apc_point += i

    dfs(init_arr, apc_point)
    if answer_arr:
        temp_answer = [0] * 11
        for elm in answer_arr:
            for i in range(len(elm)-1, -1, -1):
                if temp_answer[i] > elm[i]:
                    break
                if temp_answer[i] < elm[i]:
                    temp_answer = elm[:]
                    break

        answer = temp_answer[:]
    return answer

# Test Case
n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]

print(solution(n,info))