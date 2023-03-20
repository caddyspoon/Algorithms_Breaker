import heapq

V, E = map(int, input().split())    # 각 정점과 간선의 갯수
adj = {i:[] for i in range(V)}
for i in range(E):
    s, e, c, = map(int, input().split())
    adj[s].append([e, c])
    adj[e].append([s, c])
# key, mst, 우선순위 큐 준비
INF = float('inf')
key = [INF] * V
mst = [False] * V
pq = [] # 우선순위 큐
# 시작 정점 선택: 0
key[0] = 0
# 큐 시작 정점을 넣음 => (key, 정점 인덱스)
# 우선순위 큐 -> 이진힙 -> heapq 라이브러리 사용
heapq.heappush(pq, (0,0))
# 힙의 구조를 유지하면서 하나의 새로운 원소를 집어 넣어줌, 배열 정보와 어떤 원소를 집어 넣을지 입력해준다.
# 우선순위큐 -> 원소의 첫 번째 요소로 pop을 함 -> 그렇담 key를 우선순위로.

result = 0
while pq:
    # 최소값 찾기
    k, node = heapq.heappop(pq)
    if mst[node]: continue
    # mst로 선택
    mst[node] = True
    result += k
    # key 갱신 => key배열/큐
    for dest, wt in adj[node]:  # 가고자 하는 곳 dest, 가중치 wt
        if not mst[dest] and key[dest] > wt:
            key[dest] = wt
            # 큐 갱신 => 새로운 (key, 정점) 삽입 => 필요없는 원소는 스킵
            heapq.heappush(pq, (key[dest], dest))