def solution(n, computers):
    answer = 1
    graph = [[] for i in range(n)]
    visited = [0]*n
    for i in range(n):
        for j in range(n):
            if computers[i][j] and i!=j:
                graph[i].append(j)

    queue = [0]
    while queue :
        pos = queue.pop(0)
        visited[pos]=1
        for new_pos in graph[pos]:
            if not visited[new_pos]:
                queue.append(new_pos)
        if len(queue)==0 and sum(visited)<n:
            queue.append(visited.index(0))
            answer += 1

    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))