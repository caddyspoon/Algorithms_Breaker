def solution(n):
    pyramid = []

    for i in range(n):
        crnt_row = [0] * (i + 1)
        pyramid.append(crnt_row)

    cnt = 1
    total_cnt = n * (n+1) // 2
    trial = 0

    while cnt <= total_cnt:
        for idx, arr in enumerate(pyramid):
            if trial < len(arr) and not arr[trial]:
                arr[trial] = cnt
                cnt += 1

            if idx == (n - 1) - trial:
                for i in range(trial + 1, len(arr) - 1):
                    if not arr[i]:
                        arr[i] = cnt
                        cnt += 1

        for arr_idx in range(len(pyramid) - 1, -1, -1):
            if len(pyramid[arr_idx]) - 1 > trial and not pyramid[arr_idx][-(1+trial)]:
                pyramid[arr_idx][-(1+trial)] = cnt
                cnt += 1

        trial += 1

    answer = []
    for arr in pyramid:
        for elm in arr:
            answer.append(elm)

    return answer