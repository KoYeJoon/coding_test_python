def solution(n, edge):
    answer = 0
    INF = int(1e9)
    cost = [INF]*(n+1)
    cost[1] = 0
    queue = [1]

    graph = [[] for i in range(n+1)]
    # 그래프 변형
    for a,b in edge :
        graph[a].append(b)
        graph[b].append(a)

    while queue :
        cur = queue.pop(0)

        for dist in graph[cur]:
            if cost[cur] + 1 < cost[dist] :
                cost[dist] = cost[cur] + 1
                queue.append(dist)

    max_num = max(cost[1:])
    for i in cost[1:]:
        if i==max_num:
            answer += 1

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))