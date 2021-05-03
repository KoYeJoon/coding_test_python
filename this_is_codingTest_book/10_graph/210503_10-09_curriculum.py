'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''
import sys
from collections import deque
import copy

input = sys.stdin.readline
n = int(input())
indegree = [0] *(n+1)
graph = [[] for i in range(n+1)]
duration = [0] * (n+1)

for i in range(1,n+1):
    data = list(map(int,input().split()))
    duration[i] = data[0]
    for j in data[1:-1]:
        indegree[i] += 1
        # 선수 과목에 현재 과목 꼬리달기
        graph[j].append(i)

def topology_sort() :
    result=copy.deepcopy(duration)
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    while q :
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+duration[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1,n+1):
        print(result[i])


topology_sort()