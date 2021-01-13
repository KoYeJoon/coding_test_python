def solution(m, n, board):
    answer = 0
    temp = [[0 for a in range(m)] for b in range(n)]
    board.reverse()
    for i in range(n):
        for j in range(m):
            temp[i][j] = board[j][i]

    while True :
        mark =  [[0 for a in range(m)] for b in range(n)]
        flag=0
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                if i < len(temp)-1 and j < len(temp[i])-1 and j<len(temp[i+1])-1:
                    if temp[i][j] == temp[i][j+1] == temp[i+1][j] == temp[i+1][j+1] :
                        mark[i][j] = 1
                        mark[i][j+1] = 1
                        mark[i+1][j]=  1
                        mark[i+1][j+1]=1
                        flag = 1

        for i in range(len(mark)):
            answer += sum(mark[i])

        if flag == 0:
            break

        for i in range(len(temp)):
            for j in range(len(temp[i])):
                if mark[i][j]==1:
                    temp[i][j] = '0'
            temp[i]=list(filter(lambda x : x !='0',  temp[i]))

    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))