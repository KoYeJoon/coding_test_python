'''
def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    graph = [[INF]*(N+1) for i in range(N+1)]

    for i in range(N+1):
        for j in range(N+1):
            if i==j:
                graph[i][j] = 0

    for a,b,c in road :
        if graph[a][b] > c:
            graph[a][b] = c
            graph[b][a] = c

    for pass_through in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                graph[i][j] = min(graph[i][j], graph[i][pass_through]+graph[pass_through][j])


    for i in range(1,len(graph[1])) :
        if graph[1][i]<= K:
            answer += 1

    return answer
'''

def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    cost = [INF] * (N+1)
    cost[1] = 0
    queue = [1]
    while queue :
        pos = queue.pop(0)
        for a,b,c in road:
            if a==pos or b==pos:
                dist = a
                if a==pos:
                    dist = b
                if c+cost[pos] < cost[dist]:
                    cost[dist] = c+cost[pos]
                    queue.append(dist)

    for i in cost :
        if i <= K :
            answer += 1
    return answer

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))