# 문제 5- 광고 삽입

def time_converting(time):
    t, m, s = map(str, time.split(":"))
    return 3600*int(t) + 60*int(m) + int(s)

def solution(play_time, adv_time, logs):
    answer = ''

    play_s = time_converting(play_time)
    adv_s = time_converting(adv_time)

    if play_s <= adv_s:
        return "00:00:00"

    time_list = [0] * (play_s + 1)
    
    for log in logs:
        start, end = map(str, log.split("-"))
        # print("Here you are", start, end)
        # print("s: ", time_converting(start))
        # print("e: ", time_converting(end))
        for i in range(time_converting(start), time_converting(end) + 1):
            time_list[i] += 1
    

    max_time = 0
    raw_answer = -1
    for j in range(play_s - adv_s, -1, -1):
        total_time = 0
        for k in range(j, j + adv_s):
            total_time += time_list[k]
        if total_time >= max_time:
            max_time = total_time
            raw_answer = j
        # total_time = sum(range(time_list[j], time_list[j+adv_s]))
        # if total_time >= max_time:
        #     max_time = total_time
        #     raw_answer = j

    h = raw_answer // 3600
    m = (raw_answer - 3600*h) // 60
    s = raw_answer % 60


    answer = str(h) + ":" + str(m) + ":" + str(s)

    return answer


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
result = "01:30:59"

print("1")
print(solution(play_time, adv_time, logs))
print()

play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
result = "01:00:00"

print("2")
print(solution(play_time, adv_time, logs))
print()

play_time = "50:00:00"
adv_time = "50:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
result = "00:00:00"

print("3")
print(solution(play_time, adv_time, logs))
print()

# # 테스트 케이스 검증
# if solution(play_time, adv_time, logs) == result:
#     print("Passed")
# else:
#     print("Failed")