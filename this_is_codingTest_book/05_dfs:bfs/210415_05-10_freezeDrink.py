'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''
n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<0 or x>n-1 or y<0 or y>m-1 :
        return False
    if graph[x][y]:
        return False
    graph[x][y] = 1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True

count = 0
for a in range(n):
    for b in range(m):
        if dfs(a,b) :
            count += 1

print(count)