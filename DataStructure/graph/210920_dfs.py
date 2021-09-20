def dfs(graph,v,visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph = [
    [],
    [2,3,8], # 1->2->3->8
    [1,7], # 2->1->7
    [1,4,5], # 3->1->4->5
    [3,5],  # 4->3->5
    [3,4],  # 5-> 3-> 4
    [7],    # 6-> 7
    [2,6,8], # 7->2->6->8
    [1,7]    # 8-> 1->7
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] *9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)