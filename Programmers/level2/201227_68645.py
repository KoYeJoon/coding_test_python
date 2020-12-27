def solution(n):
    answer = []
    temp = [[0 for col in range(n)] for row in range(n)]
    y,x = -1,0
    num = 1
    for i in range(n):
        for j in range(i,n):
            if i%3 == 0:
                y += 1
            elif i%3 ==1 :
                x+=1
            elif i%3 == 2:
                y -= 1
                x -= 1
            temp[y][x]=num
            num += 1
    for i in range(n):
        for j in range(n):
            if temp[i][j] != 0 :
                answer.append(temp[i][j])

    return answer

print(solution(4))