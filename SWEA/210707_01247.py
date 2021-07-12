T = int(input())
INF = int(1e9)
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def getdistance(pos1, pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

def bfs():
    stack = []
    if 

for test_case in range(1, T + 1):
    costumer_n = int(input())
    list_n = list(map(int,input().split()))

    costumer_pos = []
    company_graph = []
    home_graph = []
    costumer_graph = [[INF] * (costumer_n+1) for _ in range(costumer_n+1)]

    for i in range(0,2*(costumer_n+2),2):
        if i== 0 :
            company_pos = [list_n[i],list_n[i+1]]
        elif i==2 :
            home_pos = [list_n[i],list_n[i+1]]
        else :
            costumer_pos.append([list_n[i],list_n[i+1]])

    # company_Graph 채우기
    for i in range(costumer_n):
        company_graph.append(getdistance(company_pos,costumer_pos[i]))

    # home_graph 채우기
    for i in range(costumer_n):
        home_graph.append(getdistance(home_pos,costumer_pos[i]))

    # costumer_graph 채우기
    for i in range(costumer_n):
        for j in range(i,costumer_n):
            cost = getdistance(costumer_pos[i], costumer_pos[j])
            costumer_graph[i][j] = cost
            costumer_graph[j][i] = cost

    # bfs


    # 비용체크
    print(costumer_graph)
    min_value = INF
    for st in range(costumer_n):
        costumer_graph[st][st] = INF
        min_distance = min(costumer_graph[st])
        dist = costumer_graph[st].index(min_distance)

        if min_value > company_graph[st] + min_distance + home_graph[dist] :
            min_value = company_graph[st] + min_distance + home_graph[dist]

    print(f'#{test_case} {min_value}')

