def solution(n, results):
    answer = 0
    graph = [[0] * (n+1) for _ in range(n+1)]

    for winner,loser in results :
        # 이기면 1, 지면 2
        graph[winner][loser] = 1
        graph[loser][winner] = 2


    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][k]==1 and graph[k][j]==1 and i!=j:
                    graph[i][j]=1
                    graph[j][i]=2

                elif graph[i][k]==2 and graph[j][k]==1 and i!=j:
                    graph[j][i]=1
                    graph[i][j]=2

    for i in range(1,n+1):
        if graph[i].count(0)==2:
            answer += 1

    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))