INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력 받기
n = 4
m = 7


graph = [[INF,INF,INF,INF,INF],[INF,0,4,INF,6],[INF,3,0,7,INF],
         [INF,5,INF,0,4],[INF,INF,INF,2,0]]


P = [[0]*(n+1) for _ in range(n+1)]

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][k] + graph[k][b] < graph[a][b] :
                P[a][b]=k
                graph[a][b] = graph[a][k] + graph[k][b]

# 수행된 결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        # 도달할 수 없는 경우, 무한 (INFINITY)라고 출력한다.
        if graph[a][b] == INF :
            print("Infinity",end=' ')

        # 도달할 수 없는 경우 거리를 출력
        else :
            print(graph[a][b], end = ' ')
    print()

print(P)