import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수, 시작 노드 입력 받기
n,m,c = map(int,input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력 받기
for _ in range(m):
    x,y,z = map(int,input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q :
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now] :
            cost = dist+i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우ㅜ
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# 다익스트라 알고리즘 수행
dijkstra(c)

count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance :
    if d!=INF :
        count +=1
        max_distance = max(max_distance,d)

print(count-1, max_distance)