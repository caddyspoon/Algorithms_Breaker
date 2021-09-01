for _ in range(int(input())):
    n = int(input())

    arr = [0, 1, 2, 4]

    if n < 4: 
        print(arr[n])

    else:
        for i in range(4, n+1):
            crnt_cnt = 0
            for elm in (1, 2, 3):
                stnd = i - elm
                crnt_cnt += arr[stnd]
            arr.append(crnt_cnt)
        print(arr[n])

