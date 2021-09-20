'''
5 8
1
1 2 -1
1 3 4
2 3 3
2 4 2
2 5 2
4 2 1
4 3 5
5 4 -3
'''
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 10억을 설정

# 노드의 개수, 간선의 개수 입력 받기
n,m = map(int, input().split())
# 시각 노드 번호를 입력 받기
start = int(input())
edges = []
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
vistied = [False] * (n+1)
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력 받기
for _ in range(m):
    u,v,cost = map(int, input().split())
    # u번 노드에서 v번 노드로 가는 비용이 cost라는 의미이다.
    edges.append((u,v,cost))



def bellman_ford(graph,start) :
    distance[start]= 0
    for i in range(n):
        for j in range(m):
            node = graph[j][0]
            next = graph[j][1]
            cost = graph[j][2]
            if distance[node] != INF and distance[next] > distance[node]+cost :
                distance[next]=distance[node]+cost
                if i== n-1 :
                    return True

    return False

negative_cycle = bellman_ford(edges,1)
if negative_cycle :
    print('-1')
else :
    for i in range(1,n+1):
        if distance[i]==INF:
            print('-1')
        else :
            print(distance[i])