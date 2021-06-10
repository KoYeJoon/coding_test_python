'''
시간 초과
import copy

n,k = map(int,input().split())
current = []

for i in range(n):
    current.append(list(map(int,input().split())))

s,x,y = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def virus(x,y,current_k):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        # 퍼질 수 있음
        if nx>-1 and ny>-1 and nx < n and ny < n :
            if new[nx][ny] == 0:
                new[nx][ny] = current_k


# 몇 초동안
for i in range(s):
    new = copy.deepcopy(current)
    # 바이러스 1번부터 k까지
    for j in range(1,k+1):
        # current 에서 현재 k번 바이러스 인 경우, 전파시키기
        for a in range(n):
            for b in range(n):
                if current[a][b] == j :
                    virus(a,b,j)

    current = new

print(current[x-1][y-1])
'''

from collections import deque

n,k = map(int,input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0 :
            data.append([graph[i][j],0,i,j])

data.sort()
q=deque(data)

target_s,target_x,target_y = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]


while q:
    virus,s,row,col = q.popleft()
    if s == target_s :
        break
    for i in range(4):
        nx = row+dx[i]
        ny = col+dy[i]

        if 0<=nx and nx < n and 0<=ny and ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append([virus,s+1,nx,ny])

print(graph[target_x-1][target_y-1])