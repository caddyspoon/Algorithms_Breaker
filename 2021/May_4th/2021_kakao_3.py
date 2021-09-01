def cvtt(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s


def solution(play_time, adv_time, logs):
    answer = ''

    total_time = [False] * 360000

    for log in logs:
        stime, etime = map(str, log.split('-'))
        sseconds = cvtt(stime)
        eseconds = cvtt(etime)
        total_time[sseconds] = total_time[sseconds] + 1
        total_time[eseconds] = total_time[eseconds] - 1
    
    for i in range(1, cvtt(play_time)-1):
        total_time[i] = total_time[i] + total_time[i-1]
    
    for i in range(1, cvtt(play_time)-1):
        total_time[i] = total_time[i] + total_time[i-1]
    
    max_time = 0
    sa = 0
    ea = 0
    for i in range(cvtt(adv_time)-1, cvtt(play_time) - 1):
        if i >= cvtt(adv_time):
            bm = max_time
            max_time = max(max_time, total_time[i] - total_time[i - cvtt(adv_time)])
            if bm != max_time:
                sa = total_time[i - cvtt(adv_time)]
                ea = total_time[i]
        else:
            bm = max_time
            max_time = max(max_time, total_time[i])
    H = ea
    print(H)
    return answer


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

solution(play_time, adv_time, logs)