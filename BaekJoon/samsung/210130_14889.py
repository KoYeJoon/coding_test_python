from sys import stdin
import itertools
n = int(stdin.readline())

effect=[]
for i in range(n):
    arr = list(map(int,stdin.readline().split()))
    effect.append(arr)

n_list = list(range(n))
combi_list = list(itertools.combinations(n_list,n//2))
min = 1000


for i in range(len(combi_list)//2) :
    temp = list(n_list)
    sum1 = 0
    sum2 = 0

    for j in combi_list[i]:
        for k in combi_list[i]:
            sum1 += effect[j][k]

    for j in range(n//2):
        temp.remove(combi_list[i][j])

    for j in temp :
        for k in temp:
            sum2 += effect[j][k]

    if min > abs(sum1 - sum2) :
        min = abs(sum1 - sum2)

print(min)