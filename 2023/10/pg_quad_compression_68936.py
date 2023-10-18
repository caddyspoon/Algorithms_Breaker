def solution(arr):
    def is_compressible(i_start, j_start, crnt_l):
        nonlocal arr

        i_end = i_start + crnt_l
        j_end = j_start + crnt_l

        standard_value = arr[i_start][j_start]

        for i in range(i_start, i_end):
            for j in range(j_start, j_end):
                if arr[i][j] != standard_value:
                    return False

        return True


    def paint_char(i_start, j_start, crnt_l):
        nonlocal arr

        for i in range(i_start, i_start + crnt_l):
            for j in range(j_start, j_start + crnt_l):
                arr[i][j] = None
    

    answer = [0, 0]

    l = len(arr[0])
    crnt_l = l

    while crnt_l > 1:
        crnt_i_s = 0
        crnt_j_s = 0

        while crnt_i_s < l:
            if type(arr[crnt_i_s][crnt_j_s]) == int:
                if is_compressible(crnt_i_s, crnt_j_s, crnt_l):
                    if arr[crnt_i_s][crnt_j_s] == 0:
                        answer[0] += 1
                    else:
                        answer[1] += 1
                    paint_char(crnt_i_s, crnt_j_s, crnt_l)

            crnt_j_s += crnt_l

            if crnt_j_s >= l:
                crnt_j_s = 0
                crnt_i_s += crnt_l

        crnt_l //= 2

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                answer[0] += 1
            elif arr[i][j] == 1:
                answer[1] += 1

    return answer