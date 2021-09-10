# https://haeseok.medium.com/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B2%BD%EC%A3%BC%EB%A1%9C-%EA%B1%B4%EC%84%A4-6331021a7536

from collections import deque
def calc_cost(cur_dir, nex_dir, cost):
    if (cur_dir == 'R' or cur_dir == 'L') and (nex_dir == 'L' or nex_dir == 'R'):
        return cost + 100
    if (cur_dir == 'D' or cur_dir == 'U') and (nex_dir == 'D' or nex_dir == 'U'):
        return cost + 100
    if (cur_dir == 'R' or cur_dir == 'L') and (nex_dir == 'D' or nex_dir == 'U'):
        return cost + 500 + 100
    if (cur_dir == 'D' or cur_dir == 'U') and (nex_dir == 'R' or nex_dir == 'L'):
        return cost + 500 + 100


def bfs(x, y, cost, direct,board):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    dir = ['R','D','L','U']
    n = len(board)
    queue = deque([(x, y, cost, direct)])
    check = [[0]*n for _ in range(n)]
    check[x][y] = 1

    while queue:
        x, y, cost, cur_dir = queue.popleft()
        if x == n-1 and y == n-1:
            answer.append(cost)
            continue
        for i in range(4):
            new_x, new_y, new_cost = x+dx[i], y+dy[i], calc_cost(cur_dir, dir[i], cost)
            if new_x < 0 or new_y < 0 or new_x > n-1 or new_y >n-1:
                continue
            if not board[new_x][new_y]:
                if not check[new_x][new_y] or check[new_x][new_y] > new_cost:
                    check[new_x][new_y] = new_cost
                    queue.append((new_x, new_y, new_cost, dir[i]))


def solution(board):
    global answer
    answer = []

    bfs(0, 0, 0, 'R',board)
    bfs(0, 0, 0, 'D',board)
    return min(answer)

print(solution([[0,0,0],[0,0,0],[0,0,0]]))