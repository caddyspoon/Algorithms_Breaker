from itertools import product

def solution(users, emoticons):
    dc_rate = [10, 20, 30, 40]
    
    temp_arr = [0] * len(emoticons)
    
    # 주어진 할인율에 따라 계산하는 함수
    def cal(dc_info):
        sub_cnt = 0
        profit = 0
        for user in users:
            dc_cut, budget = user
            sum_cost = 0

            for idx, emo in enumerate(emoticons):
                if dc_cut <= dc_info[idx]:
                    sum_cost += emo - int(emo * (dc_info[idx] / 100))

                    # FIXME: 아래 계산식으로는 통과하지 못함
                    # sum_cost += int((100 - dc_info[idx]) / 100  * emo)
                    # 위의 식을 아래로 바꾸면 통과 함
                    # sum_cost += (100 - dc_info[idx]) / 100  * emo
                    # sum_cost = int(sum_cost)
            
                if sum_cost >= budget:
                    sub_cnt += 1
                    break
            else:
                profit += sum_cost
                        
        return [sub_cnt, profit]
                    
    result = [0, 0]

    # option 1. 중복함수로 해결
#     for info in product(dc_rate, repeat=len(emoticons)):
#         print(info)
#         cnrt_result = cal(info)
#         sub_cnt, profit = cnrt_result

#         if sub_cnt > result[0]:
#             result = cnrt_result

#         elif sub_cnt == result[0]:
#             if profit > result[1]:
#                 result = cnrt_result

    # option 2. 재귀로 해결
    def recur_sale(my_idx = 0, my_arr = temp_arr):
        nonlocal result

        if my_idx == len(emoticons):
            crnt_result = cal(my_arr)
            if crnt_result[0] > result[0]:
                result = crnt_result[:]
            elif crnt_result[0] == result[0]:
                if crnt_result[1] > result[1]:
                    result = crnt_result[:]
            return
        
        for dc in dc_rate:
            my_arr[my_idx] = dc
            recur_sale(my_idx + 1, my_arr)
    
    recur_sale()

    return result