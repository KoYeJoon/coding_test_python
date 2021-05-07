import sys
import itertools

input = sys.stdin.readline

n,m = map(int,input().split())
board = []
INF = int(1e9)

for i in range(n):
    board.append(list(map(int,input().split())))

home_arr = []
chicken_arr =[]
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home_arr.append([i,j])
        elif board[i][j]==2:
            chicken_arr.append([i,j])


chick_combi = list(itertools.combinations(chicken_arr,m))

total = INF
for chicken in chick_combi:
    min_total = 0
    for home in home_arr:
        min_temp = INF
        for temp in chicken :
            distance = abs(temp[0]-home[0]) + abs(temp[1]-home[1])
            min_temp = min(min_temp,distance)

        min_total += min_temp

    total = min(total,min_total)


print(total)