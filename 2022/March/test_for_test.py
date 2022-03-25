def solution(v):
    answer = []

    xs = []
    ys = []
    for i in range(3):
        x = v[i][0]
        y = v[i][1]

        if x in xs:
            xs.remove(x)
        else:
            xs.append(x)
        if y in ys:
            ys.remove(y)
        else:
            ys.append(y)

    answer.append(xs[0])
    answer.append(ys[0])
    print(answer)
    return answer

v = [[1, 4], [3, 4], [3, 10]]
result = [1, 10]

print(solution(v) == result)