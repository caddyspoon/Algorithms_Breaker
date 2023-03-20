def solution(n, costs):
    def find_set(x):
        if p[x] == x:
            return x
        else:
            p[x] = find_set(p[x])
            return p[x]

    def union(x, y):
        parent_x = find_set(x)
        parent_y = find_set(y)
        if parent_x > parent_y:
            p[parent_y] = parent_x
        else:
            p[parent_x] = parent_y

    costs.sort(key=lambda x: x[2])

    # make_set: 모든 정점에 대해 집합 생성
    p = [i for i in range(n)]

    cnt = 0
    result = 0
    mst = []
    # 모든 간선에 대해서 반복 -> V-1개의 간선이 선택될 때까지

    for i in range(len(costs)):
        s, e, c = costs[i]
        print(s, e)
        # 사이클이면 스킵: 간선의 두 정점이 서로 같은 집합이면 => find_set

        if find_set(s) == find_set(e):
            continue
        # 간선 선택
        # => mst에 간선 정보 더하기 / 두 정점을 합친다 => union
        result += c
        union(s, e)
        print("union p: ", p)
        # 연결한 간선 정보를 mst 리스트에 담아보자.
        mst.append(costs[i])
        cnt += 1

        if cnt == n - 1:
            break

    return result

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

solution(n, costs)