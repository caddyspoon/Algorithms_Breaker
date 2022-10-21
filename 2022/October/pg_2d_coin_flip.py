def solution(beginning, target):
    answer = 0
    stand_row = ""
    
    h = len(beginning)
    w = len(beginning[0])
    
    for i in range(h):
        crnt_row = ''
        for j in range(w):
            if (beginning[i][j] != target[i][j]):
                crnt_row += '1'
                
                if i == 0:
                    answer += 1
                else:
                    if stand_row[0] == '0' and j == 0:
                        answer += 1
            else:
                crnt_row += '0'
                print(stand_row)
                if i > 0 and stand_row[0] == '1' and j == 0:
                    answer += 1
    
        if i == 0:
            stand_row = crnt_row
        else:
            if stand_row != crnt_row:
                if not int(stand_row) + int(crnt_row) == int('1' * w):
                    return -1
                
    return min(answer, h + w - answer)

beginning = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
target = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
result = 5

print(solution(beginning, target))