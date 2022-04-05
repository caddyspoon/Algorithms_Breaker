def solution(N, number):
    if N == number:
        return 1
    dp = {1: [N]}
    answer = -1

    crntNum = 2
    while crntNum <= 8:
        clist = dp[crntNum] = []

        if int(str(N)*crntNum) == number:
            return number

        clist.append(int(str(N)*crntNum))

        for i in range(1, crntNum):
            pair_num = crntNum - i

            if i > pair_num: break

            for elm1 in dp[i]:
                for elm2 in dp[pair_num]:
                    if elm1+elm2 not in clist:
                        if elm1+elm2 == number:
                            return crntNum
                        clist.append(elm1+elm2)

                    if abs(elm1-elm2) not in clist:
                        if abs(elm1-elm2) == number:
                            return crntNum
                        clist.append(abs(elm1-elm2))

                    if elm1*elm2 not in clist:
                        if elm1*elm2 == number:
                            return crntNum
                        clist.append(elm1*elm2)

                    if elm1 > elm2:
                        elm1, elm2 = elm2, elm1
                    if elm1 != 0:
                        if elm2//elm1 == number:
                            return crntNum

                        if elm2 // elm1 not in clist:
                            clist.append(elm2//elm1)
        crntNum += 1
    return answer
