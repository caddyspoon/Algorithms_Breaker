def solution(n, info):
    answer = [-1]

    apc_point = 0
    for idx, i in enumerate(info):
        point = 10 - idx
        if i:
            apc_point += point
    # print('어피치 점수: ', apc_point)
    max_gap = 0

    init_arr = [0] * 11
    def dfs(arr, apc_point, l = n, crnt_point = 0, cnumber = 10):
        # print()
        # print('배열: ', arr, '남은 화살 수: ', l, '현재 점수: ', crnt_point, '현재 노리는 점수: ', cnumber)
        nonlocal answer, max_gap

        if l == 0 or cnumber <= 0:
            # print(arr)
            # print()
            crnt_gap = crnt_point - apc_point
            if crnt_gap > 0:
                temp_arr = arr[:]
                if l > 0:
                    temp_arr[10] = l
                # print("결과: ", arr, crnt_gap, crnt_point, apc_point)
                # print(crnt_gap, 'here')
                if max_gap < crnt_gap:
                    # print("최종 결과: ", arr, crnt_gap, crnt_point, apc_point)
                    max_gap = crnt_gap
                    answer = temp_arr[:]
                elif max_gap == crnt_gap:
                    for i in range(10, -1, -1):
                        if temp_arr[i] > answer[i]:
                            answer = temp_arr[:]
                            break
            return

        for i in range(cnumber, -1, -1):
            # print('case: 1 |', '현재 시작: ', i, arr, l, crnt_point)
            idx = 10 - i

            # 할 만한 가치가 있다면
            # 현재 투자할 값
            if i == 0:
                temp_arr = arr[:]
                temp_arr[10] = l
                dfs(temp_arr, apc_point, 0, crnt_point, i - 1)
                break
            # else:
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
            # print('현재 결과: ', temp_arr)
            # dfs(arr, l = n, crnt_point = 0, cnumber = 10)
            dfs(temp_arr, apc_point, l, crnt_point, i - 1)

            # 원상복귀
            l += info[idx] + 1
            crnt_point -= i
            if info[idx] > 0:
                apc_point += i
            # print('case: 2 |', l)

    dfs(init_arr, apc_point)
    # print('answer: ', answer)

    # if type(answer) != list:
    #
    # option 1.
    # result = []
    # order_standard = 0
    # for elm in answer[max_gap]:
    #     crnt_sum = 0
    #     for idx in range(11):
    #         if elm[idx]:
    #             crnt_sum += idx
    #     if crnt_sum > order_standard:
    #         order_standard = crnt_sum
    #         result = elm[:]
    # answer = result[:]

    # option 2.
    # temp_answer = []

    # for elm in answer[max_gap]:
    #     temp_sum = []
    #     for idx in range(10, -1, -1):
    #         temp_sum.append(elm[idx])
    #     temp_answer.append(temp_sum)

    # temp_answer.sort()

    # final_temp = []
    # for idx in range(10, -1, -1):
    #     final_temp.append(temp_answer[0][idx])
    # answer = final_temp[:]

    # option 3.
    # temp = [0] * 11
    # # print(answer[max_gap])
    # # print()
    # for elm in answer[max_gap]:
    #     for i in range(10, -1, -1):
    #         # print(temp[i], elm[i])
    #         if elm[i] > temp[i]:
    #             # print('here')
    #             # print(temp, elm)
    #             # print()
    #             temp = elm[:]
    #             break
    # answer = temp[:]
    return answer

n = 5
info = [0,2,2,0,1,0,0,0,0,0,0]

print(solution(n,info))