def solution(scores):
    if len(scores) == 1:
        return 1

    x, y = scores.pop(0)

    scores.sort(key = lambda x : (-x[0], x[1]))
    
    rank = 1
    max_bound = 0
    for score in scores:
        p, q = score
        
        if x < p and y < q:
            return -1

        if max_bound <= q:
            if x + y < p + q:
                rank += 1
            max_bound = q
        
    return rank

scores = [[2,2],[1,4],[3,2],[3,2],[2,1]]
result = 4

print(solution(scores) == result)