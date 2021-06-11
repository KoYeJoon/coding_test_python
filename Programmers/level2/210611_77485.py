def solution(rows, columns, queries):
    answer = []
    maps = [[0]*columns for i in range(rows)]

    for i in range(rows):
        for j in range(columns):
            maps[i][j] = (i)*columns + j + 1


    drow = (0,1,0,-1)
    dcol = (1,0,-1,0)

    for (x1,y1,x2,y2) in queries :
        min_n = rows*columns
        nx = x1 - 1
        ny = y1 - 1
        count = (y2-y1, x2-x1,y2-y1,x2-x1)
        first_val = maps[nx][ny]

        for i in range(4):
            for _ in range(count[i]):
                nx += drow[i]
                ny += dcol[i]
                temp = maps[nx][ny]
                maps[nx][ny] = first_val
                first_val=temp
                min_n = min(min_n, maps[nx][ny])

        answer.append(min_n)

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))