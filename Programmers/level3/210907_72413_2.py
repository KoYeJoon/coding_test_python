def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    fare_graph = [[INF]*(n+1) for i in range(n+1)]
    for i in range(1,n+1):
        fare_graph[i][i] = 0

    for st,d,c in fares :
        fare_graph[st][d] = c
        fare_graph[d][st] = c

    for k in range(1,n+1):
        for a1 in range(1,n+1):
            for b1 in range(1,n+1):
                fare_graph[a1][b1] = min(fare_graph[a1][b1], fare_graph[a1][k] + fare_graph[k][b1])

    for i in range(1,n+1):
        c = fare_graph[s][i] + fare_graph[i][a] + fare_graph[i][b]
        if c < answer :
            answer = c
    return answer


print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))