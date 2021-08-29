def check(x, y, board):
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    # 1. 상하좌우
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or ny<0 or nx>=5 or ny>=5 :
            continue
        if board[nx][ny]=='P':
            return False
    # 2. 2칸씩
    for i in range(4):
        nx = x+2*dx[i]
        ny = y+2*dy[i]
        if nx<0 or ny<0 or nx>=5 or ny>=5 :
            continue
        if board[nx][ny]=='P':
            if board[x+dx[i]][y+dy[i]] != 'X':
                return False

    # 3. 대각선
    ddx = [1,1,-1,-1]
    ddy = [1,-1,1,-1]
    for i in range(4):
        nx = x+ddx[i]
        ny = y+ddy[i]
        if nx<0 or ny<0 or nx>=5 or ny>=5 :
            continue
        if board[nx][ny]=='P':
            if board[x][ny] != 'X' or board[nx][y] != 'X':
                return False
    return True

def solution(places):
    answer = []
    for place in places :
        flag = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    if check(i,j,place) :
                        continue
                    else :
                        flag = 1
                        break
            if flag :
                answer.append(0)
                break
        else :
            answer.append(1)

    return answer
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))