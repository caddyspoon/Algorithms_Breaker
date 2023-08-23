# 중복조합
from itertools import combinations_with_replacement as comb_re

def solution(k, n, req):
    answer = float('inf')

    # 해당 과목에서 최대 배치 가능한 인원 수
    l = n - k + 1

    # 유형 배치도
    master_info = [[[float('inf'), float('inf')] for _ in range(l)] for _ in range(k)]

    def do_councel(councel_info, req=req):
        waiting_time = 0

        # 초기화
        for i in range(k):
            temp_councel_cnt = councel_info[i]
            for j in range(l):
                if j < temp_councel_cnt:
                    master_info[i][j] = [0, 0]
                else:
                    master_info[i][j] = [float('inf'), float('inf')]

        for mentee_info in req:
            req_time, spent_time, council_type = mentee_info

            # 해당 유형의 멘토들 상담 정보
            mento_timetable = master_info[council_type - 1]

            # 종료시간이 제일 빠른 순으로 정렬되어 있는 리스트의 첫 항목
            mento_info = mento_timetable[0]

            # 멘토_인포 = [종료시간, 시작시간]
            curr_end = mento_info[0]
            no_delay = curr_end <= req_time

            if no_delay:
                mento_info[1] = req_time
                mento_info[0] = req_time + spent_time
            else:
                waiting_time += mento_info[0] - req_time
                if waiting_time > answer:
                    return float('inf')

                mento_info[1] = mento_info[0]
                mento_info[0] += spent_time

            # 각 항목의 멘토 시간 정보 중 0번 인덱스가 제일 일찍 끝나는 멘토 시간 정보가 되도록 정렬
            master_info[council_type - 1].sort()

        return waiting_time    


    def set_schedule():
        nonlocal answer

        for arr in list(comb_re(range(k), n - k)):
            councel_info = [1] * k
            for idx in arr:
                councel_info[idx] += 1
            answer = min(answer, do_councel(councel_info))

    set_schedule()

    return answer