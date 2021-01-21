from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
bigmap = []

for i in range(n):
    arr = list(stdin.readline())
    bigmap.append(arr[:-1])


dx = (-1,1,0,0)
dy = (0,0,-1,1)
visit = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
queue = deque()


def init() :
    rx,ry,bx,by = 0,0,0,0
    for i in range(n) :
        for j in range(m) :
            if bigmap[i][j] == 'R' :
                rx,ry = i,j
            elif bigmap[i][j] == 'B' :
                bx,by = i,j

    queue.append((rx,ry,bx,by,1))
    visit[rx][ry][bx][by] = True


def move(x,y,dx,dy):
    count = 0
    while bigmap[x+dx][y+dy] != '#' and bigmap[x][y] != 'O' :
        x+=dx
        y+=dy
        count += 1

    return x,y,count


def bfs():
    init()

    while queue :
        rx,ry,bx,by,depth = queue.popleft()
        if depth > 10 :
            break

        # left, right, top, bottom
        for i in range(4) :
            # red
            new_rx, new_ry , r_dph = move(rx,ry,dx[i],dy[i])
            # blue
            new_bx, new_by, b_dph = move(bx,by,dx[i],dy[i])
            if bigmap[new_bx][new_by] == 'O' :
                continue
            if bigmap[new_rx][new_ry] == 'O':
                return depth

            # 빨간 공과 파란 공의 위치가 같은 경우
            if new_rx == new_bx and new_ry == new_by :
                if r_dph > b_dph :
                    new_rx -= dx[i]
                    new_ry -= dy[i]
                else :
                    new_bx -= dx[i]
                    new_by -= dy[i]

            if not visit[new_rx][new_ry][new_bx][new_by] :
                visit[new_rx][new_ry][new_bx][new_by] = True
                queue.append((new_rx,new_ry,new_bx,new_by,depth+1))

    return -1



print(bfs())
