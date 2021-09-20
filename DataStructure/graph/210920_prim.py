'''
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''
import heapq
v,e = map(int,input().split())
vertexes = dict()
visited = [0]*(v+1)

for i in range(1,v+1):
    vertexes[i] = []

for i in range(e):
    a,b,cost = map(int,input().split())
    vertexes[a].append([cost,a,b])
    vertexes[b].append([cost,b,a])

# v-1개의 간선을 가질때까지 반복
def prim(graph,start_node):
    visited[start_node]=1
    queue = graph[start_node]
    heapq.heapify(queue)
    answer_set = []
    result = 0
    while queue:
        cost,u,v = heapq.heappop(queue)
        print(u,v)
        if not visited[v] :
            visited[v]=1
            answer_set.append((u,v))
            result += cost

            for next in graph[v]:
                if not visited[next[2]] :
                    heapq.heappush(queue,next)
    print(result)
    print(answer_set)
    return result



prim(vertexes,1)

