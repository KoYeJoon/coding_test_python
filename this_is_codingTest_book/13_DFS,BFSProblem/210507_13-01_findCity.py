import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

n,m,k,x = map(int,input().split())
board = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    board[a].append(b)

distance= [INF]*(n+1)
distance[x] = 0

q =deque()
q.append(x)
while q :
    now = q.popleft()
    for i in board[now]:
        if distance[i] == INF :
            distance[i] = distance[now]+1
            q.append(i)

flag = 1
for i in range(1,n+1):
    if distance[i] == k :
        print(i)
        flag = 0

if flag :
    print(-1)