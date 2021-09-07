INF = int(1e9)
# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node(distance, visited,n):
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드 (인덱스 )
    for i in range(1,n+1) :
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            index = i

    return index

def dijkstra(start,n,graph):
    # 시작 노드에 대해서 초기화
    visited = [False] * (n+1)
    # 최단 거리 테이블을 무한으로 초기화
    distance = [INF] * (n+1)
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node(distance,visited,n)
        visited[now] = True

        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]] :
                distance[j[0]] = cost


    return distance

def solution(n, s, a, b, fares):
    answer = INF
    fare_graph = [[] for i in range(n+1)]
    for st,d,c in fares :
        fare_graph[st].append((d,c))
        fare_graph[d].append((st,c))

    common_distance = dijkstra(s,n,fare_graph)
    a_distance = dijkstra(a,n,fare_graph)
    b_distance = dijkstra(b,n,fare_graph)

    for i in range(1,n+1):
        c = common_distance[i] + a_distance[i] + b_distance[i]
        if c<answer:
            answer = c

    return answer


print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))