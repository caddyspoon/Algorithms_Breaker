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

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(E)]

# 간선을 간선 가중치를 기준으로 정렬
edges.sort(key=lambda x: x[2])
print(edges)

# make_set: 모든 정점에 대해 집합 생성
p = [i for i in range(V)]
rank = [0] * V

cnt = 0
result = 0
mst = []
# 모든 간선에 대해서 반복 -> V-1개의 간선이 선택될 때까지

for i in range(E):
    s, e, c = edges[i][0], edges[i][1], edges[i][2]
    # 사이클이면 스킵: 간선의 두 정점이 서로 같은 집합이면 => find_set
    if find_set(s) == find_set(e):
        continue
    # 간선 선택
    # => mst에 간선 정보 더하기 / 두 정점을 합친다 => union
    result += c
    union(s, e)

    # 연결한 간선 정보를 mst 리스트에 담아보자.
    mst.append(edges[i])
    cnt += 1

    if cnt == V-1:
        break

# 결과를 확인해보자.
print(result)

# mst를 확인해보자.
print(mst)