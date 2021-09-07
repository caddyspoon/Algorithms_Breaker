from pprint import pprint

from itertools import combinations as comb
from collections import deque

def solution(info, query):
    answer = []

    info_dict = {}

    for applicant in info:
        raw_key = applicant.split()
        info_key = raw_key[:4]
        score = int(raw_key[4])

        for i in range(5):
            for actual_key in comb(info_key, i):
                key_voc = "".join(actual_key)
                try:
                    info_dict[key_voc].append(score)
                except:
                    info_dict[key_voc] = [score]

    for key in info_dict:
        info_dict[key].sort()

    for q in query:
        qraw_key = deque(q.split(" "))
        qscore = int(qraw_key.pop())
        crnt_key = ""

        while qraw_key:
            qp = qraw_key.popleft()
            if qp == "-" or qp == "and":
                continue
            crnt_key += qp
        
        cnt = 0
        if crnt_key in info_dict:
            l = info_dict[crnt_key]
            start, end = 0, len(l)
            while end > start:
                mid = (start + end) // 2
                if l[mid] >= qscore:
                    end = mid
                else:
                    start = mid + 1
            cnt = (len(l) - start)
        answer.append(cnt)

    return answer


# 테스트 케이스
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
result = [1,1,1,1,2,4]

# 테스트 케이스 검증
if solution(info, query) == result:
    print("Passed")
else:
    print("Failed")