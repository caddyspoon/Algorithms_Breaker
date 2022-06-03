def solution(routes):
    answer = 0

    routes.sort(key=lambda x: (x[1]))
    while routes:
        s, e = routes.pop(0)
        answer += 1
        temp = []

        for idx, elm in enumerate(routes):
            p, q = elm
            if p <= e <= q:
                temp.append(idx)

            if e < p:
                break

        for idx in range(len(temp)-1, -1, -1):
            routes.pop(temp[idx])
    return answer


routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3], [-6, -4], [-12, -10], [-2, 0], [-12, -6]]
return_answer = 2
solution(routes)