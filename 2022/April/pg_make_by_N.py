def solution(N, number):
    if N == number:
        return 1
    dp = {1: [N]}
    answer = -1

    crntNum = 2
    while crntNum <= 8:
        clist = dp[crntNum] = []

        if int(str(N)*crntNum) == number:
            return crntNum

        clist.append(int(str(N)*crntNum))

        for i in range(1, crntNum):
            pair_num = crntNum - i

            for elm1 in dp[i]:
                for elm2 in dp[pair_num]:

                    if elm1+elm2 not in clist:
                        if elm1+elm2 == number:
                            return crntNum
                        clist.append(elm1+elm2)

                    if elm1-elm2 not in clist:
                        if elm1-elm2 == number:
                            return crntNum
                        clist.append(elm1-elm2)

                    if elm1*elm2 not in clist:
                        if elm1*elm2 == number:
                            return crntNum
                        clist.append(elm1*elm2)

                    if elm2 != 0:
                        if elm1 // elm2 not in clist:
                            if elm1 // elm2 == number:
                                return crntNum
                            clist.append(elm1//elm2)
        crntNum += 1
    return answer

N = 5
number = 12
result = 4

print(solution(N, number))