def solution(m, n, puddles):
    dp_table = [[0]*m for _ in range(n)]
    dp_table[0][0] = 1

    for col,row in puddles :
        dp_table[row-1][col-1] = -1

    for row in range(n):
        for col in range(m):
            if dp_table[row][col] != -1:
                if row == 0 and col == 0:
                    pass
                elif row == 0 :
                    dp_table[row][col] = max(dp_table[row][col], dp_table[row][col-1])
                elif col == 0:
                    dp_table[row][col] = max(dp_table[row][col], dp_table[row-1][col])
                else:
                    dp_table[row][col] = max(dp_table[row][col], dp_table[row-1][col]+dp_table[row][col-1], dp_table[row-1][col],dp_table[row][col-1])


    return dp_table[-1][-1]%1000000007 if dp_table[-1][-1] > 0 else 0


print(solution(4,3,[[2,2]]))