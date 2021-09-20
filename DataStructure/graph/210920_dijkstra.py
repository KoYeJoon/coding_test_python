
'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 10억을 설정

# 노드의 개수, 간선의 개수 입력 받기
n,m = map(int, input().split())
# 시각 노드 번호를 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
vistied = [False] * (n+1)
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력 받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미이다.
    graph[a].append((b,c))


# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드 (인덱스 )
    for i in range(1,n+1) :
        if distance[i] < min_value and not vistied[i] :
            min_value = distance[i]
            index = i

    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    vistied[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        vistied[now] = True

        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]] :
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1,n+1):
    # 도달할 수 없는 경우, INF로 출력
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])