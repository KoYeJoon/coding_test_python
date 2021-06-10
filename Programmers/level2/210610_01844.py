from collections import deque

def bfs(x,y,n,m,maps,visit):
    dx = (1,0,-1,0)
    dy = (0,1,0,-1)
    queue = deque()
    queue.append((x,y))
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            if maps[nx][ny] and not visit[nx][ny]:
                visit[nx][ny] = 1
                maps[nx][ny] = maps[x][y]+1
                queue.append((nx,ny))

    if maps[n-1][m-1] == 1:
        return -1

    return maps[n-1][m-1]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for i in range(n)]
    visited[0][0]=1
    return bfs(0,0,n,m,maps,visited)

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))