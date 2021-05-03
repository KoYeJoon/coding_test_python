import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a< b:
        parent[b] = a
    else :
        parent[a] = b

n,m = map(int,input().split())
parent = [i for i in range(n+1)]

edges = []
for i in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
result= 0
last =0

for edge in edges :
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b) :
        union_parent(parent,a,b)
        result += cost
        last = cost

print(result-last)