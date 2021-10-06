def find_parent(parent,x):
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b :
        parent[b]=a
    else :
        parent[a] = b

def solution(n, wires):
    answer = n+1

    for i in range(n-1):
        remain_wires = wires[:i] + wires[i+1:]
        parent = [p for p in range(n+1)]

        for rw_a,rw_b in remain_wires :
            union_parent(parent,rw_a,rw_b)

        for j in range(1,n+1):
            find_parent(parent,j)

        if answer > abs(2*parent.count(parent[1])-n) :
            answer = abs(2*parent.count(parent[1])-n)

    return answer

# def dfs(wire_info,start,n):
#     stack = [start]
#     visited = [0]*(n+1)
#     count = 0
#     while stack :
#         x = stack.pop()
#         visited[x] = 1
#         count += 1
#         for w in wire_info[x] :
#             if not visited[w] :
#                 stack.append(w)
#     return count
#
#
# def solution(n,wires):
#     answer = n+1
#     cut_wires = list(wires)
#     while cut_wires:
#         cut_wire_a, cut_wire_b = cut_wires.pop()
#         wire_info = [[] for _ in range(n+1)]
#         for a,b in wires :
#             if a == cut_wire_a and b == cut_wire_b :
#                 continue
#             wire_info[a].append(b)
#             wire_info[b].append(a)
#         differ = abs(2*(dfs(wire_info,cut_wire_a,n))-n)
#         if answer > differ:
#             answer = differ
#     return answer

print(solution(	7, [ [4, 5],[2, 7] ,[1, 2],[3, 7], [3, 4],  [6, 7]]))